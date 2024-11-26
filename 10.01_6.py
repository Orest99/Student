import telebot
from telebot import types
from deep_translator import GoogleTranslator

TOKEN = '8047577921:AAE61QXc95IOCSzLbtUZh6sXORK4dpgP4Us'
bot = telebot.TeleBot(TOKEN)

target_language = 'en'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привіт! Я бот-перекладач. Надішліть мені текст, і я перекладу його англійською мовою. "
        "Щоб змінити мову перекладу, скористайтеся командою /language."
    )
languages = {
    "Англійська (en)": "en",
    "Німецька (de)": "de",
    "Французька (fr)": "fr",
    "Іспанська (es)": "es"
}

@bot.message_handler(commands=['language'])
def choose_language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for lang in languages.keys():
        markup.add(lang)
    bot.send_message(message.chat.id, "Оберіть мову для перекладу:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global target_language
    if message.text in languages:
        target_language = languages[message.text]
        bot.send_message(message.chat.id, "Мову перекладу змінено: " + message.text.split(' ')[0])
    else:
        translate_message(message)

def translate_message(message):
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(message.text)
    if translated_text:
        bot.send_message(message.chat.id, "Переклад: " + translated_text)
    else:
        bot.send_message(message.chat.id, "Вибачте, сталася помилка при перекладі. 😔")
        print("Помилка при перекладі")

bot.polling(none_stop=True)
