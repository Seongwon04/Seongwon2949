import re
while True:
    str = input('텍스트를 입력하세요 ==> ')
    cp = re.compile('[a-zA-Z0-9_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+')
    result = cp.findall(str)
    if len(result) >= 1:
        print('추출된 이메일 주소:')
        for email in result:
            print(email)
    else:
        print('이메일 주소가 발견되지 않았습니다.')
        break