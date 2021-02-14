import asyncio
import io
import logging

from aiogram import Bot, Dispatcher, executor, types
from PIL import Image
from project.WoWWiki_BOT.Bot.parsing import parcing
from project.WoWWiki_BOT.Data.DBContext import DBContext
from project.WoWWiki_BOT.Parser.ArticleModel import ArticleModel

import config

"""bot initialization"""
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

"""logs config"""
logging.basicConfig(level=logging.INFO)

"""connecting to the database"""
db = DBContext(
    #here is a sting that contain path to your database
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
        "something else and I'll "
        "try to find it!".format(message.from_user.first_name)
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
        if article.photo_link == "NONE_IMAGE_HERE":

            buffer = io.BytesIO()
            not_found = Image.open("not-found.jpg")
            not_found.save(buffer, format="JPEG", quality=75)
            not_found = buffer.getbuffer()

            await send_article(message, article, not_found)
        else:
            await send_article(message, article, article.photo_link)
    else:
        await message.answer(
            "Sorry, I cannot find information about "
            "this :(\nCheck if you typed correctly."
        )


async def send_article(message: types.Message,
                       article: ArticleModel,
                       article_photo):
    """function to send article by the bot"""
    if len(article.text) > 870:
        await bot.send_photo(message.from_user.id, article_photo)
        await bot.send_message(
            chat_id=message.from_user.id,
            text=message.text.upper()
            + "\n\n"
            + article.text
            + "\n\nHere is a link to full article:\n"
            + article.link,
        )
    else:
        await bot.send_photo(
            message.from_user.id,
            article_photo,
            caption=message.text.upper()
            + "\n\n"
            + article.text
            + "\n\nHere is a link to full article:\n"
            + article.link,
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
