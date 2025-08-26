import os

name = input("Fayl nomini kiriting: ")

if os.path.exists(name):
    print(f"Fayl '{name}' mavjud.")
else:
    print(f"Fayl '{name}' topilmadi.")
