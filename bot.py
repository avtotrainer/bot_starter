import telebot
from telebot import types

bot=telebot.TeleBot('6450641365:AAEJyLYrQJkq_HUgmftauH8uOwVpx7krHuo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b>ვაა, ბარო</b> {message.from_user.first_name} {message.from_user.last_name}',parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help(message):    
    bot.send_message(message.chat.id, '<b>მე ვარ</b> - <i>მომავლის ბოტი</i> ',parse_mode='HTML')



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.inline_handler(lambda query: True)
def inline_query(query):
    try:
        # ინლაინ ღილაკის შექმნა
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="დააკლიკეთ აქ!", callback_data="button_pressed")
        keyboard.add(button)

        # Создаем инлайн-результат с кнопкой
        result = types.InlineQueryResultArticle(
            id='1', title="დააკლიკეთ!",
            input_message_content=types.InputTextMessageContent(message_text="თქვენ დააკლიკეთ ღილაკზე!"),
            reply_markup=keyboard
        )

        bot.answer_inline_query(query.id, [result])

    except Exception as e:
        print(e)



# bot.polling(non_stop=True)

bot.infinity_polling()
