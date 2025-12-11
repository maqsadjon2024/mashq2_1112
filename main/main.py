#6
tub_sonlar = {
    x for x in range(2, 51)
    if all(x % d != 0 for d in range(2, int(x**0.5) + 1))
}
print(tub_sonlar)

#7
words = ["olma", "anjir", "Gilos", "uzum", "banan", "Olov"]
unlidan_boshlanadigan = {
    w for w in words if w.lower().startswith(("a", "e", "i", "o", "u", "o‘", "u‘"))
}
print(unlidan_boshlanadigan)

#8
matn = "Assalomu alaykum"
unikal_harflar = {harf for harf in matn if harf.isalpha()}
print(unikal_harflar)

#9
toq_kublar = {x**3 for x in range(1, 31) if x % 2 == 1}
print(toq_kublar)

#10
soz = "Python"
ascii_qiymatlar = {ord(harf) for harf in set(soz)}
print(ascii_qiymatlar)
