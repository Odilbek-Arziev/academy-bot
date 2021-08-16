from telebot import types

courses_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
url_keyboard = types.InlineKeyboardMarkup()

python = types.KeyboardButton(text='1️⃣ Python & Django')
javascript = types.KeyboardButton(text='2️⃣ JavaScript & React')
smm = types.KeyboardButton(text='3️⃣ CММ')
graphic_design = types.KeyboardButton(text='4️⃣ Графический дизайн')
wordpress = types.KeyboardButton(text='5️⃣ Wordpress')
scratch = types.KeyboardButton(text='6️⃣ Scratch')
courses_keyboard.add(python, javascript, smm, graphic_design, wordpress, scratch)

url_button = types.InlineKeyboardButton(url='macademy.uz', text='Перейдите на наш сайт')
url_keyboard.add(url_button)
