from weather import get_weather
from config import bot_token, admin_username
from scheduler import start_scheduler, send_now
from check import check_member
from buttons import buttons, callback_handler
from languages import t, foydalanuvchi_tili, TIL_NOMLARI
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, filters
)

def asosiy_menyu_markup(til: str):
    return ReplyKeyboardMarkup([
        [KeyboardButton(t("getweather_tugmasi", til))],
        [KeyboardButton(t("sozlamalar_tugmasi", til))],
    ], resize_keyboard=True)


# ─── /start ───────────────────────────────────────────────────────────────────

async def start(update, context):
    if not await check_member(update, context):
        til = foydalanuvchi_tili(context) or "uz"
        await update.message.reply_text(t("obuna_kerak", til))
        return

    til = foydalanuvchi_tili(context)

    if not til:
        tugma_til = InlineKeyboardMarkup([[
            InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="start_til_uz"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="start_til_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="start_til_en"),
        ]])
        await update.message.reply_text(
            "🌍 Xush kelibsiz! / Добро пожаловать! / Welcome!\n\nTilni tanlang / Выберите язык / Select language:",
            reply_markup=tugma_til
        )
        return

    if not context.user_data.get("lat"):
        tugmalar = ReplyKeyboardMarkup([
            [KeyboardButton(t("joylashuv_tugmasi", til), request_location=True)]
        ], resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(
            t("start_xush_kelibsiz", til, admin=admin_username),
            reply_markup=tugmalar
        )
        return

    await update.message.reply_text(
        t("asosiy_menyu", til),
        reply_markup=asosiy_menyu_markup(til)
    )

async def location_handler(update, context):
    til = foydalanuvchi_tili(context) or "uz"
    context.user_data["lat"]  = update.message.location.latitude
    context.user_data["long"] = update.message.location.longitude

    await update.message.reply_text(
        t("joylashuv_qabul", til),
        reply_markup=asosiy_menyu_markup(til)
    )

async def getweather(update, context):
    til  = foydalanuvchi_tili(context) or "uz"
    lat  = context.user_data.get("lat")
    long = context.user_data.get("long")

    if not lat or not long:
        tugmalar = ReplyKeyboardMarkup([
            [KeyboardButton(t("joylashuv_tugmasi", til), request_location=True)]
        ], resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(t("joylashuv_yoq", til), reply_markup=tugmalar)
        return

    natija = await get_weather(lat=lat, long=long, til=til)
    await update.message.reply_text(natija)

def main():
    app = Application.builder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getweather", getweather))
    app.add_handler(CommandHandler("sendnow", send_now))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))
    app.add_handler(CallbackQueryHandler(callback_handler))

    start_scheduler(app.bot)
    app.run_polling()


if __name__ == "__main__":
    main()
