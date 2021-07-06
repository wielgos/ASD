from random import randint, seed


def mergesort(T):
  def cut(T,p,q): #funkcja pomocnicza, pocinacz tablicy od p do q włącznie
    res=[]
    for i in range(p,q+1):
      res += [T[i]]
    return res

  def mergesorthelper(T):
    n = len(T)
    if n > 1: #dzielę na części dopóki nie zostanie jeden element
      mid = n//2
      L = cut(T,0,mid-1) #ucinam T by uzyskać lewą część
      R = cut(T,mid,n-1) #ucinam T by uzyskać prawą część

      mergesort(L) #posortuj dla części L
      mergesort(R) #posortuj dla części R

      i = j = k = 0 #i-iteruje po tablicy L, j-iteruje po tablicy R, k-iteruje po finalnej tablicy
      n1 = len(L)
      n2 = len(R)
      #składanie razem posortowanych list L i R
      while (i < n1 and j < n2): #iteruję po L i R dopóki mogę porównywać elementy
        if L[i]<R[j]:
          T[k] = L[i]
          i += 1
        else:
          T[k] = R[j]
          j += 1
        k += 1
      if i == n1: #sprawdzam z której tablicy mam przepisać pozostałe elementy
        for l in range(j,n2):
          T[k] = R[l]
          k += 1
      else:
        for l in range(i,n1):
          T[k] = L[l]
          k += 1
  mergesorthelper(T) #sortuję mergesortem
  return T #zwracam finalną posortowaną tablicę
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")