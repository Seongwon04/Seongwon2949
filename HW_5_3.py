from collections import Counter
import re

#파일 오픈
fhand = open('file01.txt')
fhand2 = open('file02.txt')

#줄바꿈 문자 제거, 소문자 변환
file01 = fhand.read()
new_file01 = file01.replace('\n', ' ')
new_file01 = new_file01.lower()

file02 = fhand2.read()
new_file02 = file02.replace('\n', ' ')
new_file02 = new_file02.lower()

#공백을 기준으로 스플릿
f1_list = new_file01.split()
f1_list = [re.sub(r'[^\w\s]', '', s) for s in f1_list] #특수문자(.) 지우기 (문자, 화이트 스페이스가 아닐경우 ''으로 바꾸기)
f2_list = new_file02.split()
f2_list = [re.sub(r'[^\w\s]', '', s) for s in f2_list] #특수문자(.) 지우기 (문자, 화이트 스페이스가 아닐경우 ''으로 바꾸기)

counter1 = Counter(f1_list)
counter2 = Counter(f2_list)

common_words = counter1 & counter2

print('공통된 단어와 각 파일에서의 빈도:')
for word in common_words:
    print(f'{word}: 파일1 - {counter1[word]} / 파일2 - {counter2[word]}')
    