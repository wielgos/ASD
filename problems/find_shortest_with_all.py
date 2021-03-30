'''
find shortest i to j with all "colors" (numbers in table)
'''

def find(A, k):
  colors = 0

  B = [0] * k

  i = 0
  j = -1

  min_i, min_j = -1, -1
  shortest = len(A)

  while True:
    if colors < k:
      if j == len(A) - 1:
        break
      j += 1
      if B[A[j]] == 0:
        colors += 1
      B[A[j]] += 1
    if colors == k:
      if j - i < shortest:
        min_i, min_j = i, j
        shortest = j - i
      B[A[i]] -= 1
      if B[A[i]] == 0:
        colors -= 1
      i += 1
  return min_i, min_j



if __name__ == '__main__':
    A = [0,1,0,0,2,3,0,1,2,3]
    print(find(A,4))
