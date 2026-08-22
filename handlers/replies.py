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


@router.message(F.reply_to_message, F.media_group_id)
async def process_reply(message: Message, bot: Bot, album: list[Message]):
    replied_msg_id = message.reply_to_message.message_id
    sender = await User.get(telegram_id=message.from_user.id)
    sender_id = str(sender.telegram_id)

    anon_msg = await AnonimMessage.get_or_none(
        data__contains={sender_id: replied_msg_id}
    ).prefetch_related('sender', 'source')

    if not anon_msg:
        return

    # source = anon_msg.source
    # new_recipients, link_users = source.data['user_group']
    # if message.from_user.id in new_recipients:
    #     new_recipients.remove(message.from_user.id)
    # new_recipients.append(anon_msg.sender.telegram_id)

    source = anon_msg.source
    new_recipients = list(source.data.get('user_group', []))
    link_users = list(source.data.get('user_group', []))

    if sender_id in new_recipients:
        new_recipients.remove(sender_id)
    if anon_msg.sender.telegram_id not in new_recipients:
        new_recipients.append(anon_msg.sender.telegram_id)

    recipient_dict = anon_msg.data.copy()
    if str(anon_msg.sender.telegram_id) not in recipient_dict:
        recipient_dict[str(anon_msg.sender.telegram_id)] = anon_msg.msg_id_in_sender_chat
    recipient_dict = {str(key): value for key, value in recipient_dict.items()}
    recipient_dict.pop(sender_id)

    print(f"recipient_dict: {recipient_dict}")

    text = album[0].caption or '<i>Без текста.</i>'

    msg_dict = {}

    for recipient_id in recipient_dict:
        try:
            msg_in_recipient_chat = recipient_dict[recipient_id]
            full_caption = ''
            if (int(sender_id) in link_users and int(recipient_id) not in link_users) or (int(sender_id) not in link_users and int(recipient_id) in link_users):
                full_caption = f'💬 <b>Тебе ответили</b>\n\n<blockquote>{text}</blockquote>\n\nСвайпни для ответа ↩️'
            elif int(sender_id) in link_users and int(recipient_id) in link_users:
                full_caption = f'💬 <b>Ответ получателя из группы</b>\n\n<blockquote>{text}</blockquote>\n\nСвайпни для ответа ↩️'
            else:
                print("Что-то сломалось")

            media_group = []
            for index, msg in enumerate(album):
                photo_id = msg.photo[-1].file_id
                if index == 0:
                    media_group.append(InputMediaPhoto(media=photo_id, caption=full_caption))
                else:
                    media_group.append(InputMediaPhoto(media=photo_id))

            sent_message = another_message = await bot.send_media_group(
                chat_id=int(recipient_id),
                media=media_group,
                reply_parameters=ReplyParameters(
                    message_id=msg_in_recipient_chat,
                    allow_sending_without_reply=True
                )
            )

            if (int(sender_id) in link_users and int(recipient_id) not in link_users) or (int(sender_id) not in link_users and int(recipient_id) in link_users):
                msg_dict[recipient_id] = sent_message[0].message_id
            else:
                msg_dict[recipient_id] = another_message[0].message_id

        except:
            print('Ошибка отправки, читай логи')
            await message.answer(
                f"😢 Сообщение НЕ доставилось. Получатель заблокировал бота или удалил чат."
            )
            return

    await AnonimMessage.create(
        sender=sender,
        recipients=new_recipients,
        # recipient=anon_msg.sender,
        source=anon_msg.source,
        # text=text,
        # created_at=now_msk(),
        data=msg_dict,
        # msg_id_in_recipient_chat=sent_message[0].message_id,
        msg_id_in_sender_chat=message.message_id
    )

    await message.answer(
        f"✅ <b>Твоё сообщение отправлено!</b>"
    )


@router.message(F.reply_to_message, F.photo)
async def process_reply(message: Message, bot: Bot):
    replied_msg_id = message.reply_to_message.message_id
    sender = await User.get(telegram_id=message.from_user.id)
    sender_id = str(sender.telegram_id)

    anon_msg = await AnonimMessage.get_or_none(
        data__contains={sender_id: replied_msg_id}
    ).prefetch_related('sender', 'source')

    if not anon_msg:
        print('Сообщение не найдено, баклан')
        return

    photo_id = message.photo[-1].file_id
    text = message.caption or '<i>Без текста.</i>'

    # source = anon_msg.source
    # new_recipients, link_users = source.data['user_group']
    # if message.from_user.id in new_recipients:
    #     new_recipients.remove(message.from_user.id)
    # new_recipients.append(anon_msg.sender.telegram_id)

    source = anon_msg.source
    new_recipients = list(source.data.get('user_group', []))
    link_users = list(source.data.get('user_group', []))

    if sender_id in new_recipients:
        new_recipients.remove(sender_id)
    if anon_msg.sender.telegram_id not in new_recipients:
        new_recipients.append(anon_msg.sender.telegram_id)

    recipient_dict = anon_msg.data.copy()
    if str(anon_msg.sender.telegram_id) not in recipient_dict:
        recipient_dict[str(anon_msg.sender.telegram_id)] = anon_msg.msg_id_in_sender_chat
    recipient_dict = {str(key): value for key, value in recipient_dict.items()}
    recipient_dict.pop(sender_id)
    # print(f"Вывод для отправки фото:\nrecipient_dict: {recipient_dict}")

    msg_dict = {}

    for recipient_id in recipient_dict:
        try:
            msg_in_recipient_chat = recipient_dict[recipient_id]
            full_caption = ''
            if (int(sender_id) in link_users and int(recipient_id) not in link_users) or (int(sender_id) not in link_users and int(recipient_id) in link_users):
                full_caption = f'💬 <b>Тебе ответили</b>\n\n<blockquote>{text}</blockquote>\n\nСвайпни для ответа ↩️'
            elif int(sender_id) in link_users and int(recipient_id) in link_users:
                full_caption = f'💬 <b>Ответ получателя из группы</b>\n\n<blockquote>{text}</blockquote>\n\nСвайпни для ответа ↩️'

            if (int(sender_id) in link_users and int(recipient_id) not in link_users) or (int(sender_id) not in link_users and int(recipient_id) in link_users):
                sent_message = await bot.send_photo(
                    chat_id=int(recipient_id),
                    photo=photo_id,
                    caption=full_caption,
                    reply_parameters=ReplyParameters(
                        message_id=msg_in_recipient_chat,
                        allow_sending_without_reply=True
                    )
                )
                msg_dict[recipient_id] = sent_message.message_id

            else:
                another_message = await bot.send_photo(
                    chat_id=int(recipient_id),
                    photo=photo_id,
                    caption=full_caption,
                    reply_parameters=ReplyParameters(
                        message_id=msg_in_recipient_chat,
                        allow_sending_without_reply=True
                    )
                )
                msg_dict[recipient_id] = another_message.message_id

        except:
            print("Что-то пошло не так")
            await message.answer(
                f"😢 Сообщение НЕ доставилось. Получатель заблокировал бота или удалил чат."
            )

    await AnonimMessage.create(
        sender=sender,
        recipients=new_recipients,
        # recipient=anon_msg.sender,
        source=anon_msg.source,
        # text=text,
        # created_at=now_msk(),
        data=msg_dict,
        # msg_id_in_recipient_chat=sent_message.message_id,
        msg_id_in_sender_chat=message.message_id
    )

    await message.answer(
        f"✅ <b>Твоё сообщение отправлено!</b>"
    )


@router.message(F.reply_to_message)
async def process_reply(message: Message, bot: Bot):
    replied_msg_id = message.reply_to_message.message_id
    sender = await User.get(telegram_id=message.from_user.id)
    sender_id = str(sender.telegram_id)

    anon_msg = await AnonimMessage.get_or_none(
        data__contains={sender_id: replied_msg_id}
    ).prefetch_related('sender', 'source')

    if not anon_msg:
        print('Сообщение не найдено, баклан')
        return

    print(f"{anon_msg.sender.telegram_id}: {anon_msg.msg_id_in_sender_chat}")

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
            await message.answer("✅ Пользователь добавлен в группу.\n\nТеперь он тоже будет получать сообщения, приходящие по этой ссылке.")
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
    print(link_users)

    if sender_id in new_recipients:
        new_recipients.remove(sender_id)
    if anon_msg.sender.telegram_id not in new_recipients:
        new_recipients.append(anon_msg.sender.telegram_id)

    # print(f"new_recipients: {new_recipients}")
    # print(f"anon_msg.sender.telegram_id: {anon_msg.sender.telegram_id}")

    recipient_dict = anon_msg.data.copy()
    if str(anon_msg.sender.telegram_id) not in recipient_dict:
        # print('Оригинального анонима ещё нет в списке, добавляю...')
        recipient_dict[str(anon_msg.sender.telegram_id)] = anon_msg.msg_id_in_sender_chat
    recipient_dict = {str(key): value for key, value in recipient_dict.items()}
    recipient_dict.pop(sender_id)
    print(f"recipient_dict: {recipient_dict}")

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
        # text=message.text,
        # created_at=now_msk(),
        data=msg_dict,
        # msg_id_in_recipient_chat=sent_message.message_id,
        msg_id_in_sender_chat=message.message_id
    )

    await message.answer(
        f"✅ <b>Твоё сообщение отправлено!</b>"
    )


@router.callback_query(ActionCallback.filter(F.action_code == "block"))
async def block_action(callback: CallbackQuery):
    anon_msg = await AnonimMessage.get_or_none(msg_id_in_recipient_chat=callback.message.message_id).prefetch_related('sender', 'source__user')
    if not anon_msg:
        print('Сообщение не найдено')
        await callback.answer()
        return
    recipient = anon_msg.source.user
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
    else:
        print('Пользователь не найден')
        await callback.answer(f"🚫 Пользователь не найден.")
        return

@router.callback_query(ActionCallback.filter(F.action_code == "unblock"))
async def unblock_action(callback: CallbackQuery):
    anon_msg = await AnonimMessage.get_or_none(
        msg_id_in_recipient_chat=callback.message.message_id
    ).prefetch_related('sender', 'source__user')

    if not anon_msg:
        await callback.answer("Сообщение не найдено", show_alert=True)
        return

    recipient = anon_msg.source.user
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