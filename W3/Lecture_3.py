try:
    age = int(input("age:"))
    if age <= 0:
        print("Age cannot be smaller or equal than 0!")
    elif age >= 120:
        print("human cant live that long!")
    else:
        card = input("Do you have student card? (yes/no)")
        if age < 18 or age > 65:
            print("free admission")
        elif card == "yes":
            print("student admission: price is 50HKD")
        else:
            print("Regular admission: 100HKD")

except ValueError:
    print("Invalid input! Please enter an integer!")