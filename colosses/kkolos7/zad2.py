def stypendia(T, A, k):
    m = len(T)
    n = len(T[0])
    # tu umieść swoją implementację


T = [[5.0, 5.0, 3.75, 4.5, 4.3, 4.1, 3.9, 4.9, 3.6, 2.0, 2.0, 2.0],
     [5.0, 4.6, 4.9, 4.2, 3.7, 4.0, 3.8, 4.01, 3.6, 3.5, 3.4, 2.0],
     [5.0, 4.7, 3.0, 3.5, 2.8, 2.7, 2.5, 2.0, 2.3, 2.2, 2.1, 2.4]]
print(stypendia(T, 7, 19) == True)
print(stypendia(T, 7, 21) == False)
