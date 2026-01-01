import itertools

colors = ['red', 'green']
sizes = ['S', 'M', 'L']
product = itertools.product(colors, sizes)

print("Produk Cartesius dari warna dan ukuran:")
for item in product:
    print(item)
# Fungsi: Menghasilkan produk dari beberapa iterable.
# Kondisi: Ketika Anda ingin mendapatkan kombinasi dari elemen dari beberapa set.
