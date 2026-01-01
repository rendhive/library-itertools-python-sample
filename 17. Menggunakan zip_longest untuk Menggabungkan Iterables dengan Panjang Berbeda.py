import itertools

list1 = [1, 2, 3]
list2 = ['A', 'B']

zipped = itertools.zip_longest(list1, list2, fillvalue='N/A')

print("Hasil zip_longest:")
for item in zipped:
    print(item)
# Fungsi: Menggabungkan elemen dari dua iterable dengan panjang berbeda.
# Kondisi: Ketika Anda perlu mengatasi iterable yang memiliki panjang berbeda secara bersamaan.
