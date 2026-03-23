import asyncio
import json

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.Func.main_menu import main_menu
from src.Func.settings import settings
from src.Func.alarms import alarm
from src.Func.view import view

CONFIG: dict
with open('imp/config.json', 'r') as f:
    CONFIG = json.load(f)

async def main():
    global CONFIG
    bot = Bot(token=CONFIG['bot_token'], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(main_menu, settings, alarm, view)

    print('bot start')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
