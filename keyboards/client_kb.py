from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

#KeyboardButton Репась 
kb1=KeyboardButton('💸Навалить репася💸')
kb1_client = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb1_client.add(kb1)

#add - c новой строки 
#row - в одну строку 
#insert - если есть свободное место 


#KeyboardButton Менюшка 
#kb_cats = KeyboardButton('😻Котики😻')
kb2 = KeyboardButton('🔗Links🔗')
kb3 = KeyboardButton('🔐Get my ID🔐')
kb_kazic_enter = KeyboardButton('🎰Казик🎰')
kb_exit = KeyboardButton('❌EXIT❌')
#kb_memes = KeyboardButton('⚡Мемесы⚡')
kb2_client = ReplyKeyboardMarkup(resize_keyboard = True)
kb2_client.add(kb2,kb3).add(kb_kazic_enter).add(kb_exit)#.add(kb_cats)#.add(kb_memes)




#KeyboardButton Каизно меню 

kb_spin = KeyboardButton('🔄Крутить')
kb_exit = KeyboardButton('Выход⏩')
kb_kazic_menu = ReplyKeyboardMarkup(resize_keyboard = True)#, one_time_keyboard = True)
kb_kazic_menu.add(kb_spin,kb_exit)

'''
#InlineKeyboardButton Казик не работает отдельно, не рандомится
kazic_list = ['\U0001F4A9','\U0001F4A3','\U0001F352','\U0001F347','\U0001F34C','\U0001F340','\U0001F349']

ikb_kazic = InlineKeyboardMarkup(row_width=3)
ibk1 = InlineKeyboardButton (text = random.choice(kazic_list) ,callback_data='kaz1' )
ibk2 = InlineKeyboardButton (text = random.choice(kazic_list), callback_data= 'kaz2')
ibk3 = InlineKeyboardButton (text = random.choice(kazic_list), callback_data= 'kaz3')
ikb_kazic.add(ibk1,ibk2,ibk3)
'''
#InlineKeyboardButton кисаки

'''
ikb_more_cats = InlineKeyboardButton(text = '⏩⏩⏩Еще больше кисак⏪⏪⏪',callback_data = 'cats')
ikb_cats = InlineKeyboardMarkup(row_width=1)
ikb_cats.add(ikb_more_cats)
'''

##






#InlineKeyboardButton Ссылки
ikb_links = InlineKeyboardMarkup(row_width=1)
ib1 = InlineKeyboardButton (text='🔥Dumb Ways to Live : Album🔥',url ='https://push.fm/fl/dumbwaystolive')
ib2 = InlineKeyboardButton (text='🔥Say Goodbye 🔥',url ='https://www.youtube.com/watch?v=0GcL8K3gkXE')
ikb_links.add(ib1,ib2)