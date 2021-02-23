from random import *
count=0
for i in range(1,51):
    customer=randrange(5,51)
    if 5<=customer and customer <=15:
        count+=1   
        print("[O] {0}번째 손님 ( 소요시간 : {1})" .format(i,customer))
        continue
    print("[ ] {0}번째 손님 ( 소요시간 : {1})" .format(i,customer))

print("총 탑승 승객 : {0} 분" .format(count))