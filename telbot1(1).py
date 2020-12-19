import telebot
import pandas as pd
import numpy as np
from telebot import types

frame = pd.read_excel('kachan.xls', header=0)
M = np.array(frame)
Token = '1302586780:AAH2QhIUyjPQCBVcIE3j7NMRNaVyvjle3m4'

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    but1 = types.KeyboardButton('Качественные реакции')
    but2 = types.KeyboardButton('Материал для учебы')
    keyboard.add(but1, but2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы обучить тебя химии.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Что вас интересует? ', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def heeelp(message):
    bot.send_message(message.chat.id,
                     "Hello, hello, меня зовут Cabbagehead, я был создан для того, чтобы помогать студентам быстро находить качественные реакции на определенные ионы в неорганической химии.Алгоритм работы крайне прост: изначально, необходимо выбрать элемент из таблицы Менделеева, качественную реакцию на ион которого, тебе, fellow, хотелось бы узнать. Если такой элемент есть в моей программе, то тебе будет предложен ряд ионов, из которых необходимо выбрать нужный тебе. Бот выдает краткую справочную информацию о реакциях, при необходимости каких-либо полезных комментариев")




@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'В начало':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

            but1 = types.KeyboardButton('Качественные реакции')
            but2 = types.KeyboardButton('Материал для учебы')
            keyboard.add(but1, but2)

            bot.send_message(message.chat.id, 'Что вас интересует? ', reply_markup = keyboard)
        elif message.text == 'Качественные реакции':
            keys = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item1 = types.KeyboardButton('I')
            item2 = types.KeyboardButton('II')
            item3 = types.KeyboardButton('III')
            item4 = types.KeyboardButton('IV')
            item5 = types.KeyboardButton('V')
            item6 = types.KeyboardButton('VI')
            item7 = types.KeyboardButton('VII')
            item8 = types.KeyboardButton('VIII')
            item_home = types.KeyboardButton('В начало')

            keys.add(item1, item2, item3, item4, item5, item6, item7, item8, item_home)
            bot.send_message(message.chat.id, 'выбери группу ', reply_markup = keys)

        elif message.text == 'Материал для учебы':
            file_1 = open('Tretyakov_1_tom.pdf', 'rb')
            file_2 = open('Tretyakov_2_tom.pdf', 'rb')
            file_3 = open('Tretyakov_3_tom_1_chast.pdf', 'rb')
            file_4 = open('Tretyakov_3_tom_2_chast.pdf', 'rb')
            bot.send_document(message.chat.id, file_1)
            bot.send_document(message.chat.id, file_2)
            bot.send_document(message.chat.id, file_3)
            bot.send_document(message.chat.id, file_4)


        elif message.text == 'I':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Li\u207A", callback_data='Li')
            item2 = types.InlineKeyboardButton("Na\u207A", callback_data='Na')
            item3 = types.InlineKeyboardButton("K\u207A", callback_data='K')
            item4 = types.InlineKeyboardButton("Cu\u207A", callback_data='Cu')
            item5 = types.InlineKeyboardButton("Ag\u207A", callback_data='Ag')

            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup = markup)

        elif message.text == 'II':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Ba\u00b2\u207A', callback_data='Ba')
            item2 = types.InlineKeyboardButton('Ca\u00b2\u207A', callback_data='Ca')
            item3 = types.InlineKeyboardButton('Mg\u00b2\u207A', callback_data='Mg')
            item4 = types.InlineKeyboardButton('Sr\u00b2\u207A', callback_data='Sr')
            item5 = types.InlineKeyboardButton('Zn\u00b2\u207A', callback_data='Zn')
            item6 = types.InlineKeyboardButton('Hg\u00b2\u207A', callback_data='Hg')
            item7 = types.InlineKeyboardButton('Cd\u00b2\u207A', callback_data='Cd')
            markup.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup = markup)

        elif message.text == 'III':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Al\u00b3\u207A', callback_data='Al')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup = markup)
        elif message.text == 'IV':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Sn', callback_data='Sn')
            item2 = types.InlineKeyboardButton('Pb', callback_data='Pb')
            item3 = types.InlineKeyboardButton('C', callback_data='CO3')
            item4 = types.InlineKeyboardButton('Si', callback_data='SiO3')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Выбери элемент ', reply_markup = markup)

        elif message.text == 'V':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('NO\u2083\u207B', callback_data='NO3')
            item2 = types.InlineKeyboardButton('NH\u2084\u207A', callback_data='NH4')
            item3 = types.InlineKeyboardButton('PO\u2084\u00b3\u207B', callback_data='PO4')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup=markup)

        elif message.text == 'VI':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('SO\u2084\u00b2\u207B', callback_data='SO4')
            item2 = types.InlineKeyboardButton('Cr\u00b3\u207A', callback_data='Cr')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup = markup)

        elif message.text == 'VII':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('I\u207B', callback_data='I')
            item2 = types.InlineKeyboardButton('Cl\u207B', callback_data='Cl')
            item3 = types.InlineKeyboardButton('Br\u207B', callback_data='Br')
            item4 = types.InlineKeyboardButton('IO\u00b3\u207B', callback_data='IO3')

            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup=markup)

        elif message.text == 'VIII':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Fe\u00b2\u207A', callback_data='Fe2')
            item2 = types.InlineKeyboardButton('Fe\u00b3\u207A', callback_data='Fe3')
            item3 = types.InlineKeyboardButton('Co\u00b2\u207A', callback_data='Co')

            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Выбери ион ', reply_markup=markup)


    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    elem = call.data
    c = np.where(elem == M)[0][0]
    bot.send_message(call.message.chat.id, frame.iloc[c][2])


# RUN
bot.polling(none_stop=True)
