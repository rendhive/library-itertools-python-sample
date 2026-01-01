import itertools

data = ['A', 'B', 'C']
combinations = itertools.combinations(data, 2)

print("Kombinasi 2 dari data:")
for combo in combinations:
    print(combo)
# Fungsi: Menghasilkan semua kombinasi dari elemen tanpa pengulangan.
# Kondisi: Ketika Anda ingin mendapatkan kombinasi beberapa elemen dari kumpulan data.
