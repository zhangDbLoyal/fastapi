from fastapi import APIRouter
from elasticsearch import Elasticsearch
from typing import List


search = APIRouter()

es = Elasticsearch("http://localhost:9200")

@search.post("/selectDataByEqualName",summary="准确查询key—value",description="准确查询key—value")
def selectByName(index : str , key : str, value :str,begin:int = None, size :int = None):
    # 判断索引存在
    if not(es.indices.exists(index = index)):
        return {"error":"index_exist"}
    # sql拼接
    body = {}
    sql = {key:value}
    body["query"] = {"term": sql}
    if begin:
        body["from"] = begin
    if size:
        body["size"] = size
    data = es.search(index=index,body = body)
    return data

@search.post("/selectDataByEqualNameInList",summary="准确查询key-in-values(List)",description="准确查询key-in-values(List)")
def selectByNameInList(index : str , key : str,alist : List[str],begin:int = None , size :int = None):
    # 判断索引存在
    if not(es.indices.exists(index = index)):
        return {"error":"index_exist"}
    # sql拼接
    body = {}
    sql = {key:alist}
    body["query"] = {"terms": sql}
    if begin:
        body["from"] = begin
    if size:
        body["size"] = size
    data = es.search(index=index,body = body)
    return data

@search.post("/selectDataByKeyLikeValue",summary="模糊查询key—value",description="模糊查询key—value")
def selectByName(index : str , key : str, value :str,begin:int = None , size :int = None):
    # 判断索引存在
    if not(es.indices.exists(index = index)):
        return {"error":"index_exist"}
    # sql拼接
    body = {}
    sql = {key: value}
    body["query"] = {"match": sql}
    if begin:
        body["from"] = begin
    if size:
        body["size"] = size
    data = es.search(index=index,body = body)
    return data


@search.post("/test",summary="test",description="test")
def test(index : str , key : str, value :str,begin:int = None , size :int = None):
    # 判断索引存在
    if not(es.indices.exists(index = index)):
        return {"error":"index_exist"}
    # sql拼接
    body={}
    sql = {key:value}
    body["query"]={"match":sql}
    body["from"] = begin
    body["size"] = size
    # match["term"] = sql
    print(body)
    data = es.search(index=index,body = body)
    return data