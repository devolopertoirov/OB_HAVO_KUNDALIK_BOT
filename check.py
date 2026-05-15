from config import kanallar

async def check_member(update, context):
    user_id = update.effective_user.id
    for kanal in kanallar:
        member = await context.bot.get_chat_member(chat_id=kanal, user_id=user_id)
        if member.status in ["left", "kicked"]:
            return False
    return True