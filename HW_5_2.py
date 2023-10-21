from collections import deque

def solution(prices):
    List = []
    for k in range(n):
        List.append(0)
        for i in range(k+1, n):
            if prices[k] <= prices[i]:  #가격 증가 or 유지할때 List[k] 값 1씩 더하기
                List[k] += 1

    return List

prices = deque()
n = len(prices)
while True:
    price = input('Enter price (End enter = done) >> ')
    if price == 'done':
        break
    if int(price) < 1 or int(price) > 10000:  #범위에 맞지 않는 값 걸러내기
        print('Error : price는 1이상 10000이하로 입력해주세요. ')
        continue
    prices.append(price)

#price의 개수 범위 설정
test = True
if n < 2 or n > 100000:
    test = False
    print('Error : price는 최소 2번 최대 100000번까지 입력 가능합니다')
    
if test == True:
    print(f'prices\n{list(prices)}\n')
    print(f'result\n{solution(prices)}')
