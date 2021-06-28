from random import randint
import copy

T1 = [0.1, 0.5, 0.2, 0.78, 0.01 ]
T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
T3 = [0.1, 0.9,0.2,0.8,0.3,0.7,0.4,0.6]

D1 = [2**x for x in T1]
D2 = [2**x for x in T2]
D3 = [3**x for x in T3]

TESTS = [(D1,2), (D2,2), (D3,3)]



def T2S( T ):
    return " ".join([ "%.3f" % x for x in T ] )

random_wrong = ["https://www.youtube.com/watch?v=AHdfqDWl3T4",
        "https://www.youtube.com/watch?v=VPBbqc8W47Q",
        "https://www.youtube.com/watch?v=gAxVR2tvpA4 dobra ja sie cykam jak to mialo dzialac",
        "https://www.youtube.com/watch?v=1p6Fp2bkw4Y destroyed",
        "https://www.youtube.com/watch?v=-h057K7E3io",
        ]


random_good = ["https://www.youtube.com/watch?v=D_UKuVGzCHk wzz wzz wzz ojciec ma boscha",
        "https://www.youtube.com/watch?v=ytSsGn3E-ic",
        "https://www.youtube.com/watch?v=ZZMxFPNqZLk mozesz isc pic bo dziala",
        "https://www.youtube.com/watch?v=fTFL-hNoQuE ten wieśniacki sweter",
        "https://www.youtube.com/watch?v=8TTU-ivcy6M",
        "https://www.youtube.com/watch?v=3OWSjjcAswM",
        "https://www.youtube.com/watch?v=9Xfv1qzSX5I",
        "https://www.youtube.com/watch?v=XrzqiIhU5cU"]


def runtests( f ):
    OK = True
    for (T,a) in TESTS:
        BAD = False
        T1 = copy.deepcopy( T )
        T2 = copy.deepcopy( T )
        T.sort()
        print( "tablica            :", T2S(T2) )
        print( "posortowana tablica:", T2S(T) )
        res = f(T1,a)
        print( "wynik programu     :", T2S(res) )

        if len(res) != len(T):
            OK = False
            print("Tablice sa roznych dlugosci")
            continue

        for i in range(len(T)):
            if abs(T[i] - res[i]) > 0.001:
                   BAD = True
                   break
        if BAD:
            OK = False
            print("Blad!")

        print("----------------------")

    if OK:
        print(random_good[randint(0,len(random_good)-1)])
        print( "OK!" )
    else:
        print(random_wrong[randint(0,len(random_wrong)-1)])
        print( "Bledy!" )
