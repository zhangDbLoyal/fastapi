import psycopg2


if __name__ == '__main__':

    pg_url = "fastgpt#1234#10.0.46.78#8100#fastgpt"
    pgurl = pg_url.split('#')
    conn = psycopg2.connect(user=pgurl[0],
                                  password=pgurl[1],
                                  host=pgurl[2],
                                  port=pgurl[3],
                                  database=pgurl[4])
    cursor = conn.cursor()
    sql = "INSERT INTO vectorTest (name,vector1,vector2) VALUES 'zhang', ('[1,2,3]'), ('[1,1,1]');"
    cursor.execute(sql)

    conn.commit()

    # row = cursor.fetchone()
    # print(row)


    # cursor.execute(query)
    # emb_result = cursor.fetchall()
    # print("向量检索结果：", emb_result)