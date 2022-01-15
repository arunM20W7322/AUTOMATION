import cv2
import mediapipe as mp
import os
import RPi.GPIO as GPIO
from time import sleep


drawingModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands

mod=handsModule.Hands()


h=480
w=640


def findpostion(frame1):
    list=[]
    results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
       for handLandmarks in results.multi_hand_landmarks:
           drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
           list=[]
           for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * w)
                y = int(pt.y * h)
                list.append([id,x,y])

    return list            





def findnameoflandmark(frame1):
     list=[]
     results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
     if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:


            for point in handsModule.HandLandmark:
                 list.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
     return list

def on():
    # Sleeping for a second
    sleep(1)
    # We will be using the BCM GPIO numbering
    LED_PIN = 17
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, True)
    sleep(5) # output rfGPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.cleanup() 
def off():
    # Sleeping for a second
    sleep(1)
    # We will be using the BCM GPIO numbering
    LED_PIN = 17
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, False)
    sleep(5) # output rfGPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.cleanup() 

    
