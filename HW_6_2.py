numbers = []
while len(numbers) < 10:
    number = int(input('Enter the number. >> '))
    if number > 1000 or number < 0:
        print('Enter the right number. (0 <= number <= 1000)')
        continue
    else:
        numbers.append(number)
        
result = []
result = list(set(i%42 for i in numbers))
print(len(result))