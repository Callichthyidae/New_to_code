number = int(input("Enter a number: "))
match number:
    case n if n < 5:
        print(f"{number} smaller than 5")
    case n if n > 5:
        print(f"{number} bigger than 5")
    case _:
        print("5 is equal to 5")