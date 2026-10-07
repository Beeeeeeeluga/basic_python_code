while True:
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Number cannot be smaller than 0!")
            continue

        elif number > 50:
            print("Number cannot be greater than 50!")
            continue

        else:
            for i in range(1, number + 1):
                print(" " * (number - i) + "*" * (2 * i - 1))
            break

    except ValueError:
        print("Invalid input! Please enter an integer!")
        continue