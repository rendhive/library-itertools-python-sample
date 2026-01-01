import itertools

data = ['A', 'B', 'C']
permutations = itertools.permutations(data, 2)

print("Permutasi 2 dari data:")
for perm in permutations:
    print(perm)
# Fungsi: Menghasilkan semua permutasi dari elemen.
# Kondisi: Ketika Anda ingin mendapatkan urutan yang mungkin dari elemen.
