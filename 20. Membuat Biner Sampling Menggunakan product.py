import itertools

num_bits = 3
samples = itertools.product([0, 1], repeat=num_bits)

print("Sampel biner untuk 3 bit:")
for sample in samples:
    print(sample)
# Fungsi: Menghasilkan semua kombinasi biner untuk n bit.
# Kondisi: Ketika Anda perlu menghasilkan semua variasi dari nilai biner.
