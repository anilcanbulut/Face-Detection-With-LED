# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import RPi.GPIO as GPIO

GPIO.setwarnings(False) #To avoid all warnings
GPIO.setmode(GPIO.BCM) #Setting of the GPIO board mode

#GPIO pin definition
GPIO.setup(17, GPIO.OUT)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))
 
# To warm up your camera
time.sleep(0.1)

#Define your Cascade Classifier, I've directly used my directory so you should change it.
face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/OpenCv Turtorials/haarcascade-frontalface-default.xml')

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    image = frame.array
    
    #Converting the image color to gray, this makes things easy
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Lets find the faces    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #Our LED will start to light
    GPIO.output(17, GPIO.HIGH)
      
    for (x,y,w,h) in faces:
        
        #This line will draw rectangles for each of the faces.
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        
        #When we draw a rectangle, our LED will die.
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.5)  # wait some time
    
    #Start to light it again
    GPIO.output(17, GPIO.HIGH)
    # show the frame
    cv2.imshow("Frame", image)
    
     
    
        

