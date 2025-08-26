distance = float(input("Distance(km): "))

if distance < 0:
    print("Masofa manfiy bo'la olmaydi!")
elif distance < 1:
    print("Piyoda yuring")
elif distance < 5:
    print("Velosiped yoki elektr skuter")
elif distance < 50:
    print("Avtobus yoki mashina")
else:
    print("Poyezd yoki samolyot")