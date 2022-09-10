import telebot
import translators as ts


bot = telebot.TeleBot("5693614084:AAH0Adyz6h_9gieHPJ3bbEMADueLC--IVDs", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, I am your translator bot.")

@bot.message_handler(func=lambda m: True)
def translate(message):
	bot.reply_to(message, ts.google(message.text, from_language="ru", to_language = 'en'))

bot.infinity_polling()