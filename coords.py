import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import numpy
from game import *
from tkinter import *
from construction import *

def get_landmarks():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    WIDTH = 600
    HEIGHT = 600
    root = Tk() 
    C = Canvas(root, bg = "black",height = HEIGHT, width = WIDTH)
    C.pack()

    capture = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose :
        while(capture.isOpened()) :
            ret , frame = capture.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            result = pose.process(image)

            try :
                landmarks = result.pose_landmarks.landmark
                coordinates = {"Nose" : [WIDTH *landmarks[0].x,HEIGHT*landmarks[0].y] , "Left-Shoulder" : [WIDTH *landmarks[11].x,HEIGHT*landmarks[11].y] , "Right-Shoulder" : [WIDTH *landmarks[12].x,HEIGHT*landmarks[12].y] , "Left-Elbow" : [WIDTH *landmarks[13].x,HEIGHT*landmarks[13].y] , "Right-Elbow" : [WIDTH *landmarks[14].x,HEIGHT*landmarks[14].y] , "Left-Wrist" : [WIDTH *landmarks[15].x,HEIGHT*landmarks[15].y] , "Right-Wrist" : [WIDTH *landmarks[16].x,HEIGHT*landmarks[16].y], "Left-Hip" : [WIDTH *landmarks[23].x,HEIGHT*landmarks[23].y], "Right-Hip" : [WIDTH *landmarks[24].x,HEIGHT*landmarks[24].y], "Left-Knee" : [WIDTH *landmarks[25].x,HEIGHT*landmarks[25].y], "Right-Knee" : [WIDTH *landmarks[26].x,HEIGHT*landmarks[26].y], "Left-Ankle" : [WIDTH *landmarks[27].x,HEIGHT*landmarks[27].y], "Right-Ankle" : [WIDTH *landmarks[28].x,HEIGHT*landmarks[28].y] , "Left-Sword" : [0,0] , "Right-Sword" : [0,0]}
                Make_Canvas(C,coordinates,root)
            except :
                pass

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)

            cv2.imshow("Mediapipe Feed" , image)

            if cv2.waitKey(10) & 0xFF == ord('q') :
                break


    capture.release()
    cv2.destroyAllWindows()
    return landmarks

get_landmarks()