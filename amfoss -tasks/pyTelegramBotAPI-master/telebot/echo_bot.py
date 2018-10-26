import telebot

bot = telebot.TeleBot("659259469:AAFAC2ZS9et4Rv6-gxwjyysK1wAMQzwJ3Jo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
