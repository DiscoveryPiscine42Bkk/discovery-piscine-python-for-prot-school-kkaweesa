def main():
    user_input = input("Give me a number: ")
    number = float(user_input)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

if __name__ == "__main__":
    main()