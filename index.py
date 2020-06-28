import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
 

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)
    print(':', chat_type, content_type, chat_id)
    global user_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='مشاهده شد 👀', callback_data='see+' + str(chat_id)),
         InlineKeyboardButton(text="💬جواب دادن", callback_data='sendMsg+' + str(chat_id))]
    ])
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id,"خوش اومدی این ربات هست، هرپیامی که میخوای براش بفرست اون جوابت رو میده.\nببخش اگه زمان میبره تا نتیجه رو ببینی!".format(AccountName),reply_to_message_id=msg['message_id'])
        else:
            if chat_id == UserChatId:
                if user_id != None: 
                    bot.sendMessage(user_id,msg['text'])
                    user_id=None
            else:
                msg_send=bot.sendMessage(UserChatId,msg['text'],reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")

    elif content_type == 'photo':
        if 'caption' in msg:
            if chat_id == UserChatId:
                if user_id != None:
                    bot.sendPhoto(user_id,msg['photo'][-1]['file_id'],caption=msg['caption']) 
                    user_id = None
            else:
                msg_send=bot.sendPhoto(UserChatId,msg['photo'][-1]['file_id'],caption=msg['caption'], reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")
        else:
            if chat_id == UserChatId:
                if user_id != None:
                    bot.sendPhoto(user_id,msg['photo'][-1]['file_id']) 
                    user_id = None
            else:
                msg_send=bot.sendPhoto(UserChatId,msg['photo'][-1]['file_id'], reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")
    elif content_type == 'document':
        if 'caption' in msg:
            if chat_id == UserChatId:
                if user_id != None:
                    bot.sendDocument(user_id,msg['document']['thumb']['file_id'],caption=msg['caption']) 
                    user_id = None
            else:
                msg_send=bot.sendDocument(UserChatId,msg['document']['thumb']['file_id'],caption=msg['caption'], reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")
        else:
            if chat_id == UserChatId:
                if user_id != None:
                    bot.sendDocument(user_id,msg['document']['thumb']['file_id']) 
                    user_id = None
            else:
                msg_send=bot.sendDocument(UserChatId,msg['document']['thumb']['file_id'], reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")
    elif content_type == 'video':
        if 'caption' in msg:
            if chat_id == UserChatId:
                if user_id != None:
                    bot.sendVideo(user_id,msg['video']['thumb']['file_id'],caption=msg['caption']) 
                    user_id = None
            else:
                msg_send=bot.sendVideo(UserChatId,msg['video']['thumb']['file_id'],caption=msg['caption'], reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")
        else:
            if chat_id == UserChatId:
                if user_id != None:
                    bot.sendVideo(user_id,msg['video']['thumb']['file_id']) 
                    user_id = None
            else:
                msg_send = bot.sendVideo(UserChatId, msg['video']['thumb']['file_id'], reply_markup=keyboard) 
                bot.sendMessage(chat_id,"پیام شما ارسال شد.")
    elif content_type == 'voice':
        if chat_id == UserChatId:
            if user_id != None:
                bot.sendVoice(user_id,msg['voice']['file_id']) 
                user_id = None

        else:
            msg_send=bot.sendVoice(UserChatId,msg['voice']['file_id'], reply_markup=keyboard) 
            bot.sendMessage(chat_id,"پیام شما ارسال شد.")
    else:
        bot.sendMessage(chat_id,"پشتیبانی نمیشود")
    pass

def on_callback_query(msg):
    query_id, from_id,query_data = telepot.glance(msg, flavor='callback_query')
    print(msg)
    print('Callback Query:', query_id, from_id, query_data)
    data=str(query_data).split("+")
    if len(data) > 1:
        global user_id
        if data[0] == 'sendMsg':
            bot.sendMessage(from_id,text="پیام خود را ارسال کنید")
            user_id=data[1]
        else:
            bot.sendMessage(data[1],'باتشکر از ارسال پیام برای {0}\n پیام شما مشاهده شد.'.format(AccountName))
            user_id = None


Token = 'ENTER YOUR BOT ID'
UserChatId = "ENTER YOUR CHAT ID"
AccountName = "ENTER YOUR NAME"

global user_id
user_id = None

bot = telepot.Bot(Token)
MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread()


while 1:
    time.sleep(60)
