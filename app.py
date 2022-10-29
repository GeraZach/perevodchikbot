import telebot
from googletrans import Translator
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot('5450770358:AAGd3aPEHv0YiRu9byyu3QgmvF3bP0lrXZo')
firstlang = 'en'
secondlang = 'ru'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Привет!</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Просто начни писать текст, который нужно перевести. Все настроить сможешь уже в процессе")


@bot.message_handler(content_types=['text'])
def callback_query(message):
    key = types.InlineKeyboardMarkup()
    if firstlang == 'en':
        but_1 = types.InlineKeyboardButton(text=r"\U+1F1EC U+1F1E7", callback_data="NumberOne")

    but_2 = types.InlineKeyboardButton(text="Swap languages", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="Second", callback_data="NumberTree")

    key.add(but_1, but_2, but_3)

    translator = Translator()
    result = translator.translate(message.text, src=firstlang, dest=secondlang)
    bot.send_message(message.chat.id, f"Перевод: {result.text}", reply_markup=key)


@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'NumberOne':
        global firstlang, secondlang
        bot.send_message(c.message.chat.id, f'1 язык: {firstlang}')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="English", callback_data="feng")
        but_2 = types.InlineKeyboardButton(text="Russian", callback_data="fru")
        but_3 = types.InlineKeyboardButton(text="French", callback_data="ffr")

        key.add(but_1, but_2, but_3)
        bot.send_message(c.message.chat.id, 'Выберите нужный вам язык:', reply_markup=key)

    if c.data == 'NumberTwo':
        swapper = secondlang
        secondlang = firstlang
        firstlang = swapper
        bot.send_message(c.message.chat.id, 'Языки свапнуты')
    if c.data == 'NumberTree':
        bot.send_message(c.message.chat.id, f'2 язык: {secondlang}')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="English", callback_data="seng")
        but_2 = types.InlineKeyboardButton(text="Russian", callback_data="sru")
        but_3 = types.InlineKeyboardButton(text="French", callback_data="sfr")

        key.add(but_1, but_2, but_3)
        bot.send_message(c.message.chat.id, 'Выберите нужный вам язык:', reply_markup=key)

    if c.data == 'feng':
        firstlang = 'en'
        bot.send_message(c.message.chat.id, f'Язык успешно выбран! {firstlang}')
    if c.data == 'fru':
        firstlang = 'ru'
        bot.send_message(c.message.chat.id, f'Язык успешно выбран! {firstlang}')
    if c.data == 'ffr':
        firstlang = 'fr'
        bot.send_message(c.message.chat.id, f'Язык успешно выбран! {firstlang}')
    if c.data == 'seng':
        secondlang = 'en'
        bot.send_message(c.message.chat.id, f'Язык успешно выбран! {secondlang}')
    if c.data == 'sru':
        secondlang = 'ru'
        bot.send_message(c.message.chat.id, f'Язык успешно выбран! {secondlang}')
    if c.data == 'sfr':
        secondlang = 'fr'
        bot.send_message(c.message.chat.id, f'Язык успешно выбран! {secondlang}')





bot.infinity_polling()


#message.text -- text soobcheniya
#translator = Translator()
#print(translator.detect(text1))

#print(translator.translate(text1))

#markup = types.InlineKeyboardMarkup() создает кнопку в сообщении
  # markup.add(types.InlineKeyboardButton('Translate', url='https://translate.google.com'))
   # bot.send_message(message.chat.id, 'Введите текст для перевода', reply_markup=markup)