from Music.config import API_HASH, API_ID, BOT_TOKEN, STRING
from pyrogram import Client

app = Client(
    "Music",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

userbot = Client(STRING, API_ID, API_HASH)
