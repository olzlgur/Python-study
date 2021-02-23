absent=[2,4]

for student in range(1,10) :
    if student in absent:
        continue
    print("{0}번 출석" .format(student))
        