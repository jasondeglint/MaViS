import os
from datetime import datetime
import cv2
import numpy as np
import time
import boto3

from upload_data import upload_file


IN_FOLDER = '/home/bll/output4/'
OUT_FOLDER = '/home/bll/archive/'

def write_video(IN_FOLDER, frames, video_file):
    img = cv2.imread(IN_FOLDER + frames[0])
    height, width, layers = img.shape
    img_size = (width,height)

    out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'DIVX'), 15, img_size)
    for frame in frames:
        img = cv2.imread(IN_FOLDER + frame)
        out.write(img)
    out.release()

s3_client = boto3.client('s3')
metadata = {
    "sender": "jason@bluelionlabs.com",
    "receiver": "jason@bluelionlabs.com   juan@bluelionlabs.com"
}

reset = True

while True:

    if reset:
        all_files = []
        start = datetime.now()
        reset = False
        new_scene = True

    files = os.listdir(IN_FOLDER)
    new_files = list(set(files) - set(all_files))
    

    print('files :    ', files)
    print('new files: ', new_files)

    # check if we have new files or not
    if new_files:     
        print("adding files")
        all_files.extend(new_files)
        print(all_files)
        print('all files: ', all_files)
        time.sleep(0.01)     

        if new_scene:
            image_input_file = IN_FOLDER + all_files[int(len(files)/2)]
            image = cv2.imread(image_input_file)
            image_ouput_file = OUT_FOLDER + start.strftime("%Y-%m-%d_%H-%M-%S") + '_image.jpg'
            cv2.imwrite(image_ouput_file, image)
            new_scene = False

            #TODO: write image_ouput_file to S3
            print('Connecting to client...')            
            upload_file(s3_client, image_ouput_file, metadata=metadata)

    else:
        print('no new files')
        time.sleep(0.01)

        # if we have no new files and it's been longer than 3 seconds
        if ((datetime.now() - start).total_seconds() > 4): # if less than 3 seconds have passed and we have new files
            if all_files:
                video_output_file = OUT_FOLDER + start.strftime("%Y-%m-%d_%H-%M-%S") + '_video.avi'
                write_video(IN_FOLDER, all_files, video_output_file)

                # TODO: write video_output_file to S3
                print('Connecting to client...')
                upload_file(s3_client, video_output_file, metadata=metadata)
                
            # remove all previous images
            print('deleting files')
            for file in all_files:
                new_files.sort()
                os.remove(IN_FOLDER+file)
            reset = True






'''
if there are no photos after x seconds
then write a video to s3

'''

'''
if files: # files will be True if list is not empty
    dt = datetime.now()
    files = os.listdir(IN_FOLDER)
    files.sort()
    image_file = IN_FOLDER + files[int(len(files)/2)]
    video_file = OUT_FOLDER + dt.strftime("%Y-%m-%d_%H-%M-%S") + '_video.avi'
    write_video(video_file, IN_FOLDER, files)
    print(image_file)
    print(video_file)
'''