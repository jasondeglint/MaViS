import os
from datetime import datetime
import cv2
import numpy as np


IN_FOLDER = '/home/bll/output5/'
OUT_FOLDER = '/home/bll/archive/'

def write_video(video_file, IN_FOLDER, frames):
    img = cv2.imread(IN_FOLDER + frames[0])
    height, width, layers = img.shape
    img_size = (width,height)

    out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'DIVX'), 15, img_size)
    for frame in frames:
        img = cv2.imread(IN_FOLDER + frame)
        out.write(img)
    out.release()


dt = datetime.now()
files = os.listdir(IN_FOLDER)
files.sort()
image_file = files[int(len(files)/2)]
video_file = OUT_FOLDER + dt.strftime("%Y-%m-%d_%H-%M-%S") + '_video.avi'


print(image_file)
print(video_file)

write_video(video_file, IN_FOLDER, files)