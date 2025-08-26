money = int(input("Qancha pul yechasiz: "))
balance = 5_000

if money <= 5_000:
    balance -= money
    print(f"Pul yechildi. Qolgan balans: {balance} so'm")
else:
    print("Mablag' yetarli emas. Sizning balansingiz: 5000 so'm")