number = int(input("Enter a number less than 25\n"))
if number > 25:
    print("Error")
else:
    while number <= 30:
        print(f"Inside the loop, my variable is {number}")
        number += 1