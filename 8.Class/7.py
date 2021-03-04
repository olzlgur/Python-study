class Unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" .format(self.name, location, self.speed ))
class AttackUnit(Unit): #상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

class BuildingUnit(Unit):
    def __init__(self, name, hp, loaction):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500 ,"7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass


game_start()
game_over()