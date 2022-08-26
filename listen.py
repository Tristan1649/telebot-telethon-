from telethon.sync import TelegramClient, events
from app_config import API_ID, API_HASH

with TelegramClient('telegram_session', API_ID, API_HASH) as client:
   client.send_message('me', 'Hello, myself!')
   print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*Hello'))
   async def handler(event):
      await event.reply('Good!')

#для вывода в консоль
   @client.on(events.NewMessage(incoming=True))
   async def handler(event):
      print(event.message.message)

#для удаления   
   @client.on(events.MessageDeleted)
   async def handler(event):
      print(event.deleted_id)

#для исправления
   @client.on(events.MessageEdited)
   async def handler(event):
      print(event.message.message)
      await event.reply('This message was edited!')

   client.run_until_disconnected()

