from telethon.sync import TelegramClient, events
api_id , api_hash = [1833830630,'AAG4tGCXt0xMFxHk8qDwnq0lPoFE3EeCz5g']

with TelegramClient('tassist', api_id, api_hash) as client:
   client.send_message('me', 'Hello, myself!')
   print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*Hello'))
   async def handler(event):
      await event.reply('Hey!')

   client.run_until_disconnected()