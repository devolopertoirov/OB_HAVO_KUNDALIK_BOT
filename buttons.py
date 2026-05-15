from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config
from languages import t, foydalanuvchi_tili, TIL_NOMLARI

async def buttons(update, context):
    if not update.message or not update.message.text:
        return

    message = update.message.text
    til = foydalanuvchi_tili(context) or "uz"

    sozlamalar_text       = t("sozlamalar_tugmasi", til)
    getweather_text       = t("getweather_tugmasi", til)
    vaqt_text             = t("vaqt_tugmasi", til)
    sana_text             = t("sana_tugmasi", til)
    til_text              = t("til_tugmasi", til)
    orqaga_text           = t("orqaga_tugmasi", til)
    joylashuv_ozg_text    = t("joylashuv_ozgartirish", til)

    if message == getweather_text:
        from main import getweather
        await getweather(update, context)
        return

    if message == sozlamalar_text:
        tugmalar = ReplyKeyboardMarkup([
            [KeyboardButton(vaqt_text),          KeyboardButton(sana_text)],
            [KeyboardButton(joylashuv_ozg_text), KeyboardButton(til_text)],
            [KeyboardButton(orqaga_text)],
        ], one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text(t("bolim_tanlang", til), reply_markup=tugmalar)

    elif message == vaqt_text:
        await update.message.reply_text(t("soat_sozlang", til), reply_markup=_soat_markup(til))

    elif message == sana_text:
        context.user_data["awaiting_date"] = True
        await update.message.reply_text(t("sana_kiriting", til))

    elif message == til_text:
        tugma_til = InlineKeyboardMarkup([[
            InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="til_uz"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="til_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="til_en"),
        ]])
        await update.message.reply_text(t("til_tanlang", til), reply_markup=tugma_til)

    elif message == joylashuv_ozg_text:
        tugmalar = ReplyKeyboardMarkup([
            [KeyboardButton(t("joylashuv_tugmasi", til), request_location=True)]
        ], resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(t("start_xush_kelibsiz", til, admin=""), reply_markup=tugmalar)

    elif message == orqaga_text:
        from main import start
        await start(update, context)

    elif context.user_data.get("awaiting_date"):
        context.user_data["awaiting_date"] = False
        sana = message.strip()
        import re
        if re.match(r"^\d{4}-\d{2}-\d{2}$", sana):
            context.user_data["tanlangan_sana"] = sana
            await update.message.reply_text(t("sana_saqlandi", til, sana=sana))
        else:
            context.user_data["awaiting_date"] = True
            await update.message.reply_text(t("sana_xato", til))

async def callback_handler(update, context):
    query = update.callback_query
    await query.answer()
    data = query.data
    til  = foydalanuvchi_tili(context) or "uz"
    if data.startswith("start_til_"):
        yangi_til = data.split("_")[2]
        context.user_data["til"] = yangi_til
        til_nomi = TIL_NOMLARI[yangi_til]
        await query.edit_message_text(t("til_saqlandi", yangi_til, til_nomi=til_nomi))

        from config import admin_username
        tugmalar = ReplyKeyboardMarkup([
            [KeyboardButton(t("joylashuv_tugmasi", yangi_til), request_location=True)]
        ], resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text(
            t("start_xush_kelibsiz", yangi_til, admin=admin_username),
            reply_markup=tugmalar
        )
        return

    if data in ("til_uz", "til_ru", "til_en"):
        yangi_til = data.split("_")[1]
        til_nomi  = TIL_NOMLARI[yangi_til]
        if context.user_data.get("til") == yangi_til:
            await query.answer(t("til_allaqachon", yangi_til, til_nomi=til_nomi), show_alert=False)
        else:
            context.user_data["til"] = yangi_til
            await query.edit_message_text(t("til_saqlandi", yangi_til, til_nomi=til_nomi))
        return

    if data == "soat_-_1":
        if config.soat > 0:
            config.soat -= 1
            await query.edit_message_reply_markup(reply_markup=_soat_markup(til))
        else:
            await query.answer(t("soat_min_xato", til), show_alert=False)

    elif data == "soat_+_1":
        if config.soat < 23:
            config.soat += 1
            await query.edit_message_reply_markup(reply_markup=_soat_markup(til))
        else:
            await query.answer(t("soat_max_xato", til), show_alert=False)

    elif data == "soat_boldi":
        await query.edit_message_text(
            t("soat_saqlandi", til, soat=config.soat),
            reply_markup=_minut_markup(til)
        )

    elif data == "minut_-_1":
        if config.minut > 0:
            config.minut -= 1
            await query.edit_message_reply_markup(reply_markup=_minut_markup(til))
        else:
            await query.answer(t("minut_min_xato", til), show_alert=False)

    elif data == "minut_+_1":
        if config.minut < 59:
            config.minut += 1
            await query.edit_message_reply_markup(reply_markup=_minut_markup(til))
        else:
            await query.answer(t("minut_max_xato", til), show_alert=False)

    elif data == "minut_-_10":
        eski = config.minut
        config.minut = max(0, config.minut - 10)
        if config.minut != eski:
            await query.edit_message_reply_markup(reply_markup=_minut_markup(til))
        else:
            await query.answer(t("minut_min_xato", til), show_alert=False)

    elif data == "minut_+_10":
        eski = config.minut
        config.minut = min(59, config.minut + 10)
        if config.minut != eski:
            await query.edit_message_reply_markup(reply_markup=_minut_markup(til))
        else:
            await query.answer(t("minut_max_xato", til), show_alert=False)

    elif data == "minut_boldi":
        await query.edit_message_text(
            t("vaqt_saqlandi", til, soat=config.soat, minut=config.minut)
        )

    elif data == "noop":
        pass

def _soat_markup(til: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➖", callback_data="soat_-_1"),
            InlineKeyboardButton(f"🕐 {config.soat:02d}", callback_data="noop"),
            InlineKeyboardButton("➕", callback_data="soat_+_1"),
        ],
        [InlineKeyboardButton(t("soat_saqlash", til), callback_data="soat_boldi")],
    ])


def _minut_markup(til: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➖",    callback_data="minut_-_1"),
            InlineKeyboardButton(f"⏱ {config.minut:02d}", callback_data="noop"),
            InlineKeyboardButton("➕",    callback_data="minut_+_1"),
        ],
        [
            InlineKeyboardButton("⏪ -10", callback_data="minut_-_10"),
            InlineKeyboardButton("⏩ +10", callback_data="minut_+_10"),
        ],
        [InlineKeyboardButton(t("minut_saqlash", til), callback_data="minut_boldi")],
    ])
