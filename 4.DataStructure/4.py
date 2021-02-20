#집합 (set)
#중복 안됨, 순서 없음

number1={1,2,3,3,3}
print(number1) #1,2,3 출력

number2={2,3,4}

print(number1&number2) #교집합 출력
print(number1.intersection(number2)) #교집합

print(number1|number2) #합집합
print(number1.union(number2)) #합집합

print(number1-number2) #차집합
print(number1.difference(number2))

number1.add(5)
print(number1)

number1.remove(5)
print(number1)