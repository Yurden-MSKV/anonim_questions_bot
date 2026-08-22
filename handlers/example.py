import logging

from aiogram import Router, Bot, F
from aiogram.exceptions import TelegramAPIError
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyParameters, CallbackQuery, InputMediaPhoto

from keyboards.actions import ActionCallback, get_blacklist_keyboard
from models import AnonimMessage, User
from handlers.start import now_msk
from states.action_state import ActionForm

router = Router()


@router.message(F.reply_to_message)
async def process_reply(message: Message, bot: Bot):
    replied_msg_id = message.reply_to_message.message_id
    sender = await User.get(telegram_id=message.from_user.id)
    sender_id = str(sender.telegram_id)

    anon_msg = await AnonimMessage.get_or_none(
        data__contains={sender_id: replied_msg_id}
    ).prefetch_related('sender', 'recipient', 'source')

    if not anon_msg:
        print('Сообщение не найдено, баклан')
        return

    # print(f"{anon_msg.sender.telegram_id}: {anon_msg.msg_id_in_sender_chat}")

    if message.text == '/add':
        source = anon_msg.source
        sender_id = anon_msg.sender.telegram_id
        group = source.data['user_group']
        if sender_id in group:
            await message.answer("Пользователь уже состоит в группе.")
            return
        else:
            group.append(sender_id)
            await source.save(update_fields=['data'])
            await message.answer(
                "✅ Пользователь добавлен в группу.\n\nТеперь он тоже будет получать сообщения, приходящие по этой ссылке.")
            await bot.send_message(
                chat_id=sender_id,
                text=(
                    f"✅ Тебя подключили к ссылке <b>[{source.link_word}]</b>!\n\n"
                    f"Теперь ты будешь получать сообщения из этого источника и сможешь на них отвечать."
                )
            )
            return

    source = anon_msg.source
    new_recipients = list(source.data.get('user_group', []))
    link_users = list(source.data.get('user_group', []))

    if sender_id in new_recipients:
        new_recipients.remove(sender_id)
    if anon_msg.sender.telegram_id not in new_recipients:
        new_recipients.append(anon_msg.sender.telegram_id)

    # print(f"new_recipients: {new_recipients}")
    # print(f"anon_msg.sender.telegram_id: {anon_msg.sender.telegram_id}")

    recipient_dict = anon_msg.data.copy()
    if str(anon_msg.sender.telegram_id) not in recipient_dict:
        recipient_dict[str(anon_msg.sender.telegram_id)] = anon_msg.msg_id_in_sender_chat
    recipient_dict = {str(key): value for key, value in recipient_dict.items()}
    recipient_dict.pop(sender_id)
    # print(f"recipient_dict: {recipient_dict}")

    msg_dict = {}

    for recipient_id in recipient_dict:
        try:
            msg_in_recipient_chat = recipient_dict[recipient_id]
            # print(f"{recipient_id}: {msg_in_recipient_chat}")
            if (int(sender_id) in link_users and int(recipient_id) not in link_users) or (int(sender_id) not in link_users and int(recipient_id) in link_users):
                sent_message = await bot.send_message(
                    chat_id=int(recipient_id),
                    text=(
                        f"💬 <b>Тебе ответили</b>\n\n"
                        f"<blockquote>{message.text}</blockquote>\n\n"
                        f"Свайпни для ответа ↩️"
                    ),
                    reply_parameters=ReplyParameters(
                        message_id=msg_in_recipient_chat,
                        allow_sending_without_reply=True
                    )
                )
                msg_dict[recipient_id] = sent_message.message_id
            elif int(sender_id) in link_users and int(recipient_id) in link_users:
                another_message = await bot.send_message(
                    chat_id=int(recipient_id),
                    text=(
                        f"💬 <b>Ответ получателя из группы</b>\n\n"
                        f"<blockquote>{message.text}</blockquote>\n\n"
                        f"Свайпни для ответа ↩️"
                    ),
                    reply_parameters=ReplyParameters(
                        message_id=msg_in_recipient_chat,
                        allow_sending_without_reply=True
                    )
                )
                msg_dict[recipient_id] = another_message.message_id
            else:
                print('Проверка не работает')
                await message.answer('😢 Что-то пошло не так, сообщение не доставилось.')

        except TelegramAPIError as e:
            logging.error(f"Ошибка отправки Telegram API для {recipient_id}: {e}")
            print("Что-то пошло не так")
            await message.answer(
                f"😢 Сообщение НЕ доставилось. Получатель заблокировал бота или удалил чат."
            )
            return

    await AnonimMessage.create(
        sender=sender,
        recipients=new_recipients,
        # recipient=anon_msg.sender,
        source=anon_msg.source,
        text=message.text,
        created_at=now_msk(),
        data=msg_dict,
        # msg_id_in_recipient_chat=sent_message.message_id,
        msg_id_in_sender_chat=message.message_id
    )

    await message.answer(
        f"✅ <b>Твоё сообщение отправлено!</b>"
    )
