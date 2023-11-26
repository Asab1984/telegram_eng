import telebot

bot = telebot.TeleBot('6094190681:AAGlPEvKLMjoODti33RvGaignCZe4lk_fxc')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['hello'])
def hello(message):
    text = 'Привіт, як твої справи.'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['ask_me'])
def ask_me(message):
    text = 'Запитай мене'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'і тобі привіт')
    elif message.text == 'ask_me':
        bot.send_message(message.chat.id, 'вибери категорію')
    elif message.text == 'ask_me logo':
        photo = open('ask me.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'datetime documentation':
        doc = open('documentation.html', 'r')
        bot.send_document(message.chat.id, doc)
    else:
        bot.send_message(message.chat.id, 'Я тебе не розумію')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Класна фотографія')


bot.polling(non_stop=True)

