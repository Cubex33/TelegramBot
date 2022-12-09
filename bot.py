import telebot
from telebot import types

bot = telebot.TeleBot('5874126638:AAG03XaWYIRiCA7qwTGZwPubqBpODY0z8qY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    markup = types.ReplyKeyboardMarkup()
    my_games = types.KeyboardButton('🎮мои проекты')
    markup.add(my_games)
@bot.message_handler(content_types=['photo'])
def Get_Photo(message):
    bot.send_message(message.chat.id, 'Вау крутое фото')




bot.polling(non_stop=True)