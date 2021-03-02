class Unit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.damage=damage
        self.hp=hp
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 : {0}, 공격력 : {1}" .format(hp,damage))

marine1=Unit("마린", 40, 5)
marine2=Unit("마린", 40, 5)
tank1=Unit("탱크", 30, 10)