class Unit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.damage=damage
        self.hp=hp
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 : {0}, 공격력 : {1}" .format(hp,damage))

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 {1}" .format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #wraith2에 새로운 멤버변수 선언

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다." .format(wraith2.name))