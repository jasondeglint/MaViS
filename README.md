![](/media/mavis_logo.png)

# Background

The MaViS (**Ma**chine **Vi**sion **S**ecurity) system is an machine learning based security platform that automatically monitors and detects people in a scene, and then alerts the user in real time by sending an image and video to their email. The system is enabled through a combination of edge computing and cloud infrastructure. The edge platform used was the Nvidia Jetson Nano 4GB Developer Kit, and the cloud infrastructure was built using Amazon Web Services (AWS).

<img src="/media/overview.png" width=600>

# MaViS Public Code

This repository only contains the details and code to setup the Nvidia Jetson Nano.

Additional resources include:
1. A [short report]() including a description of the Jetson Nano and AWS setup.
2. A [video demo]() and overview of the MaViS sytem.

Setting up the Jetson Nano includes the following steps:
1. Install JetPack 4.5.1
2. Install DeepStream SDK 5.1
3. Install MaViS
4. Setup AWS Connection (optional)
5. Run MaViS

# Install JetPack 4.5.1

# Install DeepStream SDK 5.1

# Install MaViS

# Setup AWS Connection (Optional)


Setup:

```
$ sudo apt install python3-pip
$ pip3 install boto3
$ pip3 install awscli --upgrade --user
```


To setup AWS:
`$  python3 -m awscli configure`

This will create a `credentials` file in the `~/.aws` folder.


To check:

```
$ pip3 install awscli --upgrade --user
```

# Run MaViS

<img src="/media/jetson_code.png" width=600>

To run the test app:

`$ python3 main.py <v4l2-device-path> <folder-name>`

Example:

`$ python3 main.py /dev/video0 ~/output`
