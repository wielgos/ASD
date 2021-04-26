# Mikołaj Wielgos
"""
Kodowanie Huffmana.
Używam priority queue by w czasie nlogn móc "mergować" kolejne 2 najmniejsze elementy (lub wcześniej złączone już pary
elementów) w kolejce. Najpierw do kolejki dodaję wszystkie elementy z S i zapisuję ich indeks, jako tuple -
(czestotliwosc, indeks w s), ponieważ po dodaniu do priorityqueue będą uszeregowane według rosnącej częstotliwości
występowania. Dzięki temu wiem któremu elementowi przypisywać '0' lub '1' (nie muszę go szukać). Po połączeniu
2 elementów, powstaje mi nowe tuple (suma ich czestotliwosci, ich indeksy w S), gdyż potem po następnym "zmergowaniu"
będę musiał im wszystkim dać 0 lub 1.
Z obserwacji i badań doszedłem do wniosku, że średnia wysokość drzewa Huffmana dla 1000 symboli o długościach 1-1000
(random) wynosiła 1.6*log(n), stąd mój wysunięty wniosek, że średnia złożoność to nlogn (nie jestem do końca tego pewny)
Złożoność czasowa:
            średni przypadek  O(nlogn) (?)
            najgorszy przypadek (symbole majace częstotliwość w postaci "liczb fibonacciego" O(n^2)
            (^ gdyż drzewo wygląda jak "schody"^)
Potrzebna pamięć:
            przetrzymywanie priority queue dla n tupli,
            przetrzymywanie n-długości kodów: średnio n*(1.6*logn) (?)
"""

from queue import PriorityQueue

S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]


def huffman(S, F):
    q = PriorityQueue()  # inicjalizuję priority queue
    n = len(S)  # przypisuję do zmiennej 'n' długość tablicy 'S'
    codes = ['' for _ in range(n)]  # dla kazdego symbolu w S będe zapisywał jego kodowanie huffmana
    for i in range(n):  # złożonośc tej operacji to (nlogn)
        q.put((F[i], [i]))  # dodaję elementy do kolejki, element w kolejce to (czestotliwosc, jego index w S)

    while q.qsize() >= 2:  # dopóki mogę "mergować" dwa elementy
        m1 = q.get()  # biorę element o najmniejszej częstotliwości -> powinien dostać '0'
        m2 = q.get()  # biorę element o drugiej najmniejszej częstotliwości -> powinien dostać '1'
        for i in range(len(m1[1])):
            codes[m1[1][i]] += '0'  # do wszystkich uzbieranych indeksów do tej pory dodaję 0
        for i in range(len(m2[1])):
            codes[m2[1][i]] += '1'  # do wszystkich uzbieranych indeksów do tej pory dodaję 1
        q.put((m1[0] + m2[0], m1[1] + m2[1]))  # do kolejki dodaję połączone 2 elementy, odtąd będę go traktował jako 1
        # Uwaga: jako indeks "zmergowanym" elemencie kolejki, sumuję wszystkie indeksy uzbierane w m1 i m2
        # dzięki temu potem przy dodawaniu np '0' , dodaję tym wszystkim elementom

    sum = 0  # będę liczył długość całego napisu
    for i in range(n):
        print(S[i], ":", end=" ")  # printuję symbol
        for j in range(len(codes[i]) - 1, -1, -1):  # przechodzę od tyłu, ponieważ kodowanie powstawało od końca
            print(codes[i][j], end="")  # printuję po znaku kodowanie danego symbolu

        sum += F[i] * len(codes[i])  # przy okazji liczę długość napisu sumując iloczyn jego częstotliwości i długości
        print()  # robię odstęp na kolejne symbole
    print("dlugosc napisu:", sum)  # finalna długość napisu


huffman(S, F)
