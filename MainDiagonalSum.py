def findMainDiagonalSum(matrix):
    mainDiagonalSum = 0

    for i in range(len(matrix)):
        mainDiagonalSum += matrix[i][i]

    return mainDiagonalSum


if __name__ == "__main__":
    inputList = list(map(int, input().split()))
    noOfRows = inputList[0]
    noOfColumns = inputList[1]
    matrix = []

    prevI = 0
    for i in range(2, len(inputList) + noOfColumns, noOfColumns):
        rows = []
        for j in range(prevI, i):
            rows.append(inputList[j])
        prevI = i
        if i != 2:
            matrix.append(rows)

    print(findMainDiagonalSum(matrix))
