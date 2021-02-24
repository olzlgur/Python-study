def profile(name, age, language):
    print("이름 {0}, 나이 {0}, 주 사용 언어 {0}" .format(name, age, language))

profile("이지혁",24,"Python")

def profile2(name, age=20, language="Python"):
    print("이름 {0}, 나이 {0}, 주 사용 언어 {0}" .format(name, age, language))

profile2("지혁")