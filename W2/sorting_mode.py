mode = input("Enter sorting mode A, B, C, D, E, F：")
numbers = [1, 3, 6.6, 3, 89, 37]
numbers.sort()
result = []

if mode == "A":
    print(numbers)

if mode == "B":
    for num in numbers:
        print(num)

if mode == "C":
    numbers.sort(reverse=True)
    print(numbers)

if mode == "D":
    numbers.sort(reverse=True)
    for num in numbers:
        print(num)

if mode == "E":
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)


if mode == "F":
    for i in numbers:
        smallest = numbers[0]
        for j in numbers:
            if j < smallest:
                smallest = j

        result.append(smallest)
        numbers.remove(smallest)

        print("result:", result)

    print("result:", result)



