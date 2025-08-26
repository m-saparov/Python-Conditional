number = int(input("Number: "))

template = "{} soni {} ga bo'linadi"

if number % 2 == 0:
    print(template.format(number, 2))

if number % 3 == 0:
    print(template.format(number, 3))

if number % 5 == 0:
    print(template.format(number, 5))