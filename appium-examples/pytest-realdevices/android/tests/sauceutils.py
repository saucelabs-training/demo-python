from __future__ import print_function
import os
import requests
import hashlib
import sys


def upload_app(app_path, username, password):
    app_file_name = os.path.basename(app_path)
    src_md5 = md5(app_path)
    resp = None
    with open(app_path, 'rb') as f:
        resp = requests.post(
                url='https://saucelabs.com/rest/v1/storage/%s/%s?overwrite=true' % (username, app_file_name),
                data=f,
                auth=(username, password),
                headers={'Content-Type': 'application/octet-stream'})
    if resp.status_code != 200:
        print(resp, file=sys.stderr)
        raise Exception("Upload failed!")
    else:
        if resp.json()['md5'] != src_md5:
            raise Exception("Upload failed: File corrupted!")


def md5(file_path):
    hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()
