from telebot.types import Message
import telebot
from wiki import wiki_summary_searching


TOKEN = "6944857545:AAEYMl9-_zn_-g7OKYyie6mtwwS-C9G5-Y8"
WIKIPEDIA_SET_LANGUAGE = "UZ"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start', 'main', 'help'])
def start(message: Message):
    bot.send_message(message.chat.id, "Salom 🖐️ Wikipediaga hush kelibsiz! Bu erda siz ozizga kerak malumotlarni wikipediadan qidirib topib beramiz.")


@bot.message_handler()
def wiki_start(message: Message):

    bot.send_message(message.chat.id, "Iltimos biroz kuting...")
    summary = wiki_summary_searching(message.text)
    bot.send_message(message.chat.id, summary)


def main():
   bot.polling(non_stop=True)


if __name__=='__main__':
    main()