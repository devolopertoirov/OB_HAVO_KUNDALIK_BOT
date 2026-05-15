import httpx
import config
from languages import t


def get_rain_type(code: int, til: str) -> str:
    if 51 <= code <= 67:
        return t("yomgir", til)
    elif 71 <= code <= 77:
        return t("qor", til)
    elif 89 <= code <= 90:
        return t("dol", til)
    else:
        return t("yomgir_yoq", til)


async def get_weather(lat: float, long: float, til: str = "uz") -> str:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={long}"
        f"&hourly=temperature_2m,precipitation,weathercode"
        f"&timezone=auto"
    )
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url)
        data = response.json()

    indeks     = config.soat
    temp       = data["hourly"]["temperature_2m"][indeks]
    rain       = data["hourly"]["precipitation"][indeks]
    code       = data["hourly"]["weathercode"][indeks]
    rain_info  = get_rain_type(code, til) if rain > 0 else t("yomgir_yoq", til)

    return (
        f"{t('ob_havo_sarlavha', til)}\n"
        f"🕐 {config.soat:02d}:{config.minut:02d} — {temp}°C\n"
        f"{rain_info}"
    )
