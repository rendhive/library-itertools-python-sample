import itertools

counter = itertools.count(start=1, step=2)  # Mulai dari 1, langkah 2

print("Hitungan pertama 5 angka:")
for _ in range(5):
    print(next(counter), end=' ')
# Fungsi: Menghasilkan angka yang dihitung mulai dari nilai mulai dengan interval tertentu.
# Kondisi: Ketika Anda perlu menggenerasi angka berturut-turut secara tidak terbatas.
