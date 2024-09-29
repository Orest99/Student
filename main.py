import telebot
bot = telebot.TeleBot('7607049913:AAGZIfJPpNJrVd8BSEInb-1Q4PtWWHLvtqE')
@bot.message_handler(commands = ['start'])
def start (message):
    bot.send_message(message.chat.id,'Вітаю,бажаєте поспілкуватися?')


@bot.message_handler(commands = ['stop'])
def stop (message):
    bot.send_message(message.chat.id,'Stop')
    bot.stop_polling()

@bot.message_handler(commands=['close'])
def close_chat(message):
    bot.send_message(message.chat.id, 'close')
    bot.stop_polling()

@bot.message_handler()
def replay(message):
    for i in range(1):
     bot.reply_to(message,message.text)

bot.polling(non_stop=True)
#def button1():
 #   buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
 #   button1 = types.KeyboardButton(text1 = "Бан")
  #  buttons.add(button1)
   # return buttons

#def ban_user(message3):
  #  bot.send_message(message3.chat.id, "Ви заблоковані на 1 хвилину")
   # bot.restrict_chat_member(message3.chat.id, message3.from_user.id, ban=time.time() + 60)

#bot.polling()
