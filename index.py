import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(':', chat_type, content_type, chat_id)
    global user_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='مشاهده شد', callback_data='see+' + str(chat_id)),
         InlineKeyboardButton(text="جواب دادن", callback_data='sendMsg+' + str(chat_id))]
    ])
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id,"خوش اومدی این ربات برای دکتر ببعی هست، هرپیامی که میخوای برای ییعی بفرست اون بدون اینکه بدونه میبینه و جوابت رو میده.",reply_to_message_id=msg['message_id'])
        else:
            try:
                bot.sendMessage(user_id,msg['text'])
                user_id=None
            except NameError:
                bot.sendMessage('YOURCHATID',msg['text'],reply_markup=keyboard)
    elif content_type == 'photo':
        if 'caption' in msg:
            try:
                bot.sendPhoto(user_id,msg['photo'][-1]['file_id'],caption=msg['caption'])
                user_id = None
            except NameError:
                bot.sendPhoto('YOURCHATID',msg['photo'][-1]['file_id'],caption=msg['caption'], reply_markup=keyboard)
        else:
            try:
                bot.sendPhoto(user_id,msg['photo'][-1]['file_id'])
                user_id = None
            except NameError:
                bot.sendPhoto('YOURCHATID',msg['photo'][-1]['file_id'], reply_markup=keyboard)
    elif content_type == 'document':
        if 'caption' in msg:
            try:
                bot.sendDocument(user_id,msg['document']['thumb']['file_id'],caption=msg['caption'])
                user_id = None
            except NameError:
                bot.sendDocument('YOURCHATID',msg['document']['thumb']['file_id'],caption=msg['caption'], reply_markup=keyboard)
        else:
            try:
                bot.sendDocument(user_id,msg['document']['thumb']['file_id'])
                user_id = None
            except NameError:
                bot.sendDocument('YOURCHATID',msg['document']['thumb']['file_id'], reply_markup=keyboard)
    elif content_type == 'video':
        if 'caption' in msg:
            try:
                bot.sendVideo(user_id,msg['video']['thumb']['file_id'],caption=msg['caption'])
                user_id = None
            except NameError:
                bot.sendVideo('YOURCHATID',msg['video']['thumb']['file_id'],caption=msg['caption'], reply_markup=keyboard)
        else:
            try:
                bot.sendVideo(user_id,msg['video']['thumb']['file_id'])
                user_id = None
            except NameError:
                bot.sendVideo('YOURCHATID',msg['video']['thumb']['file_id'], reply_markup=keyboard)
    elif content_type == 'voice':
        try:
            bot.sendVoice(user_id,msg['voice']['file_id'])
        except NameError:
            bot.sendVoice('YOURCHATID',msg['voice']['file_id'], reply_markup=keyboard)
    else:
        bot.sendMessage(chat_id,"پشتیبانی نمیشود")
    pass

def on_callback_query(msg):
    query_id, from_id,query_data = telepot.glance(msg, flavor='callback_query')
    print(msg)
    print('Callback Query:', query_id, from_id, query_data)
    data=str(query_data).split("+")
    if len(data) > 1:
        if data[0] == 'sendMsg':
            global user_id
            bot.sendMessage(from_id,text="پیام خود را ارسال کنید")
            user_id=data[1]
        else:
            bot.sendMessage(data[1],'باتشکر از ارسال پیام برای دکتر ببعی\n پیام شما مشاهده شد.')

bot = telepot.Bot('YOURTOKEN')
MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread()

while 1:
    time.sleep(60)
