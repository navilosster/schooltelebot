import telebot
from telebot import types

bot = telebot.TeleBot('7861601236:AAEGtm3NEA-CTGrAHje-ffiKatgVaVD_RsU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Меню блюд по дням')
    item2 = types.KeyboardButton('График завтраков, обедов и полдников')
    item3 = types.KeyboardButton('Распределение столов')
    
    markup.add(item1, item2, item3) 
    
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Меню блюд по дням':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('1-ый день')
            item2 = types.KeyboardButton('2-ый день')
            item3 = types.KeyboardButton('3-ый день')
            item4 = types.KeyboardButton('4-ый день')
            item5 = types.KeyboardButton('5-ый день')
            item6 = types.KeyboardButton('6-ый день')
            item7 = types.KeyboardButton('7-ый день')
            item8 = types.KeyboardButton('8-ый день')
            item9 = types.KeyboardButton('9-ый день')
            item10 = types.KeyboardButton('10-ый день')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)
            
            bot.send_message(message.chat.id, 'Меню блюд по дням', reply_markup = markup)
                
        if message.text == 'График завтраков, обедов и полдников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Завтрак')
            item2 = types.KeyboardButton('Обед')
            item3 = types.KeyboardButton('Полдник')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)
            
            bot.send_message(message.chat.id, 'График завтраков, обедов и полдников', reply_markup = markup)
            
        elif message.text== "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Меню блюд по дням')
            item2 = types.KeyboardButton('График завтраков, обедов и полдников')
            item3 = types.KeyboardButton('Распределение столов')
    
            markup.add(item1, item2, item3) 
    
            bot.send_message(message.chat.id, 'Назад', reply_markup = markup)
            

            
    
bot.polling(none_stop = True)