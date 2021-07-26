import telebot
import config
from keyboards import *
from messages import messages

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.from_user.id, messages['greeting'], reply_markup=courses_keyboard)


@bot.message_handler(content_types='text')
def send_course_info(message):
    if message.text == '1️⃣ Python & Django':
        bot.send_message(message.from_user.id, messages['python'], reply_markup=url_keyboard)
    elif message.text == '2️⃣ JavaScript & React':
        bot.send_message(message.from_user.id, messages['javascript'], reply_markup=url_keyboard)
    elif message.text == '3️⃣ SMM':
        bot.send_message(message.from_user.id, messages['smm'], reply_markup=url_keyboard)
    elif message.text == '4️⃣ Graphic design':
        bot.send_message(message.from_user.id, messages['graphic_design'], reply_markup=url_keyboard)
    elif message.text == '5️⃣ Wordpress':
        bot.send_message(message.from_user.id, messages['wordpress'], reply_markup=url_keyboard)
    elif message.text == '6️⃣ Scratch':
        bot.send_message(message.from_user.id, messages['scratch'], reply_markup=url_keyboard)
    else:
        bot.send_message(message.from_user.id, messages['help'])


bot.polling(none_stop=True)
