quantity = int(input("Enter the quanity："))
itemno = int(input("Enter the number of items："))
price = int(input("Enter the price of items："))
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))
