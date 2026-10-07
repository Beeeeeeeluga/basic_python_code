n = int(input("Enter a number："))

if n < 10:
    print("smaller")
if n > 10:
    print("Bigger")

if n > 0:
    for i in range(n, 0, -1):
        print(i)
print("Blastoff!")

