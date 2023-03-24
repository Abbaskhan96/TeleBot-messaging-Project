try:
    import telegram 
    from telegram.ext.messagehandler import MessageHandler
    from telegram.ext.updater import Updater
    from telegram.ext import Filters
    
except:
    raise("Library not Found")



bot = telegram.Bot(token='5956943698:AAFOuVmPA_Jz6PbjZMFmBCk0ZNikYW0HYFg')

def get_group_id():
    a=[]
    with open("C:/Users/DELL/Desktop/python/TelegramMsg_Bot/Bot/BotRepo/group_id.txt") as file:
        for line in file:
            a.append(line.rstrip())
            #print(a)
        print(a)
        return a



def user_data(update, context):

    user = update.message.from_user
    name = user.first_name + ' ' + user.last_name if user.last_name else user.first_name
    username = user.username or ''
    if user.first_name and user.last_name:
        message = f'{name} (@{username}): {update.message.text}'
    else:
        message = f'@{name}: {update.message.text}'

    # Forward the message to the defined groups
    groups= get_group_id()
    for group in groups:
        bot.send_message(chat_id=group, text=message)



bot_message_handler = MessageHandler(Filters.text & (~Filters.command), user_data)
updater = Updater(token='5956943698:AAFOuVmPA_Jz6PbjZMFmBCk0ZNikYW0HYFg')

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher
dispatcher.add_handler(bot_message_handler)
updater.start_polling()
print("success...")
