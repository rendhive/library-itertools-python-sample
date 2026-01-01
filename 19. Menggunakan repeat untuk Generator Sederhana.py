import itertools

repeater = itertools.repeat(42, 5)

print("Mengulang angka 42 sebanyak 5 kali:")
for number in repeater:
    print(number, end=' ')
# Fungsi: Mengulang nilai tertentu beberapa kali.
# Kondisi: Ketika Anda ingin menghasilkan nilai tetap dalam jumlah tertentu.
