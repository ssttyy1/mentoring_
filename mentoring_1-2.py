print("100보다 작은 자연수와 0으로 이루어진 9X9 행렬을 만드시오.")
matrix = []
for i in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(matrix):
    print(row)

max_value = 0
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i + 1
            max_col = j + 1

print(max_value)
print(max_row, max_col)