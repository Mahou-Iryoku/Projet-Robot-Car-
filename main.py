# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
PIN1_M1 = 17
PIN2_M1 = 27
PIN1_M2 = 23
PIN2_M2 = 24
PIN1_M3 = 25
PIN2_M3 = 8
PIN1_M4 = 7
PIN2_M4 = 1
trigger = 21
echo = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN1_M1,GPIO.OUT)
GPIO.setup(PIN2_M1,GPIO.OUT)

GPIO.setup(PIN1_M2,GPIO.OUT)
GPIO.setup(PIN2_M2,GPIO.OUT)

GPIO.setup(PIN1_M3,GPIO.OUT)
GPIO.setup(PIN2_M3,GPIO.OUT)

GPIO.setup(PIN1_M4,GPIO.OUT)
GPIO.setup(PIN2_M4,GPIO.OUT)

GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def avancer():
    
    GPIO.output(PIN1_M1,GPIO.HIGH) 
    GPIO.output(PIN2_M1,GPIO.LOW)
            
    GPIO.output(PIN1_M2,GPIO.LOW)
    GPIO.output(PIN2_M2,GPIO.HIGH)
            
    GPIO.output(PIN1_M3,GPIO.LOW)
    GPIO.output(PIN2_M3,GPIO.HIGH)
            
    GPIO.output(PIN1_M4,GPIO.HIGH)
    GPIO.output(PIN2_M4,GPIO.LOW)
  
    print('Avancer')
   
def reculer():

    GPIO.output(PIN1_M1,GPIO.LOW) 
    GPIO.output(PIN2_M1,GPIO.HIGH)
    
    GPIO.output(PIN1_M2,GPIO.HIGH)
    GPIO.output(PIN2_M2,GPIO.LOW)
    
    GPIO.output(PIN1_M3,GPIO.HIGH)
    GPIO.output(PIN2_M3,GPIO.LOW)
    
    GPIO.output(PIN1_M4,GPIO.LOW)
    GPIO.output(PIN2_M4,GPIO.HIGH)
    print('Reculer')
def arret():
    
    GPIO.output(PIN1_M1,GPIO.LOW) 
    GPIO.output(PIN2_M1,GPIO.LOW)
    
    GPIO.output(PIN1_M2,GPIO.LOW)
    GPIO.output(PIN2_M2,GPIO.LOW)
    
    GPIO.output(PIN1_M3,GPIO.LOW)
    GPIO.output(PIN2_M3,GPIO.LOW)
    
    GPIO.output(PIN1_M4,GPIO.LOW)
    GPIO.output(PIN2_M4,GPIO.LOW)

    print('Arret')

def tourner_droite():
    
    GPIO.output(PIN1_M1,GPIO.HIGH) 
    GPIO.output(PIN2_M1,GPIO.LOW)
    
    GPIO.output(PIN1_M2,GPIO.LOW)
    GPIO.output(PIN2_M2,GPIO.LOW)

    GPIO.output(PIN1_M3,GPIO.LOW)
    GPIO.output(PIN2_M3,GPIO.LOW)
    
    GPIO.output(PIN1_M4,GPIO.HIGH)
    GPIO.output(PIN2_M4,GPIO.LOW)
    
    print('Reculer a droite')

def tourner_gauche():
    
    GPIO.output(PIN1_M1,GPIO.LOW) 
    GPIO.output(PIN2_M1,GPIO.LOW)
    
    GPIO.output(PIN1_M2,GPIO.LOW)
    GPIO.output(PIN2_M2,GPIO.HIGH)
    
    GPIO.output(PIN1_M3,GPIO.LOW)
    GPIO.output(PIN2_M3,GPIO.HIGH)
    
    GPIO.output(PIN1_M4,GPIO.LOW)
    GPIO.output(PIN2_M4,GPIO.LOW)

    print('Reculer a gauche')

def reculer_droite():

    GPIO.output(PIN1_M1,GPIO.LOW) 
    GPIO.output(PIN2_M1,GPIO.HIGH)
    
    GPIO.output(PIN1_M2,GPIO.LOW)
    GPIO.output(PIN2_M2,GPIO.LOW)
    
    GPIO.output(PIN1_M3,GPIO.LOW)
    GPIO.output(PIN2_M3,GPIO.LOW)
    
    GPIO.output(PIN1_M4,GPIO.LOW)
    GPIO.output(PIN2_M4,GPIO.HIGH)
    print('Reculer a droite')

def reculer_gauche():

    GPIO.output(PIN1_M1,GPIO.LOW) 
    GPIO.output(PIN2_M1,GPIO.LOW)
    
    GPIO.output(PIN1_M2,GPIO.HIGH)
    GPIO.output(PIN2_M2,GPIO.LOW)
    
    GPIO.output(PIN1_M3,GPIO.HIGH)
    GPIO.output(PIN2_M3,GPIO.LOW)
    
    GPIO.output(PIN1_M4,GPIO.LOW)
    GPIO.output(PIN2_M4,GPIO.LOW)

    print('Reculer a gauche')
    
    time.sleep()
    
arret()
count = 0
while True:
    i= 0
    moy_dist=0
    for i in range(5):
        GPIO.output(trigger,False)
        time.sleep(0.1)
        GPIO.output(trigger,True)
        time.sleep(0.00001)
        GPIO.output(trigger,False)

    while GPIO.input(echo)== 0:
        debutImpulsion = time.time()
    
    while GPIO.input(echo)== 1:
        finImpulsion = time.time()

    Impulsion = finImpulsion - debutImpulsion
    distance = Impulsion*343*100/2
    moy_dist = moy_dist + distance
    print("Distance moyenne:",moy_dist)
    
    flag = 0
    if moy_dist < 30 :
        count = count + 1
        arret()
        time.sleep(1)
        reculer()
        time.sleep(0.5)
        if (count%3==1)& (flag==0):
            tourner_droite()
            flag = 1
        else:
            tourner_gauche()
            flag = 0
        time.sleep(1.5)
        arret()
        time.sleep(1)
    else:
        avancer()
        flag = 0

def Camera():
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
 camera.start_recording('/home/pi/Documents/PROJET_Robot_2021_2022/test.h264')
    time.sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    print('Camera activé')

thread_1 = Thread(target=measure)
thread_2 = Thread(target=Camera)

thread_1.start()
time.sleep(1)
thread_1.join()
thread_2.start()
time.sleep(1)
thread_2.join()
