'''
knapsack
O(n*maxW)
'''


def knapsack(W, P, MaxW):
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


def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]: return [0]  # jezeli jestem na ostatnim przedmiocie i moge go wziac, to oczywiste ze go biorę
        return []  # nie mialem wagi więc nie biorę
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:  # to znaczy ze dany przedmiot wzialem
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]  # +[i] bo ity przedmiot wzialem jak sie okazalo
    return get_solution(F, W, P, i - 1, w)  # nie wzialem wiec waga zostaje taka sama


if __name__ == '__main__':
    P = [10, 8, 4, 5, 3, 7]
    W = [4, 5, 12, 9, 1, 13]
    MaxW = 24
    # P = [1,2,3,4,5]
    # W = [5,4,2,1,1]
    # MaxW = 13
    maxv, F = knapsack(W, P, MaxW)
    print(maxv)
    print(get_solution(F, W, P, len(W) - 1, MaxW))
    pass
