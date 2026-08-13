from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyParameters, CallbackQuery

from keyboards.actions import ActionCallback
from models import AnonimMessage, User
from handlers.start import now_msk
from states.action_state import ActionForm

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

    try:
        sent_message = await bot.send_message(
            chat_id=anon_msg.sender.telegram_id,
            text=(
                f"💬 <b>Тебе ответили!</b>\n\n"
                f"<blockquote>{message.text}</blockquote>"
            ),
            reply_parameters=ReplyParameters(
                message_id=anon_msg.msg_id_in_sender_chat,
                allow_sending_without_reply=True
            )
        )

        await AnonimMessage.create(
            sender=anon_msg.recipient,
            recipient=anon_msg.sender,
            source=anon_msg.source,
            text=message.text,
            created_at=now_msk(),
            msg_id_in_recipient_chat=sent_message.message_id,
            msg_id_in_sender_chat=message.message_id
        )

        await message.answer(
            f"✅ <b>Твоё сообщение отправлено!</b>"
        )

    except:
        print("Что-то пошло не так")
        await message.answer(
            f"😢 Сообщение НЕ доставилось. Получатель заблокировал бота или удалил чат."
        )

@router.callback_query(ActionCallback.filter(F.action_code == "block"))
async def block_action(
        callback: CallbackQuery,
        callback_data: ActionCallback
):
    anon_msg = await AnonimMessage.get_or_none(msg_id_in_recipient_chat=callback.message.message_id).prefetch_related('sender', 'recipient')
    if not anon_msg:
        return
    recipient = anon_msg.recipient
    sender = anon_msg.sender
    if sender:
        recipient.data["blacklist"].append(sender.telegram_id)
        await recipient.save()
    await callback.answer("Пользователь заблокирован", show_alert=True)
