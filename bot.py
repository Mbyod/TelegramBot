from aiogram import executor
from create_bot import dp

async def on_startup(_):
    print('Bot has been started')
    
from handlers import client,admin, other    

client.register_handlers_client(dp)



executor.start_polling(dp,on_startup=on_startup, skip_updates = True)