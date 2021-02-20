#리스트

number=[30,40,20,10,50] #정수형 리스트
print(number)

animal=["cat","dog","frog"] #문자형 리스트
print(animal)

animal.append("pig") #원소 추가
print(animal)

animal.insert(2,"cow") #2번째 위치에 원소 추가
print(animal)

print(animal.pop()) #마지막 원소 꺼내기
print(animal)

print(animal.count("dog")) #원소의 갯수 세기


number.sort() #정렬기능
print(number)

number.reverse() #순서 뒤집기
print(number) 

mix=["이지혁",20,True] #여러가지 자료형 사용
print(mix)

mix.extend(number) #리스트 확장
print(mix)