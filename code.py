import telepot
import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
from telepot.loop import MessageLoop
import signal
from picamera import PiCamera

#nomor pin di raspberry pi yang digunakan
switch = 23
PIR = 24

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIR, GPIO.IN)

door = 0
door2 = 0
motion = 0
i = 0
 
def handle(msg):
    global telegramText
    global chat_id
  
    chat_id = msg['chat']['id']
    telegramText = msg['text']
  
    print('Message received from ' + str(chat_id))
  
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Selamat Datang Di Rumah Ant')
        bot.sendMessage(chat_id, 'stream at ip+port')
    while True:
        main()
        

bot = telepot.Bot('token telegram')
bot.message_loop(handle)		

def main():
	    
    global chat_id
    global door 
    global door2
    global motion

    if GPIO.input(switch) == True :
        door = 1
        if door2 != door:
            door2 = door
            sendNotification(door)
        time.sleep(0.1)
            
    elif GPIO.input(switch) == False:
        door = 0
        if door2 != door:
            door2 = door
            sendNotification(door)
        time.sleep(0.1)
    
    if GPIO.input(PIR) == 1:
        motion = 1
        if motion == 1:
            capture()
            sendPhoto(motion)
        time.sleep(0.1)

def sendNotification(door):   

    global chat_id
    
    if door == 1:
        bot.sendMessage(chat_id, 'Ada orang membuka pintu tanpa izin tuan, segera lapor RT atau kerabat terdekat !!')
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
        
    elif door != 1:
        bot.sendMessage(chat_id, 'Pintu tertutup rapat')

def sendPhoto(motion):
    global chat_id

    if motion == 1:
        bot.sendPhoto(chat_id,photo=open('/image_%s.jpg' %i,'rb'))

   
def capture():

    global i
    i = i + 1
    
    camera = PiCamera()
    camera.vflip = True
    camera.resolution = (1024, 768)
    camera.start_preview()
    #warm up camera
    sleep (1)
    camera.capture('/image_%s.jpg' %i)
    camera.close()
