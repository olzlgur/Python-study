IdNumber="980903-1234567"

print("성별 : " + IdNumber[7]) #7번째 값 출력
print("연 : " + IdNumber[0:2]) #0번째부터 2번째값 전까지 즉 0,1 인덱스에 위치한 값 출력
print("월 : " + IdNumber[2:4]) 
print("일 : " + IdNumber[4:6])

print("생년월일 : " + IdNumber[:6]) #처음부터 6번째값 전까지 출력
print("뒷 자리 : " + IdNumber[7:]) #7번째부터 끝까지 출력
print("뒷 자리(뒤에서부터) : " + IdNumber[-7:]) #뒤에서 7번째부터 끝까지 출력