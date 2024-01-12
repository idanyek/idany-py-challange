import asyncio, logging, os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# loading .env file
load_dotenv()

# getting token from env file
bot = Bot( token=os.getenv( "BOT_TOKEN" ) )
dp = Dispatcher()


@dp.message( CommandStart() )
async def handle_start(message: types.Message):
    await message.answer( (f"Hello, {message.from_user.full_name}.\n"
                           f"Let's begin!") )


@dp.message()
async def replay_as_echo(message: types.Message):
    try:
        await message.send_copy( chat_id=message.chat.id )  # 432654152
    except TypeError:
        await message.reply( text="sorry i get an error, please try again." )


async def main():
    logging.basicConfig( level=logging.DEBUG )
    await dp.start_polling( bot )


if __name__ == '__main__':
    asyncio.run( main() )
