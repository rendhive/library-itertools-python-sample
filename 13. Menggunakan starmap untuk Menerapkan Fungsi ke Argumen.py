import itertools

data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, data)

print("Hasil starmap (penjumlahan):", list(result))
# Fungsi: Menerapkan fungsi ke argumen dari iterable.
# Kondisi: Ketika Anda perlu menerapkan fungsi ke setiap item yang memiliki banyak argumen.
