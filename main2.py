from quart import Quart,render_template,request
from telethon import TelegramClient,events
import os,asyncio,json



users = {}
api_id = 
api_hash =''
name = ''

client = TelegramClient(name, api_id, api_hash)

app = Quart(__name__)

users = {}
async def main():
    async with TelegramClient(name, api_id, api_hash) as client:
        
         @client.on(events.NewMessage)
         async def my_event_handler(event):
             print(event.raw_text)
             with open('data.json') as json_file:
                 data = json.load(json_file)
                 if 'userno' in event.raw_text:
                    await event.reply(str(len(data)))
                 elif 'userlist' in event.raw_text:
                    await event.reply(str(data))

         await client.run_until_disconnected()



@app.route('/request',methods = ['GET','POST'])
async def bill():
    if request.method == 'POST':
        response = await request.form
        users['students'] = []
        users['students'].append(response['link'])
        with open('data.json','w') as json_file:
            json.dump(users,json_file)

        return "entry made "+response['link']


@app.route('/')
async def index():
    return await render_template('index.html')

async def run_event():
    client.start()
    print('client started')
    await client.run_until_disconnected()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(app.run_task())
    loop.create_task(main())
    loop.run_until_complete(asyncio.sleep(800))
