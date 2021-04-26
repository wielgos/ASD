# problem 1 minimalna ilosc tankowan (cena nas nie interesuje)
def min_tank(S, L, t):  # O(n)
    n = len(S)
    curr_pos = 0
    prev_pos = -1
    visited = 0
    i = 0
    # print(H)
    while L + curr_pos < t:
        if prev_pos == curr_pos:  # gdy zapętlimy się na tej samej stacji
            return -1  # to wiemy że nie możemy dalej nigdzie pojechać
        if S[i] <= L + curr_pos:  # mogę dojechać do 'i'
            i += 1
        else:
            i -= 1
            prev_pos, curr_pos = curr_pos, S[i]
            visited += 1
        if i == n - 1:  # wymuszamy tankowanie gdyz to ostatnia stacja a nie jestesmy u celu
            i -= 1
            prev_pos, curr_pos = curr_pos, S[i]
            visited += 1
    return visited


# problem 2 minimalny koszt dotarcia do t, zaczynamy z maxem paliwa
def min_cost_tank(S, P, L, t):  # zachlanny
    # dodajemy "fejk" stacje z "darmowym" paliwem
    for i in range(len(S)):
        if S[i] >= t:
            S.insert(i, t)
            P.insert(i, -1)
            result_index = i
            break
        elif i == len(S) - 1:
            S.insert(i + 1, t)
            P.insert(i + 1, -1)
            result_index = i + 1

    if L >= t:
        return 0

    pp = float('inf')
    n = len(S)
    for i in range(0, n):  # first move (znajdujemy najtansza stacje w zasiegu):
        if L < S[i]:
            break
        else:
            if P[i] < pp:
                pp = P[i]
                go_to = i

    current_index = go_to
    current_petrol = L - (S[go_to])
    current_costs = 0

    while True:
        i = current_index + 1  # skanujemy od danej stacji do przodu
        pp = float('inf')

        while i <= result_index:  # skanujemy stacje do przodu do ktorych mozemy podjechac
            if S[current_index] + L < S[i]:  # nie mozemy dojechac na i to konczymy skanowanie
                break
            else:
                if P[i] < pp:  # jezeli cena na itej stacji jest lepsza
                    pp = P[i]
                    go_to = i  # ewentualne go_to
            i += 1
        if pp == float('inf'):  # pp nie jest zmienione czyli w zasiegu nie mamy zadnej stacji i nie jestesmy przy celu
            return -1  # nie mozemy dojechac ;(
        if S[current_index] < pp:  # jezeli najtansza stacja znaleziona to ta na ktorej jestesmy to korzystamy na fulla
            current_costs += (L - current_petrol) * P[current_index]  # tankujemy do maxa
            current_petrol = L  # bo zatankowalismy
            current_petrol -= (S[go_to] - S[current_index])  # tracimy paliwo na pojechanie do go_to
            current_index = go_to  # jestemy od teraz na go_to
        else:  # jest stacja ktora ma tansze paliwo, to chcemy tam pojechac
            if S[current_index] + current_petrol >= S[go_to]:
                # nie musimy dotankowywac wiec jedziemy do tanszej stacji:
                current_petrol -= (S[go_to] - S[current_index])
                current_index = go_to
            else:
                # musimy dotankowac pare kropelek by dojechac do tanszej stacji:
                current_costs += (S[go_to] - S[current_index] - current_petrol) * P[current_index]
                current_petrol = 0
                current_index = go_to
        if current_index == result_index:
            return current_costs


# problem 2b) minimalny koszt dotarcia do t ale tankujemy tylko do fulla
def min_cost_tank_full(S, P, L, t):  # dynamiczny
    # F[i] to minimalny koszt do itej stacji + zatankowanie do pelna na niej
    # w miejscu 't' tworzę sztuczną stację z cenem paliwa równą 0
    for i in range(len(S)):
        if S[i] >= t:
            S.insert(i, t)
            P.insert(i, 0)
            result_index = i
            break
        elif i == len(S) - 1:
            S.insert(i + 1, t)
            P.insert(i + 1, 0)
            result_index = i + 1

    n = len(S)
    F = [float('inf') for _ in range(result_index + 1)]
    for i in range(result_index + 1):
        if S[i] > L:
            break
        F[i] = S[i] * P[i]
    for i in range(result_index + 1):
        for j in range(i - 1, -1, -1):
            if S[i] - S[j] <= L:
                F[i] = min(F[i], F[j] + (S[i] - S[j]) * P[i])
    if F[result_index] == float('inf'):
        return -1
    else:
        return F[result_index]


L = 20  # pojemnosc baku czołgu
S = [10, 30, 50, 70, 100]  # punkt na osi danej stacji
P = [3, 5, 7, 2, 5]  # cena za litr na kazdej i-tej stacji
t = 91  # dokad chcemy dojechac

# L = 10
# S = [8, 11, 15, 16]
# P = [40, 7, 15, 12]
# t = 23

# L = 14
# S = [1, 9, 15, 16, 17, 27, 28]
# P = [1, 100, 10, 15, 1, 30, 30]
# t = 30

print("min ilosc tank:", min_tank(S, L, t))
print("min koszt przejazdu:", min_cost_tank(S, P, L, t))
print("min koszt przejazdu tank do max:", min_cost_tank_full(S, P, L, t))
