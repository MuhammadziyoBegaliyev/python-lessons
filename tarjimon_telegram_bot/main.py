from translate import translate
import telebot 
TOKEN = "7975356285:AAEtEG5Hi1KOXB4xko2np2R0Bt3mYnkgCEQ"
tarjimonbot = telebot.TeleBot(token=TOKEN)

@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu aleykum , tarjimon botiga hush kelibsiz."
    xabar += '\nMatningizni yuboring.'
    tarjimonbot.reply_to(message, xabar)


@tarjimonbot.message_handler(func=lambda msg: msg. text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))




tarjimonbot.polling()