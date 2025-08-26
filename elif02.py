num1 = float(input("Son-1: "))
num2 = float(input("Son-2: "))
operator = input("Operator(+, -, *, /): ")

if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == '/':
    if num2 == 0:
        print("Nolga bo'lish mumkin emas!")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")