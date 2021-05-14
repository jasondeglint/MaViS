![](/media/mavis_logo.png)
![](/media/mavis_demo.gif)

# Background

The MaViS (**Ma**chine **Vi**sion **S**ecurity) system is a machine learning based security platform that automatically monitors and detects people in a scene, and then alerts the user in real time by sending an image and video to their email. The system is enabled through a combination of edge computing and cloud infrastructure. The edge platform used was the Nvidia Jetson Nano 4GB Developer Kit, and the cloud infrastructure was built using Amazon Web Services (AWS).

<img src="/media/overview.png" width=600>

# Project History

This project is a final deliverable for the [Full Stack Deep Learning](https://fullstackdeeplearning.com/) course. 

When implementing the edge component the project went through three interations. This repository only contains the code of the Nvidia Jetson Nano used in the final version of the project.

![](/media/project_history.png)

# Full Project Details

A [short report]() is available that includes:
1. A more detailed project history.
2. A description of the engineering design.
3. The process of setting up both Jetson Nano and AWS.

[A full video demo and project explanation can be found here.](https://youtu.be/UVe5LXdPUYs) 

# Setting up Nvidia Jetson Nano

This repository only contains the details and code to setup the Nvidia Jetson Nano and run the MaViS software.

Setting up the Jetson Nano includes the following steps:
1. Install JetPack 4.5.1
2. Install DeepStream SDK 5.1
3. Install MaViS
4. Setup AWS Connection (optional)
5. Run MaViS

## 1. Install JetPack 4.5.1

To install JetPack 4.5.1, please follow the [instructions here](https://docs.nvidia.com/jetson/jetpack/install-jetpack/index.html).

## 2. Install DeepStream SDK 5.1

To install DeepStream SDK 5.1, plese follow the [instructions here](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Quickstart.html).

## 3. Install MaViS

To install MaViS clone this repository:

`$ git clone https://github.com/jasondeglint/MaViS.git`


## 4. Setup AWS Connection (optional)

To setup AWS run the following commands:

```
$ sudo apt install python3-pip
$ pip3 install boto3
$ pip3 install awscli --upgrade --user
```

To setup your login credentials run the following command:

`$  python3 -m awscli configure`

This will create a `credentials` file in the `~/.aws` folder.


To check that the install and credentials are working, run:

```
$ pip3 install awscli --upgrade --user
```

## 5. Run MaViS

The Python code for the Nvidia Jetson contains two scripts: 
1. `The main.py` script monitors the video stream and automatically saves frames that contain a positive classification. 
2. The `monitor_and_upload.py` script uploads a sample image as soon as an intruder enters a scene, and then also uploads a video once the intruder leaves the scene.

<img src="/media/jetson_code.png" width=600>

To properly run the entire system you must run both scripts at the same in two separate terminals.

### Video Streaming & Inference using DeepStream

To run the DeepStream code:

`$ python3 main.py <v4l2-device-path> <output-folder-name>`

For example:

`$ python3 main.py /dev/video0 ~/images`

### Monitor & Archive

To run the montoring code:

`$ python3 monitor_and_upload.py <input-folder-name> <archive-folder-name> UPLOAD_TO_AWS`

Where, `UPLOAD_TO_AWS` is a boolean.

For example:

`$ python3 monitor_and_upload.py ~/images ~/archive True`

# To Do
1. autocreate folders if they don't exist
2. add a flag to upload to AWS
3. check that the CLI inputs are correct

