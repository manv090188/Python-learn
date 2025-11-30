#Case: There is a shopping cart having a few products. write a program to calcualte the sum of the prices in the shooping cart.

#prices is the list of all the prices in the shopping cart
prices = [10, 20, 30, 40]
#total_amount is the varaible which has zero value
total_amount = 0
#for loop runs listing all the prices in the prices variable one by one and total_amount which was initially zero gets added by next price.
for list in prices:
    total_amount = total_amount + list
print(f"The total of the prices in the shopping cart is Rs.{total_amount}/-")