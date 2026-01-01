import itertools

count = itertools.count(start=1)

print("Mengambil 5 angka pertama dari hitungan:")
for number in itertools.islice(count, 5):
    print(number, end=' ')
# Fungsi: Mengambil bagian dari iterator berdasarkan indeks.
# Kondisi: Ketika Anda ingin mengambil elemen tertentu tanpa mengubah iterator asli.
