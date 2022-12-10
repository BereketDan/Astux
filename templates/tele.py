
from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 11928039
api_hash = 'a58c3e1b29d071e8d457975995301d20'
client = TelegramClient('+251966442525', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    username = me.username
    print(username)
    print(me.phone)



with client:
    client.loop.run_until_complete(main())
