while True:    
    try:
        age = int(input("age:"))
        if age <= 0:
            print("Age cannot be smaller or equal than 0!")
            continue
        elif age >= 120:
            print("human cant live that long!")
            continue
        elif age < 18 or age > 65:
            print("free admission")
            break
        else:
            while True:
                card = input("Do you have student card? (yes/no)").lower()
                if card not in ["yes","no"]:
                    print("Invalid input! Enter (yes/no)")
                    continue
                elif card == "yes":
                    print("student admission: price is 50HKD")
                    break
                else:
                    print("Regular admission: 100HKD")
                    break
    except ValueError:
        print("Invalid input! Please enter an integer!")
        continue
