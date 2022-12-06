#from turtle import title
import schedule     
import telebot
import time
from youtube.parsejson import pJson as pj
## глобальные переменные
from configglobal import tokenTelegram as tokT
from configglobal import TestChannelTelegram as tct
from configglobal import startTime as stT
global sendChat
global tokentelegram
tokentelegram = tokT()
# Создаем экземпляр бота
bot = telebot.TeleBot(tokentelegram)
# Адрес телеграм-канала
#test channel id
CHANNEL_NAME = str(tct())
# Функция, обрабатывающая команду /gobot
@bot.message_handler(commands=["gobot"])
def start(m, res=False):
     bot.send_message(m.chat.id, 'Всем привет! Приступаю к своим обязанностям.')
 # Отправка сообщения в телеграмм чат    
def sendNewVideo():
    sendMessage =pj()
    print(sendMessage)
    if not(sendMessage=="Публикаций не обнаружено"):
        bot.send_message(tct(), sendMessage)
schedule.every().day.at(str(stT())).do(sendNewVideo)
while True:
    schedule.run_pending()
    time.sleep(1)   
# Запускаем бота
bot.polling(none_stop=True, interval=0)    
