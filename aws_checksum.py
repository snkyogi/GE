# UPLOAD PART

import boto3
import os
import threading
import sys 

bucket_name = 'xxxx'
file_path = 'data.csv'
key = 'data.csv'

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


s3_resource = boto3.resource('s3')

s3_resource.Object(bucket_name, key).upload_file(file_path,
                        ExtraArgs={'ContentType': 'text/pdf'},
                        Callback=ProgressPercentage(file_path)
                        )


# CHECKSUM VERIFICATION PART
import boto3
import hashlib

bucket = "xxxx"
key = "data.csv"
file_path = 'data.csv'

def calculate_s3_etag(file_path, chunk_size):
    md5s = []

    with open(file_path, 'rb') as fp:
        while True:
            data = fp.read(chunk_size)
            if not data:
                break
            md5s.append(hashlib.md5(data))

    if len(md5s) < 1:
        return '"{}"'.format(hashlib.md5().hexdigest())

    if len(md5s) == 1:
        return '"{}"'.format(md5s[0].hexdigest())

    digests = b''.join(m.digest() for m in md5s)
    digests_md5 = hashlib.md5(digests)
    return '"{}-{}"'.format(digests_md5.hexdigest(), len(md5s))
    

s3_cli = boto3.client('s3')
s3_header = s3_cli.head_object(Bucket=bucket, Key=key)
e_tag = s3_header['ETag'].strip('"')

if len(e_tag)>32 and "-" in e_tag:
    s3_sub_header = s3_cli.head_object(Bucket=bucket, Key=key, PartNumber=1)
    chunk_size = s3_sub_header["ContentLength"]
    generated_hash = calculate_s3_etag(file_path, chunk_size=chunk_size)
    print("multi:",generated_hash)
else:
    chunk_size = s3_header["ContentLength"]
    generated_hash = calculate_s3_etag(file_path, chunk_size=chunk_size)
    print("single:",generated_hash)

print(e_tag==generated_hash)





