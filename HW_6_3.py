text = 'This is a more advanced comprehension exercise to practice'

result = [i[::-1] for i in text.split() if len(i) > 4]
print(result)