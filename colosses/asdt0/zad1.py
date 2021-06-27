from colosses.asdt0.zad1testy import runtests
from collections import deque


def tanagram(x, y, t):
    letters = ord('z') - ord('a') + 1
    posx = [deque() for _ in range(letters)]

    for i in range(len(x)):
        posx[ord(x[i]) - ord('a')].append(i)

    for i in range(len(y)):
        posofx = posx[(ord(y[i]) - ord('a'))].popleft()
        if abs(posofx - i) > t:
            return False
    return True


runtests(tanagram)
