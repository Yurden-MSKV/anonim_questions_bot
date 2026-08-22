import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault

from add_groups import add_groups_in_sources
from check import check_all_users_status
from middlewares.album import AlbumMiddleware

import config
from db import init_db, close_db
from handlers import start, replies, source_list, block, actions

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
    session = AiohttpSession(proxy=config.PROXY_URL) if getattr(config, "PROXY_URL", None) else None

    bot = Bot(
        token=config.BOT_TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.message.outer_middleware(AlbumMiddleware())

    await set_main_menu(bot)

    dp.include_routers(
        start.router,
        replies.router,
        source_list.router,
        block.router,
        actions.router
    )

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # Проверка активности пользователей
        # await check_all_users_status(bot)
        # Проверка групп у источников
        await add_groups_in_sources(bot)
        await dp.start_polling(bot)
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())
