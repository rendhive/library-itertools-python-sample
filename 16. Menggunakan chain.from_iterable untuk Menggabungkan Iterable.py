import itertools

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
combined = itertools.chain.from_iterable(lists)

print("Menggabungkan beberapa iterable:")
print(list(combined))
# Fungsi: Menggabungkan beberapa iterable menjadi satu iterable.
# Kondisi: Ketika Anda ingin menggabungkan koleksi iterable yang lebih besar menjadi satu.
