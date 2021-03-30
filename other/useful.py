def is_prime(n):
    if n == 2: return True
    if n % 2 == 0 or n==1: return False
    for i in range(3, int(n ** (0.5) + 1), 2):
        if n % i == 0:
            return False
    return True


def nwd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        b, a = a % b, b
    return a


def na_system_k(number, k):  # zwraca listę
    counter = 1
    while number >= k ** counter:
        counter += 1
    result = [-1] * counter
    i = counter - 1
    while number != 0:
        result[i] = number % k
        number //= k
        i -= 1
    return result


def digits(n):
    counter = 0
    while n != 0:
        n -= n % 10
        n //= 10
        counter += 1
    return counter


def get_digit(n, p):  # indeksowanie od 1, potrzeba digits()
    q = digits(n)
    if p == q:
        return n % 10
    n = n - n % (10 ** (q - p))
    a = n % (10 ** (q - p + 1))
    a //= 10 ** (q - p)
    return a


def bsort(t):
    N = len(t)
    for i in range(0, N - 1):
        for j in range(0, N - i - 1):
            if t[j] > t[j + 1]:
                t[j + 1], t[j] = t[j], t[j + 1]


def jedynki_binarnie(a):  # ile jest jedynek w binarnym zapisie
    ile = 0
    while a != 0:
        if a % 2 == 1:
            ile += 1
        a //= 2
    return ile


def reverse_list(a, p=0):
    if p == len(a) // 2:
        return
    a[len(a) - p - 1], a[p] = a[p], a[len(a) - p - 1]
    reverse_list(a, p + 1)


def czynniki_pierwsze(n):  # zwraca liste z czynnikami pierwszymi
    l = []
    if is_prime(n):
        return l + [n]
    c = 2
    while n != 1:
        if n % c == 0:
            l += [c]
            while n % c == 0:
                n //= c
        c += 1
    return l


def czynniki_pierw_bez_ost(n):  # bez ost
    l = []
    org = n
    c = 2
    while n != 1 and c <= n and c!=org:
        if n % c == 0:
            l += [c]
            while n % c == 0:
                n //= c
        c += 1
    return l

def n_number_to_base_b(n,b): #returns list containing digits of the number
    res = []
    while n!=0:
        res += [n%b]
        n = (n-n%b)//b
    return res[::-1]