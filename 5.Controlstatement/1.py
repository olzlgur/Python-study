weather = input("오늘 날씨는 어떤가요 ?")

if weather=="미세먼지" or weather=="눈" :
    print("마스크를 챙기세요")
elif weather=="비":
    print("우산을 챙기세요")
else :
    print("준비물이 필요 없습니다.")

    
temp = int(input("기온은 어떤가요? "))
if temp>=30 :
    print("굉장히 덥네요")
elif 10<temp and temp <30 :
    print("적당하네요")
else :
    print("외투를 챙기세요")