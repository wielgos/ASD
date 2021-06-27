class NIEkarta:
    def __init__(self, cena, wartosc):
        self.cena = cena
        self.wartosc = wartosc


def starszy_pasjonat(T, x, D):
    def get_solution(F, T, i, w):
        if i == 0:
            if w >= T[0].cena: return [0]  # jezeli jestem na ostatnim przedmiocie i moge go wziac, to oczywiste ze go biorę
            return []  # nie mialem wagi więc nie biorę
        if w >= T[i].cena and F[i][w] == F[i - 1][w - T[i].cena] + T[i].wartosc:  # to znaczy ze dany przedmiot wzialem
            return get_solution(F, T, i - 1, w - T[i].cena) + [i]  # +[i] bo ity przedmiot wzialem jak sie okazalo
        return get_solution(F, T, i - 1, w)  # nie wzialem wiec waga zostaje taka sama
    # x - cap of cards
    # D - money avail
    # T - cards
    # F[i][j] max j value with i taken cards
    maxv = -1
    # for e in T:
    #     maxv = max(maxv, e.wartosc)
    n = len(T)
    F = [[0] * (D + 1) for _ in range(n)]
    for i in range(T[0].cena, D+1):
        F[0][i] = T[0].wartosc

    for i in range(1, n):
        for j in range(1, D + 1):
            F[i][j] = F[i - 1][j]
            if j >= T[i].cena:
                F[i][j] = max(F[i][j], F[i - 1][j - T[i].cena] + T[i].wartosc)
    print(F[-1][-1])
    sol = get_solution(F, T, n, D)
    print(sol)
    return F


from copy import deepcopy

T = [NIEkarta(5, 10), NIEkarta(5, 5), NIEkarta(9, 1), NIEkarta(10, 2)]
cp = deepcopy(T)
x = 2
D = 10
print(starszy_pasjonat(T, x, D), [cp[0], cp[1]])

T = [NIEkarta(5, 10), NIEkarta(2, 5), NIEkarta(4, 6), NIEkarta(1, 2)]
cp = deepcopy(T)
x = 3
D = 9
print(starszy_pasjonat(T, x, D), [cp[0], cp[1], cp[-1]])
