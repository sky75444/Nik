import telebot

bot = telebot.TeleBot("1884598557:AAFuhZWBPD5dS37jSJEXHS002q2t5T48DII")


@bot.message_handler(commands=["start", "help"])
async def send_welcome(message):
    bot.reply_to(message, f"я бот. Привет {message.from_user.first_name}")


@bot.message_handler(content_types=["text"])
async def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет!")
    else:
        bot.send_message(message.from_user.id, "не понимаю что это значит")

bot.polling(none_stop=True)