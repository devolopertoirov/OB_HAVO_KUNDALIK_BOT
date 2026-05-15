from apscheduler.schedulers.asyncio import AsyncIOScheduler
from weather import get_weather
from config import kundalik_kanal, viloyatlar, admin_ids
import config


async def send_daily_weather(bot):
    for nom, (lat, lon) in viloyatlar.items():
        natija = await get_weather(lat=lat, long=lon, til="uz")
        xabar  = f"🌍 {nom}\n{natija}"
        for kanal in kundalik_kanal:
            await bot.send_message(chat_id=kanal, text=xabar)


def start_scheduler(bot):
    scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")
    scheduler.add_job(
        send_daily_weather,
        "cron",
        hour=config.soat,
        minute=config.minut,
        args=[bot]
    )
    scheduler.start()
    return scheduler


async def send_now(update, context):
    user_id = update.effective_chat.id
    if user_id not in admin_ids:
        return
    await send_daily_weather(context.bot)
