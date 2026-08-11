import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault

import config
from db import init_db, close_db
from handlers import start, replies

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

    # Создаем сессию с явным указанием локального HTTP-прокси Xray
    # session = AiohttpSession(proxy="socks5://127.0.0.1:10808")
    session = AiohttpSession(proxy=config.PROXY_URL) if getattr(config, "PROXY_URL", None) else None

    bot = Bot(
        token=config.BOT_TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_routers(
        start.router,
        replies.router,
    )

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())
