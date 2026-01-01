import itertools

numbers = iter(range(5))
iterator1, iterator2 = itertools.tee(numbers, 2)

print("Iterator 1:", list(iterator1))
print("Iterator 2:", list(iterator2))
# Fungsi: Membagi iterator menjadi beberapa iterators.
# Kondisi: Ketika Anda perlu membagikan satu iterator ke beberapa konsumen.
