from fastapi import APIRouter
from elasticsearch import Elasticsearch
from typing import Dict,Optional

basic = APIRouter()

es = Elasticsearch("http://localhost:9200")

@basic.post("/creatIndex",summary="创建索引")
def creat_index(index:str):
    if es.indices.exists(index = index):
        return {"error":"index_exist"}
    return es.indices.create(index=index)

@basic.post("/deleteIndex",summary="删除索引")
def delete_index(index:str):
    if es.indices.exists(index = index):
        es.indices.delete(index=index)
        return {"code":"0"}
    return {"error":"index_not_exist"}


@basic.post("/insertDataById",summary="插入数据")
def get(index:str,id:str,document:Optional[Dict]):
    if es.exists(index=index, id=id):
        return {"error":"data_exist"}
    es.index(index=index, id=id, body=document)
    return {"code":"0"}

@basic.post("/deleteDataById",summary="删除数据")
def delete(index:str,id:str):
    if es.exists(index=index, id=id):
        es.delete(index=index,id=id)
        return {"code":"0"}
    return {"error":"data_not_exist"}

@basic.post("/updateDataById",summary="更新数据")
def update(index:str,id:str,document:Optional[Dict]):
    if es.exists(index=index, id=id):
        es.update(index=index,id=id,doc=document)
        return {"code":"0"}
    return {"error": "data_not_exist"}

@basic.post("/selectDataById",summary="查询数据")
def select(index : str , id : str):
    if es.exists(index=index,id=id):
        return es.get(index = index ,id=id)
    return {"error":"data_not_exist"}

@basic.post("/selectDataAll",summary="查询数据")
def selectAll(index : str):
    if es.indices.exists(index = index):
        return es.search(index=index,)
    return {"error": "index_not_exist"}


