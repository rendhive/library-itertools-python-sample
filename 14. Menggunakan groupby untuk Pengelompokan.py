import itertools

data = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('C', 5)]
grouped = itertools.groupby(data, key=lambda x: x[0])

print("Pengelompokan berdasarkan huruf:")
for key, group in grouped:
    print(key, list(group))
# Fungsi: Mengelompokkan elemen berdasarkan kriteria tertentu.
# Kondisi: Ketika Anda perlu mengelompokkan data berdasarkan atribut tertentu.
