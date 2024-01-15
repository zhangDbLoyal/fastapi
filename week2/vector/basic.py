from fastapi import APIRouter
import psycopg2
from typing import Dict,Optional,List

v_id = 4
v_basic = APIRouter()
pg_url = "fastgpt#1234#10.0.46.78#8100#fastgpt"
pgurl = pg_url.split('#')
conn = psycopg2.connect(user=pgurl[0],
                        password=pgurl[1],
                        host=pgurl[2],
                        port=pgurl[3],
                        database=pgurl[4])


@v_basic.post("/insertVector",summary="插入向量")
def insertVector(vector1:List[int],vector2:List[int]):
    cursor = conn.cursor()
    sql = "INSERT INTO vectorTest (id,vector1,vector2) VALUES  ((" + v_id.__str__() + "),('" + vector1.__str__() + "'), ('" + vector2.__str__() + "'));"
    cursor.execute(sql)
    conn.commit()
    return True

@v_basic.post("/selectAllVector",summary="查询所有向量")
def selectAllVector():
    cursor = conn.cursor()
    sql = "select * from vectortest;"
    cursor.execute(sql)
    conn.commit()
    return cursor.fetchall()
@v_basic.post("/selectVectorById",summary="根据id查询向量")
def selectVectorById(v_id :int ):
    cursor = conn.cursor()
    sql = f"select * from vectortest where id = {v_id};"
    cursor.execute(sql)
    conn.commit()
    data:dict = cursor.fetchall()
    if data :
        return data
    return {"未查到数据"}
@v_basic.post("/updateVectorById",summary="根据id修改向量")
def updateVectorById(v_id:int,vector1:List[int],vector2:List[int]):
    cursor = conn.cursor()
    sql =  "UPDATE vectorTest SET vector1 = '"+vector1.__str__()+"', vector2 = '"+vector2.__str__()+"' "+f"WHERE id = {v_id};"
    cursor.execute(sql)
    conn.commit()
    return True
@v_basic.post("/deleteVectorById",summary="根据id删除向量")
def deleteVectorById(v_id:int):
    ret = selectVectorById(v_id)
    if ret == {"未查到数据"}:
        return {"未查到数据"}
    cursor = conn.cursor()
    sql =  f"DELETE FROM vectorTest WHERE id = {v_id} "
    cursor.execute(sql)
    conn.commit()
    return True

