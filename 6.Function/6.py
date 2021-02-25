gun = 10

def checkpoint(soldiers) :#경계근무
    global gun
    gun=gun-soldiers
    print("남은 총의 갯수 : {0}개" .format(gun))
    
print("전체 총의 갯수 : {0}개" .format(gun))
checkpoint(2)
print("남은 총의 갯수 : {0}개" .format(gun))

def checkpoint2(gun,soldiers):
    gun=gun-soldiers
    print("남은 총의 갯수 : {0}개" .format(gun))
    return gun

gun=checkpoint2(gun,2)
print("총의 갯수 : {0}개 " .format(gun))