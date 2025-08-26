weight = float(input("Vazn(kg): "))
height = float(input("Buy uzunligi(m): "))

bmi = weight / pow(height, 2)
print("BMI darajagiz: ", bmi)

if bmi < 18.5:
    print("Kam vazn")
elif bmi < 25:
    print("Normal vazn")
elif bmi < 30:
    print("O'rtacha vazn")
else:
    print("Semizlik")