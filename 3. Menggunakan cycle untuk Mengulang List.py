import itertools

cycle_list = itertools.cycle(['A', 'B', 'C'])

print("Mengambil 10 elemen dari siklus:")
for _ in range(10):
    print(next(cycle_list), end=' ')
# Fungsi: Mengulang dan menghasilkan elemen dari list selamanya.
# Kondisi: Ketika Anda ingin mengulang elemen dalam list yang terbatas.
