# create a shopping cart program that will contiouasly ask the user for a food product and the price of thet product
# have an exit clouse if the user wishes to stop adding more things to their cart
# at the end show the food iterms and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy or press q to quit")
    if food.lower() == 'q':
        break # if the value of food enterd is q, then break
    else:
        price = float(input(f"enter the price of the{food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-------your cart------")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price

print("\n") # leaves a line   
print(f"your total is: R{total}")
    
        
