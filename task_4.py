price = int(input("Enter your price: "))
discount = int(input("Enter your discount: "))

print(f"Your price with discount: {price - (price * discount / 100)}")