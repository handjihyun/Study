import pymysql

def create_usertable(conn, cur):
    try:
        query = """
        create table user_table
        (userID char(8) not null primary key,
        userName varchar(10) not null,
        birthYear int not null,
        addr char(2) not null,
        mobile1 char(3),
        mobile2 char(8),
        height smallint,
        mDate date)
        """

        cur.execute(query)
        conn.commit()

    except Exception as e:
        print(e)

def create_buytable(conn, cur):
    try:
        query = """
        create table buy_table
        (num int auto_increment not null primary key,
        userID char(8) not null,
        prodName char(6) not null,
        groupName char(4),
        price int not null,
        amount smallint not null,
        foreign key (userID) references user_table(userID))
        """

        cur.execute(query)
        conn.commit()
    
    except Exception as e:
        print(e)

def insert_data1(conn, cur):
    try:
        sql = """insert into user_table(userID, userName, birthYear, addr, mobile1, mobile2, height, mDate)
        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
        data = ( ('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
        ('KJD', '김제동', 1974, '경남', '', '', 173, '2013-03-03'),
        ('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
        ('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
        ('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
        ('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
        ('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
        ('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
        ('SDY', '신동엽', 1971, '경기', '', '', 176, '2008-10-10'),
        ('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08') )

        cur.executemany(sql, data)
        conn.commit()
    
    except Exception as e:
        print(e)

def insert_data2(conn, cur):
    try:
        sql = """insert into buy_table(num, userID, prodName, groupName, price, amount)
        values (%s, %s, %s, %s, %s, %s)"""
        data = ( (1, 'KHD', '운동화', '', 30, 2),
        (2, 'KHD', '노트북', '전자', 1000, 1),
        (3, 'KYM', '모니터', '전자', 200, 1),
        (4, 'PSH', '모니터', '전자', 200, 5),
        (5, 'KHD', '청바지', '의류', 50, 3),
        (6, 'PSH', '메모리', '전자', 80, 10),
        (7, 'KJD', '책', '서적', 15, 5),
        (8, 'LHJ', '책', '서적', 15, 2),
        (9, 'LHJ', '청바지', '의류', 50, 1),
        (10, 'PSH', '운동화', '', 30, 2),
        (11, 'LHJ', '책', '서적', 15, 1),
        (12, 'PSH', '운동화', '', 30, 2) )

        cur.executemany(sql, data)
        conn.commit()
    
    except Exception as e:
        print(e)

def main():
    # 데이터 베이스(shoppingmall) 연결
    conn = pymysql.connect(host='localhost', user='root', password='0131', db='shoppingmall', charset='utf8')

    # cursor 객체 생성
    cur = conn.cursor()

    # 테이블 생성 함수 호출
    create_usertable(conn, cur)
    create_buytable(conn, cur)

    # 데이터 추가
    insert_data1(conn, cur)
    insert_data2(conn, cur)

main()


def ans(sql):
    conn = pymysql.connect(host='localhost', user='root', password='0131', db='shoppingmall', charset='utf8')
    
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    
    for row in rows:
        print(row, end="\n")
    
    cur.close()
    conn.close()

# 1) 내부 조인한 결과에 ‘연락처’ 컬럼 추가
one = """select ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2) 연락처
        from user_table ut
        inner join buy_table bt
        on ut.userID = bt.userID;
        """
ans(one)

# 2) userID가 KYM인 사람이 구매한 물건과 회원 정보 출력
two = """select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2)
from user_table ut
inner join buy_table bt
on ut.userID = bt.userID
where ut.userID = 'KYM';"""

ans(two)

# 3) 전체 회원이 구매한 목록을 회원 아이디 순으로 정렬
three = """select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2)
from user_table ut
inner join buy_table bt
on ut.userID = bt.userID
order by userID;"""

ans(three)

# 4) 쇼핑몰에서 한 번이라도 구매한 기록이 있는 회원 정보를 회원 아이디 순으로 출력
#	(distinct 사용)
four = """select distinct ut.userID, ut.userName, ut.addr
from user_table ut
inner join buy_table bt
on ut.userID = bt.userID;"""

ans(four)

# 5) 쇼핑몰 회원 중에서 주소가 경북과 경남인 회원 정보를 회원 아이디 순으로 출력
five = """select ut.userID, ut.userName, ut.addr
from user_table ut
inner join buy_table bt
on ut.userID = bt.userID
where addr in ('경북', '경남');"""

ans(five)