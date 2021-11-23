from telegram.ext import Updater

def start(bot,update):
    update.message.reply_text("Saya bot. Hallo")

def main():
    updater = Updater(token='2122370052:AAHMT20jJMvre-0dOlZ_xV0rMYbqRVJ78-M')
    dispatcher = updater.dispatcher
    print("bot started")

if __name__=='__main__':
    main()
