import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요.
    db = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'user',
        passwd = '1234',
        db = 'homestead',
        charset = 'utf8'
    )
    
    # 테이블 생성 sql 정의
    sql = '''
    create table tb_student (
        id int primary key auto_increment not null,
        name varchar(32),
        age int,
        address varchar(32)
    ) engine = InnoDB default charset=utf8
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()