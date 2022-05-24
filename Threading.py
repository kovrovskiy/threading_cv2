# -*- coding: utf-8 -*-

import cv2
import threading

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print ("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)

    while (cam.isOpened()):
        rval, frame = cam.read()
        if not rval:
          break
        else:
          frame_rz = cv2.resize(frame, (640,480))
          cv2.imshow(previewName, frame_rz)
          rval, frame = cam.read()
          key = cv2.waitKey(20)
          if key == 27:  # exit on ESC
              break
    cv2.destroyWindow(previewName)

# Create two threads as follows
thread1 = (camThread("Camera 1", "rtsp://user:password@ip:554")).start()
thread2 = (camThread("Camera 2", "rtsp://user:password@ip:554")).start()