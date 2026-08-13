from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyParameters, CallbackQuery

from keyboards.actions import ActionCallback, get_blacklist_keyboard
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
        # callback_data: ActionCallback
):
    anon_msg = await AnonimMessage.get_or_none(msg_id_in_recipient_chat=callback.message.message_id).prefetch_related('sender', 'recipient')
    if not anon_msg:
        return
    recipient = anon_msg.recipient
    sender = anon_msg.sender
    if sender:
        if not recipient.data:
            recipient.data = {}
        blacklist = recipient.data.setdefault('blacklist', [])
        sender_id = sender.telegram_id
        if sender_id not in blacklist:
            blacklist.append(sender_id)
            await recipient.save(update_fields=['data'])
            await callback.message.edit_reply_markup(
                reply_markup=get_blacklist_keyboard(is_blocked=True)
            )
            await callback.answer("Отправитель заблокирован!")
        else:
            await callback.answer("Отправитель уже в черном списке.")


@router.callback_query(ActionCallback.filter(F.action_code == "unblock"))
async def unblock_action(callback: CallbackQuery):
    anon_msg = await AnonimMessage.get_or_none(
        msg_id_in_recipient_chat=callback.message.message_id
    ).prefetch_related('sender', 'recipient')

    if not anon_msg:
        await callback.answer("Сообщение не найдено", show_alert=True)
        return

    recipient = anon_msg.recipient
    sender = anon_msg.sender

    if sender:
        if not recipient.data:
            recipient.data = {}

        blacklist = recipient.data.get('blacklist', [])
        sender_id = sender.telegram_id

        if sender_id in blacklist:
            blacklist.remove(sender_id)
            await recipient.save(update_fields=['data'])

            await callback.message.edit_reply_markup(
                reply_markup=get_blacklist_keyboard(is_blocked=False)
            )
            await callback.answer("Отправитель разблокирован!")
        else:
            await callback.answer("Отправитель не был заблокирован.")