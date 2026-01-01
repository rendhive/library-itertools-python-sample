import itertools

numbers = [1, 2]
letters = ['A', 'B']

combinations = itertools.product(numbers, letters)

print("Kombinasi angka dan huruf:")
for combo in combinations:
    print(combo)
# Fungsi: Mendapatkan kombinasi dari berbagai iterable.
# Kondisi: Ketika Anda ingin mengeksplorasi kombinasi yang mungkin dari elemen yang berbeda.
