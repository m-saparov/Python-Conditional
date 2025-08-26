score = int(input("Test score: "))

if 0 >= score and score >= 100:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")
elif score >= 90:
    print("A (A'lo)")
elif score >= 80:
    print("B (Yaxshi)")
elif score >= 70:
    print("C (Qoniqarli)")
elif score >= 60:
    print("D (Qoniqarsiz)")
else:
    print("F (Rad)")