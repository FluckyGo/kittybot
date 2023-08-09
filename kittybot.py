import os
import requests

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler

load_dotenv()

secret_token = os.getenv('BOT_TOKEN')
URL = 'https://api.thecatapi.com/v1/images/search'


def get_random_cat_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat_id=chat.id, photo=get_random_cat_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.effective_chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat_id=chat.id, photo=get_random_cat_image())


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling(poll_interval=10.0)

    updater.idle()


if __name__ == '__main__':
    main()
