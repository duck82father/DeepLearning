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
        INSERT tb_student (name, age, address) values ("kei", 35, "korea");
    '''

    # 테이블 생성a
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()