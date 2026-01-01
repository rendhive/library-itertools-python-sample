import itertools

colors = ['red', 'green', 'blue']
color_cycle = itertools.cycle(colors)

print("Mengambil 6 warna dari siklus:")
for _ in range(6):
    print(next(color_cycle), end=' ')
# Fungsi: Menggunakan siklus untuk mengulang elemen secara tidak terbatas.
# Kondisi: Ketika Anda membutuhkan warna atau nilai lain yang diulang terus menerus.
