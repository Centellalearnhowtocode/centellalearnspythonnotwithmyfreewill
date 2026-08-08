#3.Using if else if else statement
your_age = int(input("Enter your age: "))

#Determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18
#Showing the ticket price
print(f"You'll pay {ticket_price}USD for the ticket.")