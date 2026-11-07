age = int(input("Enter your age: "))
adult = 100_000
old = 60_000
ticket = "Free" if 0 < age <= 6 else "Cost money"
print(ticket)
if 0 < age < 6:
    print("Kid ticket.")
elif 6 < age < 17:
    print("500_000VNĐ for student.")
elif 18 <= age < 60:
    print(f"{adult}VNĐ for adult.")
else:
    print(f"{old}VNĐ for old people.")