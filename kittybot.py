from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


BOT_TOKEN = '6496934614:AAFof2bPovzRv2Tprzl6-l-7I6GcoFweMJw'


updater = Updater(token=BOT_TOKEN)


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.effective_chat.first_name
    button = ReplyKeyboardMarkup([['Показать фото котика']])
    context.bot.send_message(
        chat_id=chat.id, text='Спасибо, что включили меня {}!'.format(name),
        reply_markup=button
    )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling(poll_interval=20.0)
updater.idle()

# bot = Bot(token=BOT_TOKEN)
# chat_id = '235620212'
# text = 'New message!'
# bot.send_message(chat_id, text)
