# Mikołaj Wielgos

# Rekurencyjny algorytm znalezienia minimalnego 'min-cut' w Binary Search Tree.
# Uruchamiam rekurencję od root.left i root.right, rekurencja jeżeli napotka node który ma liść, zwraca wartość
# danego node. W przeciwnym wypadku, rekurencja idzie głębiej, i zbiera wartości kolejne wartości min.
# Przydatne są funkcje pomocnicze is_leaf(node) oraz has_leaf(node), gdyż to one dyktują nam kiedy idziemy w głąb drzewa
# Działanie: rekurencyjnie schodzę w dół drzewa początkowo z lewej i prawej strony począwszy od roota,
# gdy jestem już najniżej jak się da, to zbieram kolejne wartości min idąc spowrotem do góry
# Po zakończeniu funkcji (przejście n node'ów) znajduję dany min-cut który jest sumą znalezionego min-cut po lewej i
# prawej stronie.

# Złożoność czasowa: O(n) - musimy przejść po node'ach w drzewie
# Złożoność pamięciowa: O(log n) - na stosie rekurencji będzie maksymalnie log(n), zakładam drzewo zbalansowane

from colosses.kolos3.zad2testy import runtests


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
    def is_leaf(node):  # funkcja pomocnicza sprawdzająca czy dany node jest liściem
        if node.left is None and node.right is None:
            return True
        return False

    def has_leaf(node):  # funkcja pomocnicza sprawdzająca czy dany node ma liść
        if node.right is not None and is_leaf(node.right):
            return True
        if node.left is not None and is_leaf(node.left):
            return True
        return False

    def rek_mincut(node):
        if node is not None:
            if has_leaf(node):  # jeżeli ma liść to zwracam po prostu wartość w node
                return node.value
            else:  # w innym wypadku zwracam wartość aktualnego node (moge go 'uciąć') i rekurencja lewo i prawo
                return min(node.value, rek_mincut(node.right) + rek_mincut(node.left))
        return 0

    best_cut = rek_mincut(T.left) + rek_mincut(T.right)  # najlepszym cutem będzie mincut left i mincut right
    return best_cut


runtests(cutthetree)
