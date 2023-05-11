
from aiogram import Bot, types, Dispatcher
from  create_bot import dp, bot
from keyboards import kb1_client, kb2_client, ikb_links , kb_kazic_menu 
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#@dp.message_handler(commands=['start']) 
async def start_cmd(message: types.Message):
	await message.answer(text = '📡Бот SVGS у домофона 👉👈',reply_markup = kb1_client)
	await message.delete()

async def rap_cmd(message: types.Message):
    user_name = str(message.from_user.first_name)
    await bot.send_message(message.chat.id,f'{user_name}❗❗❗ Жоска навалил жиденьким репчиком💩',reply_markup = kb2_client)
    await message.delete()  

async def links_cmd(message: types.Message):
    await bot.send_message(message.chat.id,'👇 Ссылки от Savages 👇',reply_markup = ikb_links) 
    await message.delete()

async def id_cmd(message: types.Message):
    user_id = str(message.from_user.id)
    await bot.send_message(message.chat.id,f'Твой ID: `{user_id}`',parse_mode='MarkdownV2')
    await message.delete()
    
async def id_kazic_entrance(message: types.Message):
    
    await bot.send_message(message.chat.id,'Привет, лудоманище',reply_markup = kb_kazic_menu)
    await message.delete()

async def id_kazic_exit(message: types.Message):
    
    await bot.send_message(message.chat.id,'Пока, лудоманище',reply_markup = kb2_client)
    await message.delete()


async def id_kazic_new(message: types.Message):
    user_name = str(message.from_user.first_name)
    kazic_list = ['\U0001F4A9','\U0001F4A3','\U0001F352','\U0001F347','\U0001F34C','\U0001F340','\U0001F349']
    kaz1 = random.choice(kazic_list)
    kaz2 = random.choice(kazic_list)
    kaz3 = random.choice(kazic_list)
    ikb_kazic = InlineKeyboardMarkup(row_width=3)
    ibk1 = InlineKeyboardButton (text = kaz1  ,callback_data='kaz1' )
    ibk2 = InlineKeyboardButton (text = kaz2 , callback_data= 'kaz2')
    ibk3 = InlineKeyboardButton (text = kaz3, callback_data= 'kaz3')
    ikb_kazic.add(ibk1,ibk2,ibk3)
    await bot.send_message(message.chat.id,f'{user_name} продал почки и крутит фарту:',reply_markup = ikb_kazic)
    
    await message.delete()
    if kaz1==kaz2==kaz3:
        await bot.send_message(message.chat.id,f'💸💸💸{user_name}💸💸💸ограбил💸💸💸робота💸💸💸ЖЕСТЬ💸💸💸ОН💸💸💸КРУТ💸💸💸')
        
    elif kaz1==kaz2==kaz3=='\U0001F347':
        await bot.send_message(message.chat.id,f'{user_name} 💩💩💩смачно обосрался💩💩💩')
        await message.delete()



async def id_exit(message: types.Message):
    await message.answer(text = 'пока',reply_markup =ReplyKeyboardRemove())
    
    await message.delete()

'''
def getcat():
    #Получение ссылки на картинку с котиками
    try:
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
    except:
        url = get_cat()
        print('Error with cat parsing')
        pass
    return url



async def id_sendcat(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=getcat(), reply_markup=kb2_client)
    await message.delete()
'''
'''

#################МЕМЫ##########################
import asyncpraw
from config import ID_CLIENT, SECRET
reddit = asyncpraw.Reddit(client_id = ID_CLIENT,
                    client_secret = SECRET,
                    user_agent = 'svgsbot')

memes = []
TIMEOUT = 300
SUBREDDIT_NAME ='memes'
POST_LIMIT = 1



async def id_memes(message : types.Message):
    await bot.send_message(message.chat.id,text)

async def main():
    while True:
        await asyncio.sleep(TIMEOUT)
        memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
        memes_submissions = memes_submissions.new(limit = POST_LIMIT)
        item = await memes_submissions.__anext__()
        if item.title not in memes:
            memes.append(item.title)
            await send_message(chat_id,)
        
    
'''





'''
async def id_more_cats(message: types.Message):
    """Отправка котиков"""
    await bot.send_photo(chat_id=message.chat.id, photo=getcat(), reply_markup=ikb_cats)
    await message.delete()
'''



################################################################################################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
import speech_recognition as sr
import subprocess
import datetime
import ffmpeg




def audio_to_text(dest_name: str):
# Функция для перевода аудио, в формате ".wav" в текст
    r = sr.Recognizer() # такое вообще надо комментить?
    # тут мы читаем наш .vaw файл
    message = sr.AudioFile(dest_name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language="ru_RU") # используя возможности библиотеки распознаем текст, так же тут можно изменять язык распознавания
    return result




logfile = str(datetime.date.today()) + '.log'

token = '5818134016:AAGVi1nnhuRE6AVh381LdDJ0A_dzdOOlg1A'

@dp.message_handler(content_types=['voice'])
async def get_audio_messages(message):
   #u_id = message.forward_from.first_name
    user_name1 = str(message.from_user.first_name)
# Основная функция, принимает голосовуху от пользователя
    try:
        
        # Ниже пытаемся вычленить имя файла, да и вообще берем данные с мессаги
        file_info = await bot.get_file(message.voice.file_id)
        path = os.path.splitext(file_info.file_path)[0] # Вот тут-то и полный путь до файла (например: voice/file_2.oga)
        fname = os.path.basename(path) # Преобразуем путь в имя файла (например: file_2.oga)
        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path)) # Получаем и сохраняем присланную голосвуху (Ага, админ может в любой момент отключить удаление айдио файлов и слушать все, что ты там говоришь. А представь, что такую бяку подселят в огромный чат и она будет просто логировать все сообщения [анонимность в телеграмме, ахахаха])
        with open(fname+'.oga', 'wb') as f:
            f.write(doc.content) # вот именно тут и сохраняется сама аудио-мессага
        process = subprocess.run(['ffmpeg', '-i', fname+'.oga', fname+'.wav'])# здесь используется страшное ПО ffmpeg, для конвертации .oga в .vaw
        result = audio_to_text(fname+'.wav') # Вызов функции для перевода аудио в текст
        
        await bot.send_message(message.chat.id,f'🔇{user_name1}🔇 сказал : "{format(result)}"') # Отправляем пользователю, приславшему файл, его текст
    except sr.UnknownValueError as e:
        # Ошибка возникает, если сообщение не удалось разобрать. В таком случае отсылается ответ пользователю и заносим запись в лог ошибок
        await bot.send_message(message.from_user.id,  "Ничего не разобрал")
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(str(datetime.datetime.today().strftime("%H:%M:%S")) + ':' + str(message.from_user.id) + ':' + str(message.from_user.first_name) + '_' + str(message.from_user.last_name) + ':' + str(message.from_user.username) +':'+ str(message.from_user.language_code) + ':Message is empty.\n')
    except Exception as e:
        # В случае возникновения любой другой ошибки, отправляется соответствующее сообщение пользователю и заносится запись в лог ошибок
        await bot.send_message(message.from_user.id,  "Ничего не работает, автор дибил ")
        with open(logfile, 'a', encoding='utf-8') as f:
            f.write(str(datetime.datetime.today().strftime("%H:%M:%S")) + ':' + str(message.from_user.id) + ':' + str(message.from_user.first_name) + '_' + str(message.from_user.last_name) + ':' + str(message.from_user.username) +':'+ str(message.from_user.language_code) +':' + str(e) + '\n')
    finally:
        #В любом случае удаляем временные файлы с аудио сообщением
        #os.remove(fname+'.wav')
        os.remove(fname+'.oga')





def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start_cmd, commands = ['start'])
    dp.register_message_handler(rap_cmd, text = ['💸Навалить репася💸'])
    dp.register_message_handler(links_cmd, text = ['🔗Links🔗'])
    dp.register_message_handler(id_cmd, text = ['🔐Get my ID🔐'])
    dp.register_message_handler(id_kazic_entrance, text = ['🎰Казик🎰'])
    dp.register_message_handler(id_kazic_new, text = ['🔄Крутить'])
    dp.register_message_handler(id_kazic_exit, text = ['Выход⏩'])
    dp.register_message_handler(id_exit, text = ['❌EXIT❌'])
   # dp.register_message_handler(id_more_cats, text = ['⏩⏩⏩Еще больше кисак⏪⏪⏪'])
    #dp.register_message_handler(id_sendcat, text = ['😻Котики😻'])
    #dp.register_message_handler(id_memes, text = ['⚡Мемесы⚡'])