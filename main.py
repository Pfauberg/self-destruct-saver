import os
import configparser
from pyrogram import Client, filters
from pyrogram.types import Message

config = configparser.ConfigParser()
config.read("config.ini")

api_id = int(config["telegram"]["api_id"])
api_hash = config["telegram"]["api_hash"]

bot = Client('self_destruct_saver', api_id=api_id, api_hash=api_hash)

@bot.on_message(filters.private & (filters.photo | filters.video | filters.video_note | filters.voice))
async def save_media(client: Client, message: Message):
    file_path = await message.download()
    caption = message.caption if message.caption else ""

    if message.photo and message.photo.ttl_seconds:
        await client.send_photo("me", file_path, caption=caption)
    elif message.video and message.video.ttl_seconds:
        await client.send_video("me", file_path, caption=caption)
    elif message.video_note and message.video_note.ttl_seconds:
        await client.send_video("me", file_path)
    elif message.voice and message.voice.ttl_seconds:
        await client.send_voice("me", file_path)

    os.remove(file_path)


bot.run()
