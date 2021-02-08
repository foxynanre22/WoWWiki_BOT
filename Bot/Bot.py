import config
import logging
from PIL import Image
import io
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from project.WoWWiki_BOT.Data.DBContext import DBContext
from project.WoWWiki_BOT.Bot.parsing import parcing

# bot initialization
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

#logs config
logging.basicConfig(level=logging.INFO)

# connecting to tour database
db = DBContext('E:\\University\\python\\test_bot\\venv\\project\\WoWWiki_BOT\\Data\\database.db')

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("Hello, {0}! I'm WoW Wiki Bot. Find what do you want from World of Warcraft fandom!".format(message.from_user.first_name))

@dp.message_handler()
async def find(message: types.Message):
    article = db.find_article(message.text.lower())

    if(article):
        if(article[0][3] == 'NONE_IMAGE_HERE'):

            buffer = io.BytesIO()
            not_found = Image.open("not-found.jpg")
            not_found.save(buffer, format='JPEG', quality=75)
            not_found = buffer.getbuffer()

            if(len(article[0][4]) > 870):
                await bot.send_photo(message.from_user.id, not_found)
                await bot.send_message(chat_id=message.from_user.id,text=message.text.upper() + "\n\n" + article[0][4] +
                                       "\n\nHere is a link to full article:\n" + article[0][2])
            else:
                await bot.send_photo(message.from_user.id, not_found,
                                     caption=message.text.upper() + "\n\n" + article[0][4] +
                                             "\n\nHere is a link to full article:\n" + article[0][2])
        else:
            if (len(article[0][4]) > 870):
                await bot.send_photo(message.from_user.id, article[0][3])
                await bot.send_message(chat_id=message.from_user.id,text=message.text.upper() + "\n\n" + article[0][4] +
                                       "\n\nHere is a link to full article:\n" + article[0][2])
            else:
                await bot.send_photo(message.from_user.id, article[0][3],
                                    caption=message.text.upper() +"\n\n" + article[0][4] +
                                            "\n\nHere is a link to full article:\n" + article[0][2])
    else:
        await message.answer("Sorry, I cannot find information about this :(\nCheck if you typed correctly.")

async def parse(interval):
    while True:
        await parcing(db)
        await asyncio.sleep(interval)

if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.create_task(parse(18000))
    executor.start_polling(dp, skip_updates=True) #loop=loop