def price(A):

    n = len(A)


    B = [[0]*n for _ in range(n)]
    B[0][0] = A[0][0]

    for i in range(1,n):
        B[0][i] = B[0][i-1] + A[0][i]

    for i in range(1,n):
        B[i][0] = B[i-1][0] + A[i][0]

    for i in range(1,n):
        for j in range(1,n):
            B[i][j] = min(B[i-1][j], B[i][j-1]) + A[i][j]

    return B


def get_solution(A, B, i, j):
    if i==0 and j==0:
        return [[0,0]]
    if i > 0 and B[i][j] == B[i-1][j] + A[i][j]:
        return get_solution(A, B, i-1, j) + [[i,j]]
    if j > 0 and B[i][j] == B[i][j-1] + A[i][j]:
        return get_solution(A, B, i, j-1) + [[i,j]]

if __name__ == '__main__':
    A = [[1, 1, 2],
         [5, 1, 3],
         [4, 1, 1]]
    B = price(A)
    print(get_solution(A,B,2,2))
