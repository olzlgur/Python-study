python="Python is Amazing"
print(python.lower()) #문자열을 소문자로 출력
print(python.upper()) #문자열을 대문자로 출력
print(python[0].isupper()) #0번째 문자 대문자 출력
print(len(python)) #문자열 길이 출력
print(python.replace("Python","Java")) #문자열 대체

index = python.index("n") #문자열 내 문자 인덱스 탐색
print(index)
index = python.index("n",index+1) #문자열 내 문자 인덱스 탐색, 탐색 시작위치 지정
print(index)

print(python.find("n")) #탐색

print(python.find("J")) #탐색 실패시 -1 출력

print(python.count("n")) #문자열 내 n의 갯수 탐색