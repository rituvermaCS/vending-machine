import time
print ("Welcome Sir!.")

no_1 = int(input("How many 1 rupee coins you would insert: "))
while no_1 < 0:
    no_1 = int(input("Please enter a valid no.:"))
    
no_2 = int(input("How many 2 rupee coins you would insert: "))
while no_2 < 0:
    no_2 = int(input("Please enter a valid no.:"))
    
no_3 = int(input("How many 5 rupee coins you would insert: "))
while no_3 < 0:
    no_3 = int(input("Please enter a valid no.:"))
    
no_4 = int(input("How many 10 rupee coins you would insert: "))
while no_4 < 0:
    no_4 = int(input("Please enter a valid no.:"))
    
change = round(((no_1 * 1) + (no_2 * 2) + (no_3 * 5) + (no_4 * 10)),2)
print ("\nTotal Rupees", change)

time.sleep(2)
pro1, pro1_price = "Dairy Milk", 20
pro2, pro2_price = "Kitkat", 20
pro3, pro3_price = "Munch", 10
pro4, pro4_price = "Milky Way", 20
pro5, pro5_price = "Perk", 10

dairy_milk_bought = 0
kitkat_bought = 0
munch_bought = 0
milky_ways_bought = 0
perk_bought = 0

print ("There are 5 Choclate product available to pick one:\n")
time.sleep(2)
print ("Item: {}, Price {} ".format(pro1, pro1_price))
print ("Item: {}, Price {} ".format(pro2, pro2_price))
print ("Item: {}, Price {} ".format(pro3, pro3_price))
print ("Item: {}, Price {} ".format(pro4, pro4_price))
print ("Item: {}, Price {} ".format(pro5, pro5_price))
print ("")

while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n")
    if customer_choice == "Dairy Milk" and change >= pro1_price:
        print ("You have chosen a", pro1, "these cost", pro1_price, "each,")
        change = round((change - pro1_price),2)
        dairy_milk_bought = (dairy_milk_bought + 1)
        print ("You have this much money remaining: ", change)
    elif customer_choice == "Kitkat" and change >= pro2_price:
        print ("You have chosen a", pro2, "these cost", pro2_price, "each,")
        change = round((change - pro2_price),2)
        kitkat_bought = (kitkat_bought + 1)
        print ("You have this much money remaining: ", change)
    elif customer_choice == "Munch" and change >= pro3_price:
        print ("You have chosen a", pro3, "these cost", pro3_price, "each,")
        change = round((change - pro3_price),2)
        munch_bought = (munch_bought + 1)
        print ("You have this much money remaining: ", change)
    elif customer_choice == "Milky Way" and change >= pro4_price:
        print ("You have chosen a", pro4, "these cost", pro4_price, "each,")
        change = round((change - pro4_price),2)
        milky_ways_bought = (milky_ways_bought + 1)
        print ("You have this much money remaining: ", change)
    elif customer_choice == "Perk" and change >= pro5_price:
        print ("You have chosen a", pro5, "these cost", pro5_price, "each,")
        change = round((change - product_5_price),2)
        perk_bought = (perk_bought + 1)
        print ("You have this much money remaining: ", change)
    elif customer_choice == "n":
        print ("\nHere is your transaction details")
        print ("")
        print ("You purchased: ")
        print (pro1, "x", dairy_milk_bought)
        print (pro2, "x", kitkat_bought)
        print (pro3, "x", munch_bought)
        print (pro4, "x", milky_ways_bought)
        print (pro5, "x", perk_bought)
        print ("You have ", change, "remaining.")
        break
    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (pro1, "x", dairy_milk_bought)
        print (pro2, "x", kitkat_bought)
        print (pro3, "x", munch_bought)
        print (pro4, "x", milky_ways_bought)
        print (pro5, "x", perk_bought)
        break
    else:
        print ("There has been an error or you may not have enough Rupees.")