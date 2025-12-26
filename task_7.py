user_number = int(input("Enter a number between 1000 and 9999: "))

if user_number < 1000 or user_number > 9999:
    print(f"Sorry, the number {user_number} is less than 1000 or greater than 9999.")
    print("Please try again and enter a number between 1000 and 9999.")
else:
    number_1 = user_number // 1000
    number_2 = user_number // 100 % 10
    number_3 = user_number // 10 % 10
    number_4 = user_number % 10

    print(f"{number_1}\n{number_2}\n{number_3}\n{number_4}")
