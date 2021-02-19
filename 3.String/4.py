
print("나는 %d살입니다. " %24)
print("나는 %s를 좋아합니다." %"python")
print("Apple은 %c로 시작해요." %'a')

print("나는 %s살입니다." %24)
print("나는 %s와 %s를 좋아합니다." %("야구","축구"))

print("나는 {}살입니다." .format(24))
print("나는 {}와 {}를 좋아합니다." .format("야구","축구"))

print("나는 {age}살이며, {fruit}를 좋아합니다." .format(age=24, fruit="apple"))

age=24
color="초록색"

print(f"나는 {age}살이며, {color}를 좋아합니다.")