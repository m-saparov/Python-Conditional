email = input("Email: ")

if '@' in email and (email[-4:] == '.com' or email[-4:] == '.net' or email[-4:] == '.org' or email[-3:] == '.uz'):
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")