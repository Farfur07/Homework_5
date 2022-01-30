import random
countOfMonths = int(input('Enter number of months: '))
salary = [0] * countOfMonths


position = 0
for item in salary:
    salary[position] = random.randrange(7500, 15000)
    position = position + 1

print(salary)

sumOfSalary = 0
for item in salary:
    sumOfSalary = item + sumOfSalary

average = sumOfSalary / countOfMonths
print(average)

