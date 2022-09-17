import telebot
import translators as ts
from gtts import gTTS
import os

bot = telebot.TeleBot("5693614084:AAH0Adyz6h_9gieHPJ3bbEMADueLC--IVDs", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, I am your translator bot.")

@bot.message_handler(func=lambda m: True)
def translate(message):
    translated_message = ts.google(message.text, from_language="ru", to_language = 'en')
    bot.reply_to(message, translated_message)
    spoken_message = gTTS(translated_message, lang='en')
    spoken_message.save("message.mp3")
    bot.send_audio(chat_id=message.chat.id, audio=open("message.mp3", 'rb'))
    os.remove("message.mp3")

bot.infinity_polling()