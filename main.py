from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
import json


wiotoken_IOT = '633ace289df8cbff87d400063e1d6bc0'

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'xin chao {update.effective_user.first_name}')

def on(update: Update, context: CallbackContext) -> None:
    r = requests.post("https://cn.wio.seeed.io/v1/node/GenericDOutD0/onoff/1?access_token="+wiotoken_IOT)
    update.message.reply_text(f' on')
def off(update: Update, context: CallbackContext) -> None:
    r = requests.post("https://cn.wio.seeed.io/v1/node/GenericDOutD0/onoff/0?access_token="+wiotoken_IOT)
    update.message.reply_text(f'off')

def nhietdo(update: Update, context: CallbackContext) -> None:
    TempSensor_Url =  "https://cn.wio.seeed.io/v1/node/GroveTempHumD1/temperature?access_token="+wiotoken_IOT
    tempReading = requests.get(TempSensor_Url)
    if tempReading.status_code == 200:
        tempReading = json.loads(tempReading.text)
        tempReading = tempReading['celsius_degree']
        update.message.reply_text(f'Nhietdo:' + str(tempReading) + ' °C')
    else:
        update.message.reply_text(f'Chua co nhiet do')

def doam(update: Update, context: CallbackContext) -> None:
    doam_url= "https://cn.wio.seeed.io/v1/node/GroveTempHumD1/humidity?access_token="+wiotoken_IOT
    doam = requests.get(doam_url)
    if doam.status_code == 200:
        doam= json.loads(doam.text)
        doam = doam['humidity']
        update.message.reply_text(f'Do am la:' + str(doam) + ' %')
    else:
        update.message.reply_text(f'Cua doc duoc do am')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Cach lenh:\n\nHello: /hello\nInformation: /info \nNhiet Do: /nhietdo\nDo am dat:/doam\nOn Red Light: /on\nOff Red Light: /off\nDo Am Dat:/moisture\nOnVibrationMotor: /onvibmotor\nOffVibrationMotor: /offvibmotor')
def moisture(update: Update, context: CallbackContext) -> None:
    m = requests.get("https://cn.wio.seeed.io/v1/node/GroveMoistureA0/moisture?access_token=" + wiotoken_IOT)
    if m.status_code == 200:
        m = json.loads(m.text)
        m = m['moisture']
        farstr = "Moisture : " + str(m) + ' %'
        update.message.reply_text(f'{farstr}')
    else:
        update.message.reply_text(f'khong hien thi do am dat')

def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Nhom 1: \nNguyen Van Tam Mssv:19146384 \nLe Quang Chien Mssv:19146310 \nNguyen Anh Quoc Mssv 19146380')


def onvib(update: Update, context: CallbackContext) -> None:
    r = requests.post("https://cn.wio.seeed.io/v1/node/GenericPWMOutD2/pwm/50?access_token="+wiotoken_IOT)
    update.message.reply_text(f'OnVibrationMotor')
def offvib(update: Update, context: CallbackContext) -> None:
    r = requests.post("https://cn.wio.seeed.io/v1/node/GenericPWMOutD2/pwm/0?access_token="+wiotoken_IOT)
    update.message.reply_text(f'OffVibrationMotor')


updater = Updater('5354867750:AAGz-aBecCDNx_bkrm-wSz6mWwvFfhEALIM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('on', on))
updater.dispatcher.add_handler(CommandHandler('off', off))
updater.dispatcher.add_handler(CommandHandler('nhietdo', nhietdo))
updater.dispatcher.add_handler(CommandHandler('doam', doam))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('moisture', moisture))
updater.dispatcher.add_handler(CommandHandler('onvibmotor',onvib))
updater.dispatcher.add_handler(CommandHandler('offVibmotor',offvib))
updater.start_polling()
updater.idle()