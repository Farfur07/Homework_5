rowsCount = int(input("Input count of rows "))
columnsCount = int(input("Input count of columns "))


currentRow = 0

while currentRow < rowsCount:
    currentColumn = 0

    while currentColumn < columnsCount:
        if currentRow == 0 or currentRow == rowsCount - 1:
            print("*", end=' ')
        else:
            if currentColumn == 0 or currentColumn == columnsCount - 1:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        currentColumn += 1

    print('')
    currentRow += 1
