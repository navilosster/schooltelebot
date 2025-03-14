import telebot
from telebot import types

bot = telebot.TeleBot('7861601236:AAEGtm3NEA-CTGrAHje-ffiKatgVaVD_RsU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Меню блюд по дням')
    item2 = types.KeyboardButton('График завтраков, обедов и полдников')
    item3 = types.KeyboardButton('Распределение столов')
    item4 = types.KeyboardButton("Список дежурных")
    
    markup.add(item1, item2, item3, item4) 
    
    bot.send_message(message.chat.id, '*Привет, {0.first_name}! Выбери нужную тебе информацию. Все сведения о школьной столовой взяты с официального сайта МБОУ СОШ №15. https://pytnashka-kras.edumsko.ru/conditions/eating *'.format(message.from_user), reply_markup = markup, parse_mode= "Markdown")
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Меню блюд по дням':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('1-й день')
            item2 = types.KeyboardButton('2-й день')
            item3 = types.KeyboardButton('3-й день')
            item4 = types.KeyboardButton('4-й день')
            item5 = types.KeyboardButton('5-й день')
            item6 = types.KeyboardButton('6-й день')
            item7 = types.KeyboardButton('7-й день')
            item8 = types.KeyboardButton('8-й день')
            item9 = types.KeyboardButton('9-й день')
            item10 = types.KeyboardButton('10-й день')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)
            
            bot.send_message(message.chat.id, '*Выбери нужный тебе день*', reply_markup = markup, parse_mode= "Markdown")
        elif(message.text == "1-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша 'Дружба', сыр(порциями), печенье, какао на молоке, хлеб из муки пшеничной. Калорийность: 638 ккал._ \n\n*2. Обед:* _Салат витаминный с растительным маслом(салат из квашенной капусты), суп вермишеливый на курином бульоне, рагу из мяса птицы (курица), напиток из плодов сушеных, хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 608 ккал._ \n\n*3. Полдник:* _Оладьи (пудинг манный), соус вишневый, масло сливочное, чай, хлеб из муки пшеничной. Калорийность 735 ккал_", parse_mode= "Markdown")
        elif(message.text=="2-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша овсяная, фрукты свежие по сезонности, сыр порциями, кофейный напиток из цикория с молоком, хлеб из муки пшеничной. Калорийность: 396 ккал._ \n\n*2. Обед:* _Огурцы свежие(огурцы консервированные без уксуса), суп картофельный с горохом, котлеты рубленые из птицы, капуста тушеная, кисель вишневый, хлеб из муки пшеничной, хлеб ржано-пшеничный._ \n\n*3. Полдник:* _Запеканка со свежими плодами, сок фруктовый, фрукты свежие по сезонности, хлеб из муки пшеничной. Калорийность: 462 ккал_",  parse_mode= "Markdown")
        elif(message.text=="3-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Пудинг из творога запеченный, соус абрикосовый, сыр (порциями), чай с лимонами, хлеб из муки пшеничной. Калорийность: 658 ккал._ \n\n*2. Обед:* _Икра из кабачков, борщ с капустой и картофелем, гуляш из мяса птицы, каша гречневая, компот из плодов свежих(яблоки), хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность 566 ккал._ \n\n*3. Полдник:* _Огурцы, консервированные без уксуса, котлета рыбная, рагу из овощей, напиток клубничный, хлеб из муки пшеничной. Калорийность: 446 ккал._",  parse_mode= "Markdown")
        elif(message.text=="4-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Омлет, печенье, какао-напиток на молоке, хлеб из муки пшеничной. Калорийность: 641 ккал._ \n\n*2. Обед:* _Салат Осенний, суп картофельный с рисом, котлета рыбная, пюре картофельное, компот из плодов сушеных, хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 603 ккал._ \n\n*3. Полдник:* _Кукуруза консервированная, макароны с сыром, чай, хлеб из муки пшеничной. Калорийность: 452 ккал._", parse_mode="Markdown")
        elif(message.text=="5-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша пшенная, сыр (порциями), печенье, кофейный напиток злаковый на молоке, хлеб из муки пшеничной. Калорийность: 599 ккал._ \n\n*2. Обед:* _Салат и свеклы с маслом растительным, суп картофельный с фасолью, пельмени с маслом сливочным, компот из плодов свежих (яблоки), хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 944 ккал._ \n\n*3. Полдник:* _Пудинг из творога запеченный, молоко сгущенное, фрукты свежие по сезонности, чай с молоком, хлеб из муки пшеничной. Калорийность: 538 ккал._",  parse_mode= "Markdown")
        elif(message.text=="6-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша рисовая, печенье, сыр (порциями), чай с лимоном, хлеб из муки пшеничной. Калорийность: 589 ккал._ \n\n*2. Обед:* _Огурцы консервированные (свежие), Рассольник ленинградский, биточки рубленые куриные, рис отварной, компот из плодов свежих (лимон), хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 585 ккал._ \n\n*3. Полдник:* _Оладьи (пудинг манный), соус вишневый, кофейный напиток из цикория с молоком, хлеб из муки пшеничной. Калорийность: 816 ккал._",  parse_mode= "Markdown")
        elif(message.text=="7-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша овсяная, печенье, сыр (порциями), чай с молоком, хлеб из муки пшеничной. Калорийность: 571 ккал._ \n\n*2. Обед:* _Салат из капусты с растительным маслом (салат из квашеной капусты), суп вермишелевый на курином бульоне, печень по-строгановски, изделия макаронные отварные, компот из плодов сушеных, хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 633 ккал._ \n\n*3. Полдник:* _Запеканка со свежими плодами, печенье, чай, хлеб из муки пшеничной. КалорийностЬ: 562 ккал._",  parse_mode= "Markdown")
        elif(message.text=="8-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша гречневая молочная, сыр (порциями), фрукты свежие по сезонности, кофейный напиток из цикория с молоком, , хлеб из муки пшеничной. КалорийностЬ: 466 ккал._ \n\n*2. Обед:* _Икра из кабачков, борщ с капустой и картофелем, котлета рыбная, картофель отварной резаный, кисель вишневый, хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 635 ккал._ \n\n*3. Полдник:* _Блины (пудинг рисовый), молоко сгущенное, масло сливочное, фрукты свежие по сезонности, сок фруктовый, хлеб из муки пшеничной. Калорийность: 661 ккал._",  parse_mode= "Markdown")
        elif(message.text=="9-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Омлет, чай, печенье, хлеб из муки пшеничной. Калорийность: 580 ккал._ \n\n*2. Обед:* _Салат Мозаика, суп картофельный с фасолью, плов куриный, напиток клубничный, хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 712 ккал._ \n\n*3. Полдник:* _Салат из помидоров и огурцов (кукуруза консервированная), макароны с сыром, компот из плодов сушеных, хлеб из муки пшеничной. Калорийность: 553 ккал._",  parse_mode= "Markdown")
        elif(message.text=="10-й день"):
            bot.send_message(message.chat.id, "1. *Завтрак:* _Каша овсяная, сыр порциями, фрукты свежие по сезонности, какао-напиток на молоке, хлеб из муки пшеничной. Калорийность: 408 ккал._ \n\n*2. Обед:* _Салат из свеклы с растительным маслом, щи из свежей капусты, пельмени с маслом сливочным , компот из плодов свежих (яблоки), хлеб из муки пшеничной, хлеб ржано-пшеничный. Калорийность: 906 ккал._ \n\n*3. Полдник:* _Запеканка из творога, соус абрикосовый, фрукты свежие по сезонности, напиток из плодов сухих (изюм), хлеб из муки пшеничной. Калорийность: 561 ккал._",  parse_mode= "Markdown")
            
            
            
                   
        if message.text == 'График завтраков, обедов и полдников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Завтрак')
            item2 = types.KeyboardButton('Обед')
            item3 = types.KeyboardButton('Полдник')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)
            
            bot.send_message(message.chat.id, '*График чего хочешь узнать?*', reply_markup = markup, parse_mode= 'Markdown')
        elif(message.text=="Завтрак"):
            bot.send_message(message.chat.id, "*1. Время:* _9.10-9.20._ *Группа/класс:* _1А, 1В, 2А, 2Б, 2В, 4В, 4Г._ \n\n*2. Время:* _10.00-10.10._ *Группа/класс:* _5А, 5Б, 5В, 5Г, 5Д._ \n\n*3. Время:* _10.10-10-20._ *Группа/класс:* _6А, 6Б, 6В, 6Г, 6Д._ \n\n*4. Время:* _11.00-11.10._ *Группа/класс:* _7А, 7Б, 7В, 7Г, 8А, 8Б, 8В, 8Г, 9А, 9Б, 9В, 9Г, 10А, 10Б, 11А, 11Б._", parse_mode="Markdown")
        elif(message.text=="Обед"):
            bot.send_message(message.chat.id, "*1. Время:* _11.55-12.10._ *Группа/класс:* _1А, 1В._ \n\n*2. Время:* _12.40-13.00._ *Группа/класс:* _5А, 5Б, 5В, 5Г, 5Д, 6А, 6Б, 6В, 6Г, 6Д._ \n\n*3. Время:* _13.10-13.20._ *Группа/класс:* _2А, 2Б, 2В._ \n\n*4. Время:* _13.20-13.30._ *Группа/класс:* _4В, 4Г._ \n\n*5. Время:* _13.40-13.50._ *Группа/класс:* _7А, 7Б, 7В, 7Г, 8А, 8Б, 8В, 8Г._ \n\n*6. Время:* _14.30-14.40._ *Группа/класс:* _9А, 9Б, 9В, 9Г, 10А, 10Б, 11А, 11Б_", parse_mode= "Markdown")
        elif(message.text=="Полдник"):
            bot.send_message(message.chat.id, "*Время:* _16.30-17.30._ *Группа/класс:* _5-9 классы_", parse_mode= 'Markdown')
            
        elif message.text== "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Меню блюд по дням')
            item2 = types.KeyboardButton('График завтраков, обедов и полдников')
            item3 = types.KeyboardButton('Распределение столов')
            item4 = types.KeyboardButton("Список дежурных")
    
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "_Назад_", reply_markup=markup, parse_mode="Markdown")
            
        if message.text=="Распределение столов":
            bot.send_photo(message.chat.id, photo=("https://i.yapx.ru/YZYZ5.jpg"))
            bot.send_message(message.chat.id, "_Вход в столовую находится справа в нижнем углу, рядом с выделенным столом._", parse_mode="Markdown")
        
        
        if message.text=="Список дежурных":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton("09-10 января 2025")
            item2 = types.KeyboardButton("13-17 января 2025")
            item3 = types.KeyboardButton("20-24 января 2025")
            item4 = types.KeyboardButton("27-31 января 2025")
            item5 = types.KeyboardButton("03-07 февраля 2025")
            item6 = types.KeyboardButton("10-14 февраля 2025")
            item7 = types.KeyboardButton("24-28 февраля 2025")
            item8 = types.KeyboardButton("03-07 марта 2025")
            item9 = types.KeyboardButton("10-14 марта 2025")
            item10 = types.KeyboardButton("17-21 марта 2025")
            item11 = types.KeyboardButton("24-28 марта 2025")
            item12 = types.KeyboardButton("31-04 апреля 2025")
            item13 = types.KeyboardButton("14-18 апреля 2025")
            item14 = types.KeyboardButton("21-25 апреля 2025")
            item15 = types.KeyboardButton("28-02 мая 2025")
            item16 = types.KeyboardButton("05-09 мая 2025")
            item17 = types.KeyboardButton("12-16 мая 2025")
            item18 = types.KeyboardButton("19-23 мая 2025")
            item19 = types.KeyboardButton("26-30 мая 2025")
            item20 = types.KeyboardButton("02-06 июня 2025")
            back = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, back)
            bot.send_message(message.chat.id, "*Выбери нужную тебе дату*",reply_markup=markup, parse_mode="Markdown")
            
            
        elif message.text== "09-10 января 2025":
            bot.send_message(message.chat.id, "*Класс:* _9Г_. *Классный руководитель:* _Абрамцева Марина Олеговна_", parse_mode= "Markdown")
        elif message.text== "13-17 января 2025":
            bot.send_message(message.chat.id, "*Класс:* _9Г_. *Классный руководитель:* _Абрамцева Марина Олеговна_", parse_mode= "Markdown")
        elif message.text== "20-24 января 2025":
            bot.send_message(message.chat.id, "*Класс:* _8А_. *Классный руководитель:* _Кискина Наталья Станиславовна_", parse_mode= "Markdown")
        elif message.text== "27-31 января 2025":
            bot.send_message(message.chat.id, "*Класс:* _8Б_. *Классный руководитель:* _Елисеева Ирина Владимировна_", parse_mode= "Markdown")
        elif message.text== "03-07 февраля 2025":
            bot.send_message(message.chat.id, "*Класс:* _8В_. *Классный руководитель:* _Евстропова Марина Владимировна_", parse_mode= "Markdown")
        elif message.text== "10-14 февраля 2025":
            bot.send_message(message.chat.id, "*Класс:* _8Г_. *Классный руководитель:* _Каштанова Натальная Александровна_", parse_mode= "Markdown")
        elif message.text== "24-28 февраля 2025":
            bot.send_message(message.chat.id, "*Класс:* _7А_. *Классный руководитель:* _Глишин Евгения Геннадьевна_", parse_mode= "Markdown")
        elif message.text== "03-07 марта 2025":
            bot.send_message(message.chat.id, "*Класс:* _7Б_. *Классный руководитель:* _Велитченко Елена Анатольевна_", parse_mode= "Markdown")
        elif message.text== "10-14 марта 2025":
            bot.send_message(message.chat.id, "*Класс:* _7В_. *Классный руководитель:* _Гавенко Арина Сергеевна_", parse_mode= "Markdown")
        elif message.text== "17-21 марта 2025":
            bot.send_message(message.chat.id, "*Класс:* _7Г_. *Классный руководитель:* _Яблокова Кристина Владиславовна_", parse_mode= "Markdown")
        elif message.text== "24-28 марта 2025":
            bot.send_message(message.chat.id, "*Класс:* _10А_. *Классный руководитель:* _Спинка Татьяна Викторовна_", parse_mode= "Markdown")
        elif message.text== "31-04 апреля 2025":
            bot.send_message(message.chat.id, "*Класс:* _10Б_. *Классный руководитель:* _Парамзин Дмитрий Николаевич_", parse_mode= "Markdown")
        elif message.text== "14-18 апреля 2025":
            bot.send_message(message.chat.id, "*Класс:* _8А_. *Классный руководитель:* _Кискина Наталья Станиславовна_", parse_mode= "Markdown")
        elif message.text== "21-25 апреля 2025":
            bot.send_message(message.chat.id, "*Класс:* _8Б_. *Классный руководитель:* _Елисеева Ирина Владимировна_", parse_mode= "Markdown")
        elif message.text== "28-02 мая 2025":
            bot.send_message(message.chat.id, "*Класс:* _8В_. *Классный руководитель:* _Евстрапова Марина Владимировна_", parse_mode= "Markdown")
        elif message.text== "05-09 мая 2025":
            bot.send_message(message.chat.id, "*Класс:* _8Г_. *Классный руководитель:* _Каштанова Натальая Александровна_", parse_mode= "Markdown")
        elif message.text== "12-16 мая 2025":
            bot.send_message(message.chat.id, "*Класс:* _10А_. *Классный руководитель:* _Спинка Татьяна Викторовна_", parse_mode= "Markdown")
        elif message.text== "19-23 мая 2025":
            bot.send_message(message.chat.id, "*Класс:* _10Б_. *Классный руководитель:* _Парамзин Дмитрий Николаевич_", parse_mode= "Markdown")
        elif message.text== "26-30 мая 2025":
            bot.send_message(message.chat.id, "*Класс:* _7-8 классы_. *Классный руководитель:* _Движение Первых, куратор: Гавенко Арина Сергеевна_", parse_mode= "Markdown")
        elif message.text== "02-06 июня 2025":
            bot.send_message(message.chat.id, "*Класс:* _7-8 классы_. *Классный руководитель:* _Волонтерский отряд 'Мы вместе', руководитель: Спинка Татьяна Викторовна_", parse_mode= "Markdown")
        
    
bot.polling(none_stop = True)