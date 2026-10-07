###########################
###arithmetic operations###
###########################

a = 10; b = 4
print(a,b)


print(a+b)
14

print(a-b)
6

print(a*b)
40

print(a/b)
2.5

print(a/a)
1.0 #Division operation always yields float output

print(a%b)
2

print(a//b)
2

print(a**b)
10000


a=12; b=5;

a+=b
print(a)
17

a-=b
print(a)
12

a*=b
print(a)
60

a/=b
print(a)
12.0

a//=b
print(a)
2.0

a**=b
print(a)
32.0

a = int(a)
a%=b
print(a)
2


#Q1:please print "hello world" on the screen
print("Hello Python World!")

#Q2: Please print multiple lines of text on the screen
print('''Today is Thursday
This is the first python lecture
I want to learn programming1''')

#Q3: define two variables x and y, and x=3, y=4, z=x*y, please print the value of z on the screen.
x = 3
y = 4
z = x*y
print(z)

#Q4: please input a integer value for the variables x and y respectively, z= x*y, please print the value of z on the screen.
print('please input a value for x')
x = int(input('Please input an integer for x:'))
y = int(input('Please input an integer for y:'))
z = x*y
print(z)

#Q5: print more than one object:
print("hello","how are you")

#Q6: ask for a user's name and print it
print('Enter your name:')
x = input()
print('Hello, ' + x)

#Q7: Use the prompt parameter to write a message before the input:
x = input('Enter your name:')
print('Hello, ' + x)

#Q8: calculate an area of a circle
pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

#Q9: change the value of radius and print the area of the new circle
# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)

#Q10: practice comments
#############################
#### COMMENTING LINES #######
#############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!

#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1

# use autocomplete to write a line that prints the value of that long variable
# notice that Spyder also automatically adds the closed parentheses for you!
####################
##### variables ####
####################
#Q1 Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

#Q2 Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Q3 If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Q4 You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

#Q5 String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

#Q6 Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a

#Q7 Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Q8 And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Q8 In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Q9 You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Q10 For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#Q11 In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)

#Q12 The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)


####################
#####  string   ####
####################

#Q1 declares book as The Great Gatsby and then modifies the variable value to Beloved.

book = "The Great Gatsby"
print(book)
book = "Beloved"
print(book)

#Q2 The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#Q3 Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Q4 Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Q5 Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


#Q6 Use negative indexes to start the slice from the end of the string:
#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

#Q7 The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#Q8 The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#Q9 The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Q10 Merge variable a with variable b into variable c
a = "Hello"
b = "World"
c = a + b
print(c)


#Q11 To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Q12 As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)

#Q13 Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Q14 The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#Q15 You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



# Q16 s = "abc"
# index 0 1 2 <-- indexing always starts at 0
# index -3 -2 -1 <-- last element always at index -1
