import telebot
from telebot import types
import BotConfig
import Parser

bot = telebot.TeleBot(BotConfig.Token)
start_msg = 'Работать - запуск скрипта. \nМеню - Настройка запроса. \nБД - База данных. '


name = 'Инженер'
area = 2
pages = 0
results_per_page = 1

Params = {	'text': name,
	        'area': int(area),
	        'page': int(pages),
	        'per_page': int(results_per_page)
        }



# Начальное меню.

@bot.message_handler(commands=['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Работать!')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton('БД')
    markup.add(btn1)
    markup.add(btn2, btn3)
    bot.send_message(message.from_user.id, start_msg, reply_markup=markup)
    bot.register_next_step_handler(message, click)

def click(message):
    match message.text:
        case 'Работать!':
            global Params
            bot.register_next_step_handler(message, Parser.GetVacancy(Params))
            #bot.register_next_step_handler(message, phloc(message))
            Vac = Parser.Vcncy
            for i in Vac:
                bot.send_message(message.chat.id, i)
            print(Vac)

        case 'Меню':
            #bot.send_message(message.chat.id, 'Ok')
            bot.register_next_step_handler(message, menu)
            #bot.register_next_step_handler(message, phloc(message))
        case 'БД':
            bot.send_message(message.chat.id, 'В процессе доработки.')


# Кнопка "Меню". Настройка словаря (Params).

def menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Название вакансии', callback_data='btn_1')
    btn2 = types.InlineKeyboardButton(text='Город', callback_data='btn_2')
    btn3 = types.InlineKeyboardButton(text='Колличество страниц', callback_data='btn_3')
    btn4 = types.InlineKeyboardButton(text='Колличество вакансий на страницу', callback_data='btn_4')
    btn5 = types.InlineKeyboardButton(text='Показать "Params"', callback_data='btn_5')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    bot.send_message(message.from_user.id, 'Push the button', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    match call.data:
        case 'btn_1':
            bot.send_message(call.from_user.id, 'Введите название вакансии:')
#            @bot.message_handler(content_types=['text'])
#            def answer(message):
#                global name
#                name = message.text
#                print(name)
#                print(Params)

        case 'btn_2':
            bot.send_message(call.from_user.id, 'Нажата кнопка 2')
            #@bot.message_handler(content_types=['text'])

        case 'btn_3':
            bot.send_message(call.from_user.id, 'Нажата кнопка 3')
            #@bot.message_handler(content_types=['text'])

        case 'btn_4':
            bot.send_message(call.from_user.id, 'Нажата кнопка 4')
            #@bot.message_handler(content_types=['text'])

        case 'btn_5':
            bot.send_message(call.from_user.id, 'Нажата кнопка 5')
            bot.send_message(call.from_user.id, ''.join(str(Params)))
            #bot.send_message(call.from_user.id, f'text\n{sep.join(i for i in Params)}')


def input_answer(message):
    global name
    name = message

def phloc(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, ' ', reply_markup=markup)






bot.polling(none_stop=True)
