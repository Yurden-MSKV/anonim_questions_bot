import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError, TelegramRetryAfter

from models import User


async def check_all_users_status(bot: Bot):
    active_users = await User.all()
    print(f"Проверка запущенa. Пользователей в базе: {len(active_users)}")

    blocked_count = 0

    for user in active_users:
        try:
            await bot.send_chat_action(chat_id=user.telegram_id, action="typing")
        except TelegramForbiddenError:
            user.is_active = False
            await user.save()
            blocked_count += 1
            print(f"Пользователь {user.telegram_id} заблокировал бота.")
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
            await bot.send_chat_action(chat_id=user.telegram_id, action="typing")
        except Exception as e:
            print(f"Ошибка у ID {user.telegram_id}: {e}")

        await asyncio.sleep(0.05)

    print(f"Готово! Из {len(active_users)} пользователей заблокировали бота: {blocked_count}")