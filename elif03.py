clock = int(input("Soat(0-23): "))

if 0 > clock and clock > 23:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")
elif 5 <= clock and clock < 12:
    print("Ertalab")
elif 12 <= clock and clock < 18:
    print("Kunduzi")
elif 18 <= clock and clock <= 21:
    print("Kechqurun")
else:
    print("Tun")