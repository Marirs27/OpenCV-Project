import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import numpy

def get_landmarks():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    capture = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose :
        while(capture.isOpened()) :
            ret , frame = capture.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            result = pose.process(image)

            try :
                landmarks = result.pose_landmarks.landmark
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