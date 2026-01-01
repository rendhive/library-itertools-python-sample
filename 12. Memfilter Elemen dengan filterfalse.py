import itertools

numbers = [1, 2, 3, 4, 5, 6]
filtered = itertools.filterfalse(lambda x: x % 2 == 0, numbers)

print("Filter angka genap:")
print(list(filtered))
# Fungsi: Memfilter elemen berdasarkan kondisi, menghasilkan elemen yang TIDAK memenuhi kondisi.
# Kondisi: Ketika Anda ingin menyaring elemen dari iterable yang tidak memenuhi kriteria tertentu.
