import telebot
bot = telebot.TeleBot('1031196043:AAH1g4GzAfsR-7PebjLGuplNd3L1Sk9Eqz4')
@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, давай начнем знакомиться!)")
bot.polling()
