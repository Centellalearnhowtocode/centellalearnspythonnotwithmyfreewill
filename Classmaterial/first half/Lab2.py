#1.Using If Statement
age = input("Enter your age:")
if int(age)>=18:
  print("You are eligible to vote")

  #2.Using if else statement
age = int(input("Enter your age:"))
if age>=18:
  print("\nYou are eligible to vote")
else:
  print("\nYou are not eligible to vote.")

#3.Using if else if else statement
your_age = int(input("Enter your age: "))

#Determine the ticket price
if your_age <5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

print(f"You'll pay {ticket_price} USD for the ticket.")

#4.Using for loop with reange()
for index in range(5):
 print(index)

#5.Using for lopp with range() with specific increment
for index2 in range (0,11,2):
   print(f"\n{index2}")
#6.Using function
def greeting():
   print("\nHi")
#calling function
greeting()

#7.Using function with parameters
def greet(name):
   print(f"\nHi {name}")
#callinb function
greet("Vanda")

#8.Using function with parameters
def sum(a,b):
   return a+b
total = sum(10,20)
print(f"\n10+20 = {total}")

#9.Using List
colors = ["red","green","blue"]
print(colors)
coordinate = [[0,0],[100,100],[200,200]]
print(coordinate) 

#10.Assessing elements in a list
numbers = [1,3,2,7,9,4]
print(f"numbers = {numbers}")
print(f"index 1 = {numbers[1]}")
print(f"index -1 = {numbers[-1]}")
print(f"index -2= {numbers[-2]}")

#11.Modifying elements
numbers2 = [1,3,2,7,9,4]
print(f"numbers= {numbers2}")
numbers2[2]=10
print(f"modifited numbers = {numbers2}")

#12.Adding Elements to the list
numbers3 = [1,3,2,7,9,4]
print(f"numbers + {numbers3}")
numbers3.append(100)
print(f"Appended numbers = {numbers3}")

#13.Removinbg elements from a list
numbers4 = [1,3,2,7,9,4]
print(f"numbers = {numbers4}")
del numbers4[0]
print(f"numbers after deleted index 0 = {numbers4}")

numbers5 = [1,3,2,7,9,4]
print(f"numbers = {numbers5}")
numbers4.remove(9)
print(f"numbers after remve 0 = {numbers5}")

#14.Using Tuple
rgb = ('red','green','blue')
print(rgb[0])
print(rgb[1])
print(rgb[2])

#15.Using List comprehensions
numbers6 = [1,2,3,4,5]
print(f"numbers = {numbers6}")
squares = []
for number in numbers:
   squares.append(number**2)
print(f"Square using normal loop: {squares}")
squares = [numbers6**2 for number in numbers6]
print(f"Square using list comprehension :{squares}")