import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault

import config
from db import init_db, close_db
from handlers import start

logging.basicConfig(level=logging.INFO)

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command="start",
            description="Главное меню"
        )
    ]
    await bot.set_my_commands(main_menu_commands, scope=BotCommandScopeDefault())


async def main():
    await init_db()
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_routers(
        start.router,
        # apply.router,
    )

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())