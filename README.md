# WOW Fandom Wiki BOT

<a href="https://t.me/wowWikiTestBot"> <div align="center">
<img src="https://i.pinimg.com/564x/18/f2/c2/18f2c237688c6a4395e0f6a702743a7c.jpg" width="100" height="100" />

<b> WOW Fandom Wiki BOT</b> 
</div></a>

This is a telegram bot that helps users to access information about World of Warcraft in a fast way from https://wowwiki-archive.fandom.com
<a href="https://wowwiki-archive.fandom.com"><b> WoW Wiki Fandom</b></a>

Now bot is offline. 

## Features:
* Searching the information from the WoW Wiki fandom.
* Bot display following information:
    * Image of the article
    * Short description
    * A link to the full article

## Setup
1. Clone the repository.
2. Install required Python dependencies: 

    `pip install -r requirements.txt`
3. Create a telegram API token with bot father. Following the [article](https://medium.com/shibinco/create-a-telegram-bot-using-botfather-and-get-the-api-token-900ba00e0f39) to check how generate your own token.
4. Add token to the *config.py* file.

     `API_TOKEN = 'your bot api token here'`
5. Initialize database context to work with database which locate in Data folder in *Bot.py* file: 

    `db = DBContext('path to the database in Data folder on your computer')`
6. Optional: In *parsing.py* file you can create|delete|add parsers, run them and save parsed information in the database. Check *Parser.py* docstrings for more information. 
7. Run python *Bot.py* file

## Comments
1. There are all logs and parsing processes in *parsing.log* file.
2. Now database is filled with over 6000 records using 47 parcer links. You can increase records adding new parcers that is based on another parcer links. Check *Parser.py* docstrings for more information about parcer links format.

## Bot commands
```
/start
To start the WOW Fandom Wiki BOT.
```

## Sources:

Bot Data Source - https://wowwiki-archive.fandom.com/wiki/Portal:Main

Python Telegram Bot API Framework "Aiogram" - https://pypi.org/project/aiogram/

## Contributors:

- Danyil Martin- [@foxynanre22](https://github.com/foxynanre22)
- Illia Samorodov- [@w60089](https://github.com/w60089)
