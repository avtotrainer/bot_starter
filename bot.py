import telebot

bot=telebot.TeleBot('6450641365:AAEJyLYrQJkq_HUgmftauH8uOwVpx7krHuo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b>ვაა, ბარო</b> {message.from_user.first_name} {message.from_user.last_name}',parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help(message):    
    bot.send_message(message.chat.id, '<b>მე ვარ</b> - <i>მომავლის ბოტი</i> ',parse_mode='HTML')

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, f'{message}')

bot.polling(non_stop=True)