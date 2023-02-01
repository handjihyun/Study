import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', password = '0131', db = 'sakila', charset = 'utf8')

cur = conn.cursor()
cur.execute('select * from language')
rows = cur.fetchall()
print(rows)
language_df = pd.DataFrame(rows)
print(language_df)

# ----------------------------------------------------------------
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', password = '0131', db = 'sakila', charset = 'utf8')

cur = conn.cursor()
query = """
select c.email
from customer as c
    inner join rental as r
    on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)"""

cur.execute(query, ('2005-06-14'))
rows = cur.fetchall()
for row in rows:
    print(rows)

cur.close()
conn.close()

# ---------------------------------------------------
# 테이블 생성
def create_table(conn, cur):
    try:
        query = """
        create table customer1
        (name varchar(10),
        category smallint,
        region varchar(10))
        """

        cur.execute(query)
        conn.commit()
        print('Table 생성 완료')

    except Exception as e:
        print(e)

def main():
    # 데이터베이스(sqlclass_db) 연결
    conn = pymysql.connect(host = 'localhost', user='root',password='0131', db='sqlclass_db', charset='utf8')

    # cursor 객체 생성
    cur = conn.cursor()

    # 테이블 생성 함수 호출
    create_table(conn, cur)

    # 데이터 추가
    insert_table(conn, cur)

    # 여러 데이터 추가
    insert_manydata(conn, cur)

    # update 및 데이터 삭제
    update_delete(conn, cur)

    # 연결 종료
    cur.close()
    conn.close()
    print("Database 연결 종료")

main()

# 데이터 추가 : INSERT
#conn = pymysql.connect(host='localhost', user='root', password='0131', db='sqlclass_db', charset='utf8')

#cur = conn.cursor()
#sql = """insert into customer1(name, category, region) values (%s, %s, %s)"""

#cur.execute(sql, ('홍길동', 1, '서울'))
#cur.execute(sql, ('이연수', 2, '서울'))

#conn.commit()
#print("INSERT 완료")

#cur.close()
#conn.close()

# executemany()
# 여러 개의 tuple 데이터 처리
def insert_manydata(conn, cur):
    try:
        sql = """insert into customer1(name, category, region)
        values (%s, %s, %s)"""
        data = ( ('홍진우', 1, '서울'), ('강지수', 2, '부산'), ('김청진', 1, '대구'))
        
        # executemany() 함수 실행
        cur.executemany(sql, data)
        conn.commit()
        print('executemany() 완료')
    
    except Exception as e:
        print(e)

def insert_table(conn, cur):
    try:
        sql = """insert into customer1(name, category, region)
        values (%s, %s, %s)"""
        cur.execute(sql, ('홍길동', 1, '서울'))
        cur.execute(sql, ('이연수', 2, '서울'))

        conn.commit()
        print('INSERT 완료')
    except Exception as e:
        print(e)

def update_delete(conn, cur):
    try:
        sql = """update customer1 set region = '서울특별시' where region = '서울'"""
        
        cur.execute(sql)
        conn.commit()
        print("update 완료")

        # DELETE 데이터
        sql = """delete from customer where name = %s"""
        cur.execute(sql, '홍길동')
        print('delete 홍길동')

    except Exception as e:
        print(e)

update_delete(conn, cur)