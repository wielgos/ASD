from queue import PriorityQueue


def szukaj_znajomosci(G, U, h):
    k = h * 12 * (-1)
    # G(V,E) znajomosci na uczelni all
    # U znajomosci STUDENTA na uczelni (startowe wierzcholki maybe?)
    # h pitos

    Q = PriorityQueue()
    n = len(G)
    known = [False] * n
    known[0] = True
    Q.put((k, 0, 0, known.copy()))
    for e in U:
        known[e] = True
        Q.put((k, e, 0, known.copy()))
        known[e] = False

    maks = (-5, 22)
    while not Q.empty():
        h, u, cnt, known = Q.get()
        #print(f"h:{h},u:{u},cnt:{cnt}")
        #print(known)
        if cnt > maks[0]:
            maks = (cnt, h * (-1))
        # print(G[u])
        for v, w in G[u]:
            if not known[v]:
                if h + w <= 0:
                    known[v] = True
                    Q.put((h + w, v, cnt + 1, known.copy()))
                    Q.put((h + w, 0, cnt + 1, known.copy()))
                    known[v] = False
    print(maks)
    return maks[0]


from colosses.szukajznajomosciXDtesty import runtests
runtests(szukaj_znajomosci)
