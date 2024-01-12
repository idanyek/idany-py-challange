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
    await message.answer( (f"Hi,\n"
                           f"{message.from_user.full_name}.\n"
                           f"Welcome to my bot.\n"
                           f"in this bot i will say everything you say. lets start...:)") )


@dp.message()
async def return_any_message_back(message: types.Message):
    try:
        await message.send_copy( chat_id=message.chat.id )
    except TypeError:
        await message.reply( text="oops i get an error, please try again." )


async def main():
    logging.basicConfig( level=logging.DEBUG )
    await dp.start_polling( bot )


if __name__ == '__main__':
    asyncio.run( main() )
