#!/bin/python3

def get_hourglass_sum(matrix, row, col):
    hourglass_sum = 0
    hourglass_sum += matrix[row - 1][col - 1]
    hourglass_sum += matrix[row - 1][col]
    hourglass_sum += matrix[row - 1][col + 1]
    hourglass_sum += matrix[row][col]
    hourglass_sum += matrix[row + 1][col - 1]
    hourglass_sum += matrix[row + 1][col]
    hourglass_sum += matrix[row + 1][col + 1]
    return hourglass_sum

if __name__ == '__main__':
    matrix = []
    for _ in range(6):
        row = list(map(int, input().rstrip().split()))
        matrix.append(row)

    max_hourglass_sum = float('-inf')
    for i in range(1, 5):
        for j in range(1, 5):
            current_hourglass_sum = get_hourglass_sum(matrix, i, j)
            max_hourglass_sum = max(max_hourglass_sum, current_hourglass_sum)

    print(max_hourglass_sum)
