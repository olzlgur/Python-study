score_file=open("score.txt","w", encoding="utf8") #파일 오픈
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file=open("score.txt" , "a", encoding="utf8") #파일에 이어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close

score_file=open("score.txt", "r" , encoding="utf8") #파일 읽기
print(score_file.read())
score_file.close()

score_file=open("score.txt", "r" , encoding="utf8") #한줄씩 읽기
while True:
    line=score_file.readline()
    print(line, end="")
    if not line:
        break
score_file.close()
print("\n")

score_file=open("score.txt", "r" , encoding="utf8")
lines=score_file.readlines()
for line in lines:
    print(line,end="")
score_file.close()