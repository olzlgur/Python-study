cabinet={1:"Java", 5:"Python"}

print(cabinet[1])
print(cabinet.get(5))

print(1 in cabinet) #True
print(3 in cabinet) #False

study={"A-1" : "Python", "A-2" : "Java"}
print(study["A-1"])
print(study["A-2"])

study["A-3"]="C++"
print(study["A-3"])

del study["A-3"]
print(study)

print(study.keys()) #key만 출력

print(study.values()) #value만 출력

print(study.items()) #둘 다 출력

study.clear() #모든 값 삭제
print(study)