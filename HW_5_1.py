def solution(priorities, location):
    k = 0
    for i in priorities: #데이터를 [(priority,index), ...] 형식으로 새로운 데이터 생성
        List.append((i,k))
        k += 1

    print_order = 0
    while len(List) > 0: #List가 empty면 while문 종료
        doc = List.pop(0) #List의 첫번째 값 선택
        if any(doc[0] < item[0] for item in List): #doc의 priority를 List의 모든 priority들과 비교해서 하나라도 참이면
            List.append(doc) #List의 맨 뒤로 이동
        else:   #참이 아니면(가장 큰 값이면)
            print_order += 1 #프린트 순서 + 1
            if doc[1] == location: #doc 의 index가 location값과 같으면 저장된 프린트 순서를 return
                return print_order
    
List = []
priorities = []
while True:  #priorities 입력받는 반복문
    priority = int(input('중요도를 입력하시오. (0을 입력하면 입력을 그만둡니다..) >> '))
    if priority == 0:
        break
    priorities.append(priority)
location = int(input(f'인쇄 순서를 알고 싶은 index를 입력하시오.\n{priorities} >> '))

print('\n\n')
print(f'priorities\n{priorities}\n')
print(f'location\n{location}\n')
print(f'인쇄 순서\n{solution(priorities,location)}')