import config
TILLAR = {
    "uz": {
        "til_tanlash_xush": "🌍 Xush kelibsiz! Iltimos, tilni tanlang:",
        "til_tanlang": "🌎 TILNI TANLANG 👇",
        "til_saqlandi": "✅ Til tanlandi: {til_nomi}",
        "til_allaqachon": "✅ {til_nomi} allaqachon tanlangan",
        "til_tugmasi": "🌎 TILNI O'ZGARTIRISH",

        "start_xush_kelibsiz": (
            "Assalomu alaykum! 👋\n"
            "Ob-havoni bilish uchun joylashuvingizni yuboring 📍\n"
            "Joylashuvingiz sir tutilishi kafolatlanadi.\n"
            f"Bot yaratuvchisi: {config.admin_username}"
        ),
        "obuna_kerak": "❌ Botdan foydalanish uchun kanallarga obuna bo'ling!",
        "joylashuv_tugmasi": "📍 JOYLASHUVNI YUBORISH",
        "joylashuv_qabul": (
            "✅ Joylashuvingiz qabul qilindi!\n"
            "Ob-havo olish uchun /getweather buyrug'ini kiriting."
        ),
        "joylashuv_yoq": "❌ Avval joylashuvingizni yuboring!",
        "joylashuv_ozgartirish": "📍 JOYLASHUVNI O'ZGARTIRISH",

        "asosiy_menyu": "🏠 Asosiy menyu",
        "sozlamalar_tugmasi": "⚙️ SOZLAMALAR",
        "getweather_tugmasi": "🌤 OB-HAVONI OLISH",

        "bolim_tanlang": "⚙️ BO'LIMNI TANLANG 👇",
        "vaqt_tugmasi": "⏳ VAQTNI O'ZGARTIRISH",
        "sana_tugmasi": "🗓 SANANI O'ZGARTIRISH",
        "orqaga_tugmasi": "🔙 ORQAGA",

        "soat_sozlang": "⏳ SOATNI PASTDAGI TUGMALAR ORQALI SOZLANG 👇",
        "soat_saqlash": "☑️ SOATNI SAQLASH",
        "soat_min_xato": "⛔ Soat 0 dan past bo'lmaydi",
        "soat_max_xato": "⛔ Soat 23 dan oshib ketmaydi",
        "soat_saqlandi": "✅ Soat {soat:02d} ga sozlandi!\n\n⏱ ENDI MINUTNI SOZLANG 👇",

        "minut_saqlash": "☑️ MINUTNI SAQLASH",
        "minut_min_xato": "⛔ Minut 0 dan past bo'lmaydi",
        "minut_max_xato": "⛔ Minut 59 dan oshib ketmaydi",
        "vaqt_saqlandi": "✅ Vaqt sozlandi: {soat:02d}:{minut:02d}\n\nOb-havo olish uchun /getweather kiriting.",

        "sana_kiriting": "📅 Sana kiriting (masalan: 2026-05-20):",
        "sana_saqlandi": "✅ Sana saqlandi: {sana}\nOb-havo olish uchun /getweather buyrug'ini kiriting.",
        "sana_xato": "❌ Noto'g'ri format! YYYY-MM-DD formatida kiriting.\nMasalan: 2026-05-20",

        "ob_havo_sarlavha": "🌤 OB-HAVO",
        "yomgir_yoq": "☀️ Yog'in yo'q",
        "yomgir": "🌧️ Yomg'ir",
        "qor": "❄️ Qor",
        "dol": "🌨️ Do'l",
    },

    "ru": {
        "til_tanlash_xush": "🌍 Добро пожаловать! Пожалуйста, выберите язык:",
        "til_tanlang": "🌎 ВЫБЕРИТЕ ЯЗЫК 👇",
        "til_saqlandi": "✅ Язык выбран: {til_nomi}",
        "til_allaqachon": "✅ {til_nomi} уже выбран",
        "til_tugmasi": "🌎 ИЗМЕНИТЬ ЯЗЫК",

        "start_xush_kelibsiz": (
            "Привет! 👋\n"
            "Отправьте своё местоположение, чтобы узнать погоду 📍\n"
            "Ваше местоположение останется конфиденциальным.\n"
            f"Создатель бота: {config.admin_username}"
        ),
        "obuna_kerak": "❌ Подпишитесь на каналы, чтобы использовать бота!",
        "joylashuv_tugmasi": "📍 ОТПРАВИТЬ МЕСТОПОЛОЖЕНИЕ",
        "joylashuv_qabul": (
            "✅ Местоположение принято!\n"
            "Для получения погоды введите /getweather."
        ),
        "joylashuv_yoq": "❌ Сначала отправьте своё местоположение!",
        "joylashuv_ozgartirish": "📍 ИЗМЕНИТЬ МЕСТОПОЛОЖЕНИЕ",

        "asosiy_menyu": "🏠 Главное меню",
        "sozlamalar_tugmasi": "⚙️ НАСТРОЙКИ",
        "getweather_tugmasi": "🌤 ПОЛУЧИТЬ ПОГОДУ",

        "bolim_tanlang": "⚙️ ВЫБЕРИТЕ РАЗДЕЛ 👇",
        "vaqt_tugmasi": "⏳ ИЗМЕНИТЬ ВРЕМЯ",
        "sana_tugmasi": "🗓 ИЗМЕНИТЬ ДАТУ",
        "orqaga_tugmasi": "🔙 НАЗАД",

        "soat_sozlang": "⏳ НАСТРОЙТЕ ЧАС С ПОМОЩЬЮ КНОПОК 👇",
        "soat_saqlash": "☑️ СОХРАНИТЬ ЧАС",
        "soat_min_xato": "⛔ Час не может быть меньше 0",
        "soat_max_xato": "⛔ Час не может быть больше 23",
        "soat_saqlandi": "✅ Час установлен: {soat:02d}\n\n⏱ ТЕПЕРЬ НАСТРОЙТЕ МИНУТЫ 👇",

        "minut_saqlash": "☑️ СОХРАНИТЬ МИНУТЫ",
        "minut_min_xato": "⛔ Минуты не могут быть меньше 0",
        "minut_max_xato": "⛔ Минуты не могут быть больше 59",
        "vaqt_saqlandi": "✅ Время установлено: {soat:02d}:{minut:02d}\n\nДля погоды введите /getweather.",

        "sana_kiriting": "📅 Введите дату (например: 2026-05-20):",
        "sana_saqlandi": "✅ Дата сохранена: {sana}\nДля погоды введите /getweather.",
        "sana_xato": "❌ Неверный формат! Введите в формате YYYY-MM-DD.\nНапример: 2026-05-20",

        "ob_havo_sarlavha": "🌤 ПОГОДА",
        "yomgir_yoq": "☀️ Осадков нет",
        "yomgir": "🌧️ Дождь",
        "qor": "❄️ Снег",
        "dol": "🌨️ Град",
    },

    "en": {
        "til_tanlash_xush": "🌍 Welcome! Please select your language:",
        "til_tanlang": "🌎 SELECT LANGUAGE 👇",
        "til_saqlandi": "✅ Language selected: {til_nomi}",
        "til_allaqachon": "✅ {til_nomi} is already selected",
        "til_tugmasi": "🌎 CHANGE LANGUAGE",

        "start_xush_kelibsiz": (
            "Hello! 👋\n"
            "Send your location to get the weather 📍\n"
            "Your location is guaranteed to remain private.\n"
            f"Bot creator: {config.admin_username}"
        ),
        "obuna_kerak": "❌ Please subscribe to the channels to use this bot!",
        "joylashuv_tugmasi": "📍 SEND LOCATION",
        "joylashuv_qabul": (
            "✅ Location received!\n"
            "Type /getweather to get the forecast."
        ),
        "joylashuv_yoq": "❌ Please send your location first!",
        "joylashuv_ozgartirish": "📍 CHANGE LOCATION",

        "asosiy_menyu": "🏠 Main menu",
        "sozlamalar_tugmasi": "⚙️ SETTINGS",
        "getweather_tugmasi": "🌤 GET WEATHER",

        "bolim_tanlang": "⚙️ SELECT A SECTION 👇",
        "vaqt_tugmasi": "⏳ CHANGE TIME",
        "sana_tugmasi": "🗓 CHANGE DATE",
        "orqaga_tugmasi": "🔙 BACK",

        "soat_sozlang": "⏳ ADJUST THE HOUR USING THE BUTTONS BELOW 👇",
        "soat_saqlash": "☑️ SAVE HOUR",
        "soat_min_xato": "⛔ Hour cannot be less than 0",
        "soat_max_xato": "⛔ Hour cannot be more than 23",
        "soat_saqlandi": "✅ Hour set to {soat:02d}\n\n⏱ NOW ADJUST THE MINUTES 👇",

        "minut_saqlash": "☑️ SAVE MINUTES",
        "minut_min_xato": "⛔ Minutes cannot be less than 0",
        "minut_max_xato": "⛔ Minutes cannot be more than 59",
        "vaqt_saqlandi": "✅ Time set: {soat:02d}:{minut:02d}\n\nType /getweather for the forecast.",

        "sana_kiriting": "📅 Enter a date (e.g. 2026-05-20):",
        "sana_saqlandi": "✅ Date saved: {sana}\nType /getweather to get the forecast.",
        "sana_xato": "❌ Wrong format! Please use YYYY-MM-DD.\nExample: 2026-05-20",

        "ob_havo_sarlavha": "🌤 WEATHER",
        "yomgir_yoq": "☀️ No precipitation",
        "yomgir": "🌧️ Rain",
        "qor": "❄️ Snow",
        "dol": "🌨️ Hail",
    },
}

TIL_NOMLARI = {
    "uz": "O'zbek 🇺🇿",
    "ru": "Русский 🇷🇺",
    "en": "English 🇬🇧",
}


def t(kalit: str, til: str = "uz", **kwargs) -> str:
    matn = TILLAR.get(til, TILLAR["uz"]).get(kalit, TILLAR["uz"].get(kalit, kalit))
    if kwargs:
        try:
            return matn.format(**kwargs)
        except (KeyError, ValueError):
            return matn
    return matn


def foydalanuvchi_tili(context) -> str:
    return context.user_data.get("til")
