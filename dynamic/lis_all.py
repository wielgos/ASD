# Mikołaj Wielgos
'''
Drobna uwaga: Cały kod implementowałem, by wypisywać ciągi w kolejności zgodnej z tablicą (tj. tak jak na przykładzie
z pdf) - linie 66-69, 32-33 są niepotrzebnymi zmianami - jak się okazało (godzinę przed deadlinem - mail
prof. Faliszewskiego) - nie jest to konieczne. Kodu postanowiłem już nie zmieniać, ponieważ bałem się że nie zdążę
poprawić rozwiązania.
--
Znajduje, zlicza, i wypisuje w odpowiedniej kolejności najdłuższe ciągi rosnące (longest increasing subsequences)
O(n^2)
Poszczególne opisy funkcji znajdują się już wewnątrz printAllLIS()
Krótki opis:
Bazuję na zwykłym LIS, ale z modyfikacją dodawania do tablicy Parentów. W tej tablicy trzymam długość danego ciągu, i
index do którego mam pójść, dzięki temu wiem, które mam wypisywać, a które nie. Nigdy nie nadpisuję, tylko dopisuję, by
mieć dostęp do wszystkich rozwiązań.

Wypisuję rekurencyjnie, a zliczam poprzez nonlocal variable (wygoda).
'''


def printAllLIS(A):
    def lis_upgraded(A):
        '''
        Funkcja LIS, ale "upgraded" ponieważ pozwala w tablicy Parentów zapisywać wszystkie "skoki" po indeksach.
        :param A: tablica na której działamy
        :return: (max długość, indeksy zakończeń podciągów, tablica parentów, tablica F)
        '''
        n = len(A)
        F = [1] * n
        P = [[] for _ in range(n)]
        maxF = 0
        indexF = []  # \/ idę od końca w pętli
        for i in range(n - 1, -1, -1):  # by mieć kolejność łatwą do wypisywania w P |modyfikacja zwykłego LIS'a
            for j in range(i, n):
                if A[j] > A[i] and F[j] + 1 >= F[i]:  # | modyfikacja zwykłego LIS'a
                    F[i] = F[j] + 1
                    P[i].append([j, F[i]])  # by móc odczytywać dane ciągi | modyfikacja zwykłego LIS'a
                    if F[i] >= maxF:  # by zbierać wszystkie indexF | modyfikacja zwykłego LIS'a
                        maxF = F[i]  # zbieram maxF już podczas pętl
                        indexF += [i]  # zbieram kolejne indexy z których potencjalnie będę wypisywał
        return maxF, indexF, P, F

    def recursiveprint(A, P, s, maxF, out, index=0):
        '''
        Funkcja rekurencyjna printująca wszystkie podciągi rozpoczynająca się z indeksu s podanego w argumencie.
        :param A: tablica na której działamy
        :param P: tablica parentów
        :param s: na którym indeksie obecnie jesteśmy
        :param maxF: długość LIS'a
        :param out: tablica w której przechowuję wynik do wypisania
        :param index: który index w tablicy out uzupełniam
        :return:
        '''
        nonlocal counter
        if index == maxF - 1:
            out[index] = A[s]
            for e in out:  # wersja wypisująca kolejne elementy tablicy out[], mogłabyć zastąpiona po prostu print(out)
                print(e, end=" ")  # wypisuję poszczególne elementy
            print()  # rozdzielam dany ciąg
            counter += 1  # wlasnie wypisalem dany sequence, więc zliczam go
            return
        else:
            out[index] = A[s]  # dodaję element do out[] na którym aktualnie jestem
            i = len(P[s]) - 1
            while i >= 1 and P[s][i][1] == P[s][i - 1][1]:  # sprawdza wszystkie możliwe skoki z danego indeksu
                i -= 1  # skok z itego miejsca jest możliwy, więc cofam się i sprawdzam dalej
            #pętla niżej zapewnia mi kolejnośc wypisywania zgodnie z kolejnością elementów w tablicy
            #jest zbędna jeżeli nie zależy nam na kolejności
            for j in range(i, len(P[s])):  # będę skakać od i do końca P[s] By zachować kolejność przy wypisywaniu
                recursiveprint(A, P, P[s][j][0], maxF, out, index + 1)

    def printAllSolutions(A, P, indexF, maxF):
        '''
        Funkcja, która "wypuszcza" wszystkie rekurencyjne wypisywania. Wszystkie potencjalne starty wypisywań, mam
        zapisane w indexF, koryguję tylko by wypisać tylko te najdłuższe(*).
        :param A: tablica na której działamy
        :param P: tablica parentów
        :param indexF: indeksy zakończeń podciągów
        :param maxF: długość LIS'a
        :return: ilość wszystkich LIS'ów
        '''
        i = len(indexF) - 1  # ustawiam i na koniec tablicy indexF
        recursiveprint(A, P, indexF[i], maxF,
                       [-1] * maxF)  # na pewno muszę wypisać ciąg ostatni zarejestrowany w indexF
        while i >= 1 and P[indexF[i]][len(P[indexF[i]]) - 1][1] == P[indexF[i - 1]][len(P[indexF[i - 1]]) - 1][
            1]:  # (*)
            # wygląda strasznie, ale iteruję po kolejnych startowych indeksach
            if indexF[i] != indexF[i - 1]:  # by nie wypisywać tych samych
                recursiveprint(A, P, indexF[i - 1], maxF, [-1] * maxF)  # odpowiednio rozpoczynam wypisywanie
            i -= 1  # idę w lewo i szukam kolejnych poprawnych indexów

    counter = 0  # licznik wszystkich LIS'ów
    maxF, indexF, P, F = lis_upgraded(A)  # zbieram dane by móc zacząć wypisywać
    printAllSolutions(A, P, indexF, maxF)  # wypisuję
    return counter  # zwracam licznik wszystkich LIS'ów
