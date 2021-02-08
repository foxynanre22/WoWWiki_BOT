import asyncio
import io
import logging

from aiogram import Bot, Dispatcher, executor, types
from PIL import Image
from project.WoWWiki_BOT.Bot.parsing import parcing
from project.WoWWiki_BOT.Data.DBContext import DBContext

import config

"""bot initialization"""
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

"""logs config"""
logging.basicConfig(level=logging.INFO)

"""connecting to the database"""
db = DBContext(
    "E:\\WSIZ\\wsiz 3 rok\\Python (Smok)\\Project\\poligon\\"
    "test_bot\\venv\\project\\WoWWiki_BOT\\Data\\database.db"
)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    """
    Message after user started bot.
    :param message:
    :return:
    """
    await message.answer(
        "Hello, {0}! I'm WoW Wiki Bot. Find what do "
        "you want from World of Warcraft fandom!"
        "Just type a name of hero/race/stuff or "
        "something else and I'll try to find it!".format(
            message.from_user.first_name
        )
    )


@dp.message_handler()
async def find(message: types.Message):
    """
    Main functionality of bot.
    Using connection to the database search for the article
    named like user input. If article caption will be >870
    symbols than image of the article will be send separate
    from the text.
    :param message:
    :return:
    """
    article = db.find_article(message.text.lower())

    if article:
        if article[0][3] == "NONE_IMAGE_HERE":

            buffer = io.BytesIO()
            not_found = Image.open("not-found.jpg")
            not_found.save(buffer, format="JPEG", quality=75)
            not_found = buffer.getbuffer()

            if len(article[0][4]) > 870:
                await bot.send_photo(message.from_user.id, not_found)
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=message.text.upper()
                    + "\n\n"
                    + article[0][4]
                    + "\n\nHere is a link to full article:\n"
                    + article[0][2],
                )
            else:
                await bot.send_photo(
                    message.from_user.id,
                    not_found,
                    caption=message.text.upper()
                    + "\n\n"
                    + article[0][4]
                    + "\n\nHere is a link to full article:\n"
                    + article[0][2],
                )
        else:
            if len(article[0][4]) > 870:
                await bot.send_photo(message.from_user.id, article[0][3])
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=message.text.upper()
                    + "\n\n"
                    + article[0][4]
                    + "\n\nHere is a link to full article:\n"
                    + article[0][2],
                )
            else:
                await bot.send_photo(
                    message.from_user.id,
                    article[0][3],
                    caption=message.text.upper()
                    + "\n\n"
                    + article[0][4]
                    + "\n\nHere is a link to full article:\n"
                    + article[0][2],
                )
    else:
        await message.answer(
            "Sorry, I cannot find information about "
            "this :(\nCheck if you typed correctly."
        )


async def parse(interval):
    """
    Function is a task for asyncio Even Loop.
    It starts parsing and after that waits for as many
    seconds as specified in the interval.
    :param interval:
    :return:
    """
    while True:
        await parcing(db)
        await asyncio.sleep(interval)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(parse(18000))
    executor.start_polling(dp, skip_updates=True, loop=loop)
