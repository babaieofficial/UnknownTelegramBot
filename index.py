import os
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
            bot.sendMessage(chat_id,"خوش اومدی این ربات برای دکتر ببعی هست، هرپیامی که میخوای برای دکتر بفرست اون بدون اینکه بدونه میبینه و جوابت رو میده.",reply_to_message_id=msg['message_id'])
        else:
            try:
                bot.sendMessage(user_id,msg['text'])
                user_id=None
            except NameError:
                bot.sendMessage('YOURCHATID',msg['text'],reply_markup=keyboard)

    elif content_type == 'photo':
        temp=f"Img{(str(time.time()).replace('.', ''))}.png"
        bot.download_file(msg['photo'][-1]['file_id'],temp)
        if 'caption' in msg:
            try:
                bot.sendPhoto(user_id,open(temp,'rb'),caption=msg['caption'])
                user_id = None
            except NameError:
                bot.sendPhoto('YOURCHATID',open(temp,'rb'),caption=msg['caption'], reply_markup=keyboard)
        else:
            try:
                bot.sendPhoto(user_id,open(temp,'rb'))
                user_id = None
            except NameError:
                bot.sendPhoto('YOURCHATID',open(temp,'rb'), reply_markup=keyboard)
        os.remove(temp)
    elif content_type == 'document':
        type=str(msg['document']['file_name']).split(".")
        temp=f"Doc{(str(time.time()).replace('.', ''))}."+type[len(type)-1]
        bot.download_file(msg['document']['thumb']['file_id'], temp)
        if 'caption' in msg:
            try:
                bot.sendDocument(user_id,open(temp,'rb'),caption=msg['caption'])
                user_id = None
            except NameError:
                bot.sendDocument('YOURCHATID',open(temp,'rb'),caption=msg['caption'], reply_markup=keyboard)
        else:
            try:
                bot.sendDocument(user_id,open(temp,'rb'))
                user_id = None
            except NameError:
                bot.sendDocument('YOURCHATID',open(temp,'rb'), reply_markup=keyboard)
        os.remove(temp)
    elif content_type == 'video':
        temp=f"Doc{(str(time.time()).replace('.', ''))}.mp4"
        bot.download_file(msg['video']['thumb']['file_id'], temp)
        if 'caption' in msg:
            try:
                bot.sendVideo(user_id,open(temp,'rb'),caption=msg['caption'])
                user_id = None
            except NameError:
                bot.sendVideo('YOURCHATID',open(temp,'rb'),caption=msg['caption'], reply_markup=keyboard)
        else:
            try:
                bot.sendVideo(user_id,open(temp,'rb'))
                user_id = None
            except NameError:
                bot.sendVideo('YOURCHATID',open(temp,'rb'), reply_markup=keyboard)
        os.remove(temp)
    elif content_type == 'voice':
        temp=f"Doc{(str(time.time()).replace('.', ''))}.mp3"
        bot.download_file(msg['voice']['file_id'], temp)
        try:
            bot.sendVoice(user_id,open(temp,'rb'))
        except NameError:
            bot.sendVoice('YOURCHATID',open(temp,'rb'), reply_markup=keyboard)
        os.remove(temp)
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
            bot.sendMessage(from_id,'باتشکر از ارسال پیام برای دکترببعی\n پیام شما مشاهده شد.')


bot = telepot.Bot('YOURTOKEN')
MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread()

while 1:
    time.sleep(60)
