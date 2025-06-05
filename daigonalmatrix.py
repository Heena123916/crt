def diagonalSum(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i]           # primary diagonal
        total += mat[i][n - 1 - i]   # secondary diagonal

    if n % 2 == 1:                   # odd length: subtract center once
        total -= mat[n // 2][n // 2]

    return total
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
print("Diagonal Sum:", diagonalSum(mat))

