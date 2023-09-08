def bilanganPrrima(aaa):
    # aab => list untuk menyimpan bilangan prima akan berisi boolean
    # aba => daftar bilangan prima yang ditemukan

    aab = [True] * (aaa + 1)
    aab[0] = aab[1] = False
    aba = []

    for baa in range(2, aaa + 1):
        if aab[baa]:
            aba.append(baa)
            for bbb in range(baa * baa, aaa + 1, baa):
                aab[bbb] = False

    return aba

# Contoh penggunaan:
print(bilanganPrrima(100))
