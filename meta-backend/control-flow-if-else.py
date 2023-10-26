# Week 1 example
# Displaying the menu
print("*** Menu ***")
print("cake: $2")
print("sandwich: $6")
print("banh mi: $1")

# Getting user input for quantities
cake = int(input("Please enter the quantity of cakes: "))
sandwich = int(input("Please enter the quantity of sandwiches: "))
banh_mi = int(input("Please enter the quantity of banh mi: "))

# Calculating the total bill
bill_total = cake * 2 + sandwich * 6 + banh_mi * 1

# Applying discounts based on the total bill amount
if bill_total > 10 and bill_total < 20: #10 < bill_total < 20:
    discount = 1
    print("Your bill is $" + str(bill_total) + ". You are eligible for a $" + str(discount) + " discount.")
    bill_total -= discount
    print("You need to pay: $" + str(bill_total))
elif bill_total >= 20:
    discount = 2
    print("Your bill is $" + str(bill_total) + ". You are eligible for a $" + str(discount) + " discount.")
    bill_total -= discount
    print("You need to pay: $" + str(bill_total))
else:
    print("Your bill is $" + str(bill_total) + ". You are not eligible for any discounts.")

