import telebot

bot=telebot.TeleBot('6450641365:AAEJyLYrQJkq_HUgmftauH8uOwVpx7krHuo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'ვაა, ბარო {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, f'{message}')

bot.polling(non_stop=True)