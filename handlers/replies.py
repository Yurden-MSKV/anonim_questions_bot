from aiogram import Router, Bot, F
from aiogram.types import Message
from models import AnonimMessage
from handlers.start import now_msk

router = Router()

@router.message(F.reply_to_message)
async def process_reply(message: Message, bot: Bot):
    replied_msg_id = message.reply_to_message.message_id

    anon_msg = await AnonimMessage.get_or_none(
        msg_id_in_recipient_chat=replied_msg_id,
        recipient__telegram_id=message.from_user.id
    ).prefetch_related('sender', 'recipient', 'source')

    if not anon_msg:
        return

    sent_message = await bot.send_message(
        chat_id=anon_msg.sender.telegram_id,
        text=(
            f"💬 <b>Тебе ответили!</b>\n\n"
            f"<blockquote>{message.text}</blockquote>"
        )
    )

    await AnonimMessage.create(
        sender=anon_msg.recipient,
        recipient=anon_msg.sender,
        source=anon_msg.source,
        text=message.text,
        created_at=now_msk(),
        msg_id_in_recipient_chat=sent_message.message_id
    )

    await message.answer(
        f"✅ <b>Твоё сообщение отправлено!</b>"
    )