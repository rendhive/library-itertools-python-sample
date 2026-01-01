import itertools

iterable1 = [1, 2, 3]
iterable2 = ['a', 'b', 'c']

combined = itertools.chain(iterable1, iterable2)

print("Menggabungkan iterable:")
print(list(combined))
# Fungsi: Menggabungkan dua atau lebih iterable menjadi satu iterable.
# Kondisi: Ketika Anda ingin menggabungkan beberapa list atau koleksi lainnya.
