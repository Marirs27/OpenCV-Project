import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def Calculate_angle (a,b,c) :
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(radians*180/np.pi)

    if (angle>180) :
        angle = 360-angle

    return angle

elbow_angles = []
knee_angles = []
capture = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose :
    while(capture.isOpened()) :
        ret , frame = capture.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        result = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # try :
        #     landmarks = result.pose_landmarks.landmark
        # except :
        #     pass

        # shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        # elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]       
        # wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        # hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
        # knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]       
        # ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

        # angle = Calculate_angle(shoulder,elbow,wrist)
        # angle2 = Calculate_angle(hip,knee,ankle)

        # elbow_angles.append(angle)
        # knee_angles.append(angle2)

        # x,y,w,h = 0,0,500,60
        # cv2.rectangle(image, (x, x), (x + w, y + h), (0,0,0), -1)
        # cv2.putText(image, "ELBOW ANGLE : " + str(angle) , (x + int(w/10),y + int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        # x += 550
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), -1)
        # cv2.putText(image, "KNEE ANGLE : " + str(angle2) , (x + int(w/10),y + int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
     
        mp_drawing.draw_landmarks(image,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)

        cv2.imshow("Mediapipe Feed" , image)

        if cv2.waitKey(10) & 0xFF == ord('q') :
            break

capture.release()
cv2.destroyAllWindows()
