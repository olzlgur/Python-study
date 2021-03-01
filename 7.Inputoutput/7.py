for cnt in range(1,51):
    report=open(str(cnt)+"주차.txt" , "w", encoding="utf8")
    report.write("{0}주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :\n" .format(cnt))
report.close()