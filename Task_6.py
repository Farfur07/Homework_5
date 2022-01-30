import random
countOfElements = int(input('Input size of array: '))
randomElements = [0] * countOfElements

# randomElements = [0, 0, 0, 0];

position = 0
for item in randomElements:
    randomElements[position] = random.randrange(0, 9)
    position = position + 1

position_2 = 0
copyRandomElements = randomElements.copy()

for item_2 in copyRandomElements:
    copyRandomElements[position_2] = item_2 * 2
    position_2 += 1

result = randomElements + copyRandomElements

print(randomElements)
print(result)

