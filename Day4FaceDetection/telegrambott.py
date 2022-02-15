import telegram

# bot = telegram.bot(token='5189882159:AAHYGO_ZbfB16aGO2Q0K13YET5rBO5BC7S0')


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='5189882159:AAHYGO_ZbfB16aGO2Q0K13YET5rBO5BC7S0', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)  

updater.start_polling()  
