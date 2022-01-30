import random

matrix = []

for row in range(0, 5):
    columns = []
    for column in range(0, 4):
        columns.append(random.randint(0, 10))
    matrix.append(columns)
print(matrix)

total = 0
for item in matrix:
    for column in item:
        total = total + column
print(total)





