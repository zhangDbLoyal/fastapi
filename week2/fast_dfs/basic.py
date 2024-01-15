from fastapi import APIRouter
from typing import Dict,Optional
from fdfs_client.client import Fdfs_client

f_basic = APIRouter()

tracker_conf = {'host_tuple': ("10.0.58.119",), 'port': 22122, 'timeout': 601, 'name': 'Tracker Pool'}
client = Fdfs_client(tracker_conf)

@f_basic.post("/uploadFileName",summary="上传文件")
def uploadFilename(fileName ):

    filePath = r"D:\FastAPI\week2\doc\\"+fileName
    fileData = client.upload_by_filename(filePath)
    return fileData

@f_basic.post("/downloadFileName",summary="下载文件")
def downloadFile(fileId:str,fileName):
    filePath = r"D:\FastAPI\week2\doc\\" + fileName
    buffer_content = client.download_to_file(remote_file_id=fileId.encode("utf-8"),local_filename=filePath)
    print(1)
    return  buffer_content
@f_basic.post("/deleteFileName", summary="删除文件")
def delete_file(fileId):
    return client.delete_file(fileId.encode("utf-8"))