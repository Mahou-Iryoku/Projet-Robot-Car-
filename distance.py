import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trigger = 21
echo = 20
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(trigger,False) # Initialiation du Trigger à 0
time.sleep(0.1)
#Vérifie si le robot détecte un obstacle
GPIO.output(trigger,True)
time.sleep(0.00001) #On attend 100 ms d'impulsion
GPIO.output(trigger,False)  
while GPIO.input(echo)==0:
    debutImpulsion = time.time()
    
while GPIO.input(echo)==1:
    finImpulsion = time.time()
distance = (finImpulsion - debutImpulsion)*343*100/2
#340 correspond à 340 m/s de vitesse du son et on multiplie par 100 pour convertir en cm/s 
print("Distance en cm :",distance)
