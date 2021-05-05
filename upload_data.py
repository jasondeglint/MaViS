import boto3, logging, os, threading, sys
from botocore.exceptions import ClientError


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()



def upload_file(s3_client, file_name, bucket='fsdl-simple-bucket', object_name=None, metadata=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if metadata is None:
        metadata = {}

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'Metadata': metadata}, Callback=ProgressPercentage(file_name))
        print()
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    print('Connecting to client...')
    s3_client = boto3.client('s3')
    upload_file(s3_client, "inputs/input1.jpg")