# Standard libraries
import asyncio

# Aiogram stuff
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.types import BotCommand

# Handlers
import handlers

# Local
from basic import log


async def main():
    # Log
    log("|| Bot started ||")

    voBot = Bot(token="")
    voDB = MongoStorage(host='localhost', port='27017', db_name='LaOne')
    voDp = Dispatcher(voBot, storage=voDB)

    # Registering Handler
    handlers.regCommands(voDp)
    handlers.regMenu(voDp)

    # Listing commands to bot command menu
    await voBot.set_my_commands([
        BotCommand(command='/start', description='Restart Bot'),
    ])
    await voDp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
