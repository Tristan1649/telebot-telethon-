import time
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient, events
from app_config import API_ID, API_HASH
from telethon.errors.rpcerrorlist import FloodWaitError


channels = ['TelethonChat','ru_python_begginers','pydjango']

with TelegramClient('telegram_session', API_ID, API_HASH) as client:
    for channel in channels:
        try:
            client(JoinChannelRequest(channel))
        except FloodWaitError as fwe:
            print(fwe)
            time.sleep(fwe.seconds)
        except Exception as e:
            print(e)
            time.sleep(20)