import re
fhand = open('mbox.txt')
num_list = []
count = 0
x = re.compile('New Revision: [0-9]+')
for line in fhand:
    line = line.rstrip()
    num = x.findall(line)
    if len(num) > 0:
        count += 1
        num_list.append(int(num[0][14:]))
    
sum_num = sum(num_list)
num_num = len(num_list)
aver_num = sum_num / num_num
print(f'Total {count} lines are matched')
print('Average : ', aver_num)