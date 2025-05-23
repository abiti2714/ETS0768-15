# Gesture Volume Control Part
import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################
wCam, hCam = 640, 480
################################
# This portion of the code is responsible for testing up to 3 camera indices to find an available
# camera. It iterates through the camera indices (0, 1, 2) and attempts to open a capture object using
# `cv2.VideoCapture(cam_index)`. If the camera at a particular index is successfully opened
# (`cap.isOpened()` returns True), it prints a message indicating that the camera was found at that
# index and sets `camera_found` to True.
print("Testing camera indices...")
camera_found = False
for cam_index in range(3):  # Test up to 3 camera indices
    cap = cv2.VideoCapture(cam_index)
    if cap.isOpened():
        print(f"Camera found at index {cam_index}")
        camera_found = True
        break
    else:
        print(f"Camera not found at index {cam_index}")
if not camera_found:
    print("Error: Camera not accessible. Please check your camera connection or index.")
    exit()

# Set camera resolution
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

# Initialize hand detector
detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# Initialize audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255, 0, 0)
# This part of the code is the main loop that runs continuously to capture frames from the camera,
# process hand gestures, and control the volume based on the hand gestures detected.

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture frame")
        continue

    # Find Hand
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList) != 0:

        # Filter based on size
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        if 250 < area < 1000:

            # Find Distance between index and Thumb
            length, img, lineInfo = detector.findDistance(4, 8, img)

            # Convert Volume
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])

            # Reduce Resolution to make it smoother
            smoothness = 10
            volPer = smoothness * round(volPer / smoothness)

            # Check fingers up
            fingers = detector.fingersUp()

            # If pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    # Drawings
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
    cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, colorVol, 3)

    # Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
