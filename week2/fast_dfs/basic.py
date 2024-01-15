from fastapi import APIRouter
from typing import Dict,Optional
from fdfs_client.client import Fdfs_client

f_basic = APIRouter()

tracker_conf = {'host_tuple': ("10.0.47.165:22122",), 'port': 48080, 'timeout': 601, 'name': 'Tracker Pool'}
client = Fdfs_client(tracker_conf)

@f_basic.post("/uploadFileName",summary="上传文件")
def uploadFilename(fileName):
    return client.upload_by_filename(fileName)

@f_basic.post("/downloadFileName",summary="下载文件")
def downloadFile(fileId,fileName):
    buffer_content = client.download_buffer(fileId)
    with open(fileName, 'wb') as f:
        f.write(buffer_content)

@f_basic.post("/deleteFileName", summary="删除文件")
def delete_file(fileId):
    return client.delete_file(fileId.encode())