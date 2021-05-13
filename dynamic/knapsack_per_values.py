'''
knapsack
O( n * (sum of all values of items) )
f(i,v) = najmniejsza waga potrzebna do uzyskania wartości V do i-tego przedmiotu włącznie
'''
from random import shuffle, randint  # do testow


def knapsack(W, P, MaxW):
    n = len(W)
    MaxV = 0

    for i in range(n):
        MaxV += P[i]  # liczę sumę wartości wszystkich przedmiotów

    F = [[MaxW + 1 for _ in range(MaxV + 1)] for _ in
         range(n)]  # tworze tablice 2 wymiarową dl wierszy to wszystkie mozliwe wartosci
    # ^ tablica F jest wypelniona MaxW+1, ponieważ będę na kazdej [i][w] brał minimum
    # chcę najmniejszą wagę za którą mogę dostać dany value

    for i in range(0, n):  # itreuje po wszystkich przedmiotach
        F[i][P[i]] = W[i]  # wpisuję wagę minimalną W[i] do uzyskania wartości P[i] (brak tutaj "zestawów")

    for i in range(1, n):  # iteruję po kolejnych wierszach
        for v in range(1, MaxV + 1):  # iteruję po kolejnych kolumnach w danym wierszu
            if F[i - 1][v] < MaxW + 1:  # jeżeli wartosc nade mną wagi jest godna przepisania
                F[i][v] = min(F[i - 1][v], F[i][v])  # to przepisuję tę mniejszą między górą a aktualną pozycją
                if v + P[i] <= MaxV:  # jeżeli nie wyjdę za tablicę
                    F[i][v + P[i]] = F[i - 1][v] + W[i]  # dodaję przedmiot i-ty do danego już zestawu z góry
    for k in range(MaxV, -1, -1):
        if F[n - 1][k] < MaxW + 1:  # szukam pierwszej prawidłowej wagi od końca w ostatnim wierszu
            return k, F  # zwracam k-najwieksza wartosc i tablicę F
    return 0, F  # nie znalazłem, więc nie mogę nic zabrać, wartość = 0
    pass


def correct_knapsack(W, P, MaxW):
    n = len(W)
    F = [[0] * (MaxW + 1) for _ in range(n)]  # tworze tablice 2 wymiarową

    for i in range(W[0], MaxW + 1):  # uzupelnij 1 wiersz
        F[0][i] = P[0]

    for i in range(1, n):  # iteruję po kolejnych wierszach
        for w in range(1, MaxW + 1):  # iteruję po kolejnych kolumnach w danym wierszu
            F[i][w] = F[i - 1][w]  # przepisuję wartość która jest nade mną
            if w >= W[i]:  # jeżeli dopuszczalna waga jest odpowiednia by zmieścić przedmiot i-ty
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])  # wybieram korzystniejszą opcję w danej chwili
                # -----------|^nie biorę,| biorę^ |-> czyli pobieram wartość wcześniejszą(nade mną) przesuniętą w lewo
                # ---------------------------------o wagę rozważanego przedmiotu(i)
    return F[n - 1][MaxW], F  # moja best value znajduje sie w rogu tablicy dwuwymiarowej
    pass


def get_solution(F, W, P, i, k):
    if i == 0:
        if F[i][k] == P[i]: return [i]
        return []
    if F[i][k] == F[i - 1][k - P[i]] + W[i]:
        return get_solution(F, W, P, i - 1, k - P[i]) + [i]
    return get_solution(F, W, P, i - 1, k)


if __name__ == '__main__':
    P = [10, 8, 4, 5, 3, 7]  # przyklad z wykladu
    W = [4, 5, 12, 9, 1, 13]  # przyklad z wykladu
    MaxW = 24

    # test section
    for i in range(1000):
        if not (correct_knapsack(W, P, MaxW)[0] == knapsack(W, P, MaxW)[0]):
            print("TEST 1 FAILED")
            exit()
        MaxW = randint(1, 46)
        shuffle(P)
        shuffle(W)
    print("TEST 1 COMPLETE")

    for i in range(1000):
        MaxW = randint(1, 300)
        P = [randint(1, 30) for _ in range(20)]
        W = [randint(1, 30) for _ in range(20)]
        if not (correct_knapsack(W, P, MaxW)[0] == knapsack(W, P, MaxW)[0]):
            print("TEST 2 FAILED")
            exit()
    print("TEST 2 COMPLETE")
