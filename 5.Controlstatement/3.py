customer="손님"
index=5

while 1<=index: #while문
    print("{0} 커피가 준비되었습니다. {1}번 남았습니다." .format(customer,index))
    index-=1

    if index==0:
        print("커피는 폐기처분되었습니다.")

customer="이지혁"
person ="Unknown"
while person!=customer:
    print("{0}님 커피가 준비되었습니다." .format(customer))
    person=input("이름이 어떻게 되세요??")
    