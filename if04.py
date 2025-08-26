age = int(input("Age: "))

price = 100

if age < 0:
    print("Yosh xato kiritilgan!")

if 0 < age and age < 7:
    price *= 0.5
elif 7 <= age and age < 17:
    price *= 0.8
elif age > 60:
    price *= 0.7

print("Yakuniy narx: ", price)