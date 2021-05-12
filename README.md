# Machine Vision Security (MaViS) System

 **Ma**chine **Vi**sion **S**ecurity (MaViS) System

prerequisite:
- DeepStreamSDK 5.1
- Python 3.6
- Gst-python


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



To run the test app:

`$ python3 main.py <v4l2-device-path> <folder-name>`

Example:

`$ python3 main.py /dev/video0 ~/output`
