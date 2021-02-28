import sys
print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep=":") 


for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))


answer=input("값을 입력하세요 : ")
print(type(answer))
print("입력하신 값은 {0}입니다." .format(answer))