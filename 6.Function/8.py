def study(* grade) :
    result=0
    cnt=0
    for gr in grade:
        result+=gr
        cnt+=1
    return result/cnt

res=study(80,70,90)

print("평균점수는 {0} 입니다." .format(res))
