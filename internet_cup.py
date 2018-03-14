import RPi.GPIO as GPIO
import time
from ISStreamer.Streamer import Streamer
streamer = Streamer(bucket_name="Button", bucket_key="c546889e-581d-4792-8b47-e5cc5a18e034", access_key="lKYKeIMQwxTIuhfZmrNDQS4bUDRVBTty")
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    first = GPIO.input(18)
    second = GPIO.input(23)
    third = GPIO.input(24)
    forth = GPIO.input(12)
    if first == False:
        print('Button 1 Pressed')
        streamer.log("Level", "Empty")
        streamer.log("Fluid Level", "1")
        time.sleep(0.2)
    elif second == False:
        print ("Button 2 Pressed")
        streamer.log("Level", "1/4")
        streamer.log("Fluid Level", "2")
        time.sleep(0.2)
    elif third == False:
        print("Button 3 Pressed")
        streamer.log("Level", "3/4")
        streamer.log("Fluid Level", "3")
        
        time.sleep(0.2)
    elif forth == False:
        print ("Button 4 Pressed")
        streamer.log("Level", "Full")
        streamer.log("Fluid Level", "4")
        time.sleep(0.2)
