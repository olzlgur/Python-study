def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 {0}, 나이 : {1}\t" .format(name,age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("이지혁",24,"Pthon","Java","C++","C#","Javascript")

def profile2(name, age, *language):
    print("이름 {0}, 나이 : {1}\t" .format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile2("이지혁",24,"Pthon","Java","C++","C#","Javascript","Kotlin")