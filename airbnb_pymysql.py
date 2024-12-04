import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='990924',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # # 문제1: 새로운 제품 추가
    # sql = "insert into products(productName, price, stockQuantity) values (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 10000, 10))
    # connection.commit()
    
    # # 문제2: 고객 목록 조회
    # cursor.execute("select * from Customers")
    # for i in cursor.fetchall():
    #     print(i)
    
    # # 문제3: 제품 재고 업데이트
    # sql = "update products set stockQuantity= stockQuantity-%s where productID=%s"
    # cursor.execute(sql, (1, 1))
    # connection.commit()
    
    # # 문제4: 고객별 총 주문 금액
    # sql = "select customerID, sum(totalAmount) as totalAmount from orders  group by customerID"
    # cursor.execute(sql)
    # i = cursor.fetchall()
    # print(i)
    
    # # 문제5: 고객 이메일 업데이트
    # sql = "update customers set email=%s where customerID=%s"
    # cursor.execute(sql, ('update@email.com', '1'))
    # connection.commit()
    
    # # 문제6: 주문 최소
    # sql = "delete from orders where orderID=%s"
    # cursor.execute(sql, 15)
    # connection.commit()
    
    # # 문제7: 특정 제품 검색
    # sql = "select * from products where productName like %s"
    # cursor.execute(sql, '%Book%')
    # datas = cursor.fetchall()
    
    # for i in datas:
    #     print(i['productName'])
    
    # # 문제8: 특정 고객의 주문 데이터 조회
    # sql = "select * from orders where customerID=%s"
    # cursor.execute(sql, 5)
    # datas = cursor.fetchall()
    
    # for i in datas:
    #     print(i)
        
    # 문제9: 가장 많이 주문한 고객
    sql = "select customerID, count(*) as orderCount from orders group by customerID order by orderCount desc limit 1"
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    
    cursor.close()