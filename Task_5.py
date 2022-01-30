countOfOddNumbers = 0
countOfEvenNumbers = 0
numbers = [0, 5, 2, 4, 7, 1, 3, 19]

for number in numbers:
    if number % 2 == 0:
        countOfEvenNumbers = countOfEvenNumbers + 1
    else:
        countOfOddNumbers = countOfOddNumbers + 1

print('Count of odd numbers: ', countOfOddNumbers)
print('Count of even numbers: ', countOfEvenNumbers)
