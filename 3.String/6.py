#url로 비밀번호 생성하기

# 예시 : http://naver.com
# 규칙 1 : http:// 부분은 제외 -> naver.com
# 규칙 2 : 처음 만나는 점 이후 부분 제외 -> naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                         (nav)        (5)           (1)           !
# 비밀번호 : nav51!

url="http://google.com"
m_str=url.replace("http://","") #http:// 제외
m_str=m_str[:m_str.index(".")] #첫 번쨰 '.' 직전까지만 저장
password=m_str[:3] + str(len(m_str)) + str(m_str.count("e")) + '!' #비밀번호 생성

print("{0}의 비밀번호는 {1}입니다." .format(url,password))

