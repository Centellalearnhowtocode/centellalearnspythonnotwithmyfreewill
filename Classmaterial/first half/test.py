#Text
str = "Hello World"
print(str)

#Numeric data types
int = 42
print(int)
float = 3.14
print(float)
complex = 1 + 2j
print(complex)

#Sequence data types
list = [1, 2, 3, 4, 5]
print(list)
tuple = (1, 2, 3, 4, 5)
print(tuple)
range = range(1, 10)
print(range)

#Mapping data type
dict = {"name": "Alice", "age": 30, "city": "New York"}
print(dict)

#Boolean data type
bool_true = True
print(bool_true)
bool_false = False
print(bool_false)

#None data type
none_value = None
print(none_value)

#List
my_list = [1,2,3,4,5]
print(my_list)
list = [[1,2,3],[4,5,6],[7,8,9]]
print(list)
number = [1,3,2,9,4]
print(number[1])

#0 1 2 3 4....

#Modifying list
num = [1,3,2,9,4]
num[0]= 4
print(num)

#Adding items to a list
num1 = [1,3,2,9,4]
num1.append(100.8) #one number only can be decimal or whole number
num1.append(200)
num1.append(58)
print(num1)

#Insert items
num2 = [1,3,2,9,4]
num2.insert(2, 50.48) #index, value
print(num2) 

#Extend list
num3 = [1,3,2,9,4]
num3.extend([200,300.49,37,2018,29494,2983]) #multiple numbers
print(num3)

#Deleting items from a list
num4 = [00,11,22,33,44,55]
del num4[-1] #delete by index
print(num4)

num5 = [2,3,36,3,6]
num5.remove(3)
num5.remove(3)
print(num5)

#Tuples
rgb = ('red','green','blue','44')
print(rgb[0])
print(rgb[1])
print(rgb[2])
print(rgb[3])
print(rgb)

#List Comprehensions
numbers = [1,2,3,4,5]
square =[numbers]
print(numbers)