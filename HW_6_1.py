prices = []
while len(prices) < 5:
    price = int(input('Enter the price. >> '))
    if price > 2000 or price < 100:
        print('Enter the right value. (100 <= value <= 2000)')
        continue
    else:
        prices.append(price)

Sum = [i for i in prices if i == min(prices[0:2])] + [j for j in prices if j == min(prices[3:])]
print(sum(Sum))
        