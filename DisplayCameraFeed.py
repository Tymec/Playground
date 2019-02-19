import cv2
import numpy as np

# Requires a separate file with cam1-cam6 defined
from helpers import cameras

while(1):
    ret, cam1_frame = cam1.read()
    cam1_frame = cv2.resize(cam1_frame, (480, 270))
    ret, cam2_frame = cam2.read()
    cam2_frame = cv2.resize(cam2_frame, (480, 270))
    ret, cam3_frame = cam3.read()
    cam3_frame = cv2.resize(cam3_frame, (480, 270))
    ret, cam4_frame = cam4.read()
    cam4_frame = cv2.resize(cam4_frame, (480, 270))
    ret, cam5_frame = cam5.read()
    cam5_frame = cv2.resize(cam5_frame, (480, 270))
    ret, cam6_frame = cam6.read()
    cam6_frame = cv2.resize(cam6_frame, (480, 270))
    
    axis1 = np.concatenate((cam1_frame, cam2_frame, cam3_frame), axis=1)
    axis2 = np.concatenate((cam4_frame, cam5_frame, cam6_frame), axis=1)
    final_frame = np.concatenate((axis1, axis2), axis=0)

    cv2.imshow('CAMERA FEED', final_frame)
    cv2.waitKey(1)
