import itertools

data = ['A', 'B']
combinations_with_replacement = itertools.combinations_with_replacement(data, 2)

print("Kombinasi dengan pengulangan dari data:")
for combo in combinations_with_replacement:
    print(combo)
# Fungsi: Menghasilkan kombinasi dengan pengulangan.
# Kondisi: Ketika Anda ingin mendapatkan kombinasi yang memungkinkan elemen yang sama muncul berkali-kali.
