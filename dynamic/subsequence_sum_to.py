'''
problem sumy podzbiorów, szukamy podciągu o ile istnieje sumującego się dokładnie do T
zakładam liczby naturalne
subset sum problem

O(n*T)
'''

import random

def ssl(A, t):
    n = len(A)

    if t<0: #trywialny przypadek
        return False, []
    if t==0: #trywialny przypadek
        return True, []

    F = [[-1 for _ in range(t + 1)] for _ in range(n)] #deklaruję tablicę 2d
    #^ kolumny oznaczają sumę, F[i][j]=-1 oznacza, że danej sumy nie da się uzyskać
    #^ wiersze oznaczają do którego indeksu w tablicy A[] mozemy sięgać

    for i in range(n): #iteruję po kolejnych elementach w A i wpisuję ich wartosci
        if A[i] <= t:
            F[i][ A[i] ] = A[i]

    for i in range(1,n): #iteruję po kolejnych wierszach
        for j in range(1,t+1): #iteruję po kolejnych kolumnach
            if j == t and F[i][j]!=-1: #jeżeli na kolumnie t, znajdzie się wartość inna niż -1, to jest możliwa suma
                return True, F, i
            if F[i-1][j] > 0: #jeżeli element nade mną nie jest -1
                F[i][j] = F[i - 1][j] #to przepisuję go do dołu
                if A[i]+j<=t:
                    F[i][A[i] + j] = A[i] #i do razu zaznaczam że do sumy z góry mogę dokleić i-ty element, więc odhaczam
                                      #w odpowiedniej kolumnie w danym wierszu -1 (wpisuję tam A[i])
    return False, F, -1 #przeszedłem przez pętlę i w kolumnie t zawsze była -1, więc zwracam fałsz

def get_solution(A, F, i, j):
    if i==0:
        if F[i][j]!=-1: return [ F[i][j] ]
        return []
    if F[i][j]!=-1:
        return get_solution(A, F, i-1, j-F[i][j]) + [F[i][j]]
    return get_solution(A, F, i-1, j)

if __name__ == '__main__':
    A = [1,1,1,5,2]
    t = 10

    # res, F, i = ssl(A, t)
    # for e in F:
    #     for e2 in e:
    #         print(e2, end="\t")
    #     print()
    # print(get_solution(A,F, i, t))


    #test section
    for i in range(1000):
        A = [random.randint(1,50) for _ in range(30)]
        t = A[random.randint(0,14)] + A[random.randint(15,29)]
        if ssl(A,t)==False:
            print("TEST 1 FAILED")
            exit()
    print("TEST 1 COMPLETE")
    for i in range(1000):
        A = [random.randint(0,20)*2 for _ in range(30)] #same parzyste
        t = random.choice([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41])
        if ssl(A,t)==True:
            print("TEST 2 FAILED")
            exit()
    print("TEST 2 COMPLETE")
