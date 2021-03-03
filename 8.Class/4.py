class Unit:
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp

class AttackUnit(Unit): #상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage=damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 : {0}, 공격력 : {1}" .format(self.hp,self.damage))

    def attack(self, location):
        print("{0}이 {1} 방향으로 공격을 시작합니다. 공격력은 {2} 입니다."\
             .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}이 {1}의 데미지를 입었습니다." .format(self.name, damage))
        self.hp-=damage
        print("{0}의 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다." .format(self.name))

firebat1 = AttackUnit("파이어뱃", 100, 50)

firebat1.attack("5시")
firebat1.damaged(70)
firebat1.damaged(50)
