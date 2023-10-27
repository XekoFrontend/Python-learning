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
# loyalty_customer = int(input("How many time do you buy on our store: "))
# If loyalty_customer >= 5 the customer is eligible $0.5 for total bill
# loyalty_customer = True

# Calculating the total bill
discount_1 = 1
discount_2 = 2
bill_total = cake * 2 + sandwich * 6 + banh_mi * 1

# Applying discounts based on the total bill amount
if bill_total > 10 and bill_total < 20:  # 10 < bill_total < 20:
    print("Your bill is $" + str(bill_total) +
          ". You are eligible for a $" + str(discount_1) + " discount.")
    bill_total -= discount_1
elif bill_total >= 20:

    print("Your bill is $" + str(bill_total) +
          ". You are eligible for a $" + str(discount_2) + " discount.")
    bill_total -= discount_2
else:
    print("Your bill is $" + str(bill_total) +
          ". You are not eligible for any discounts.")

# Notify the amount payable after the reduction for all total bill levels.
print("You need to pay: $" + str(bill_total))

# Todo: If the total bill exceeds $50, a reduction of $0.1 will be applied to each item. "If the customer is loyal, reduce an additional $0.5 from the total bill.

# loyalty_customer = True
# total_bill = 124

# if loyalty_customer and total_bill > 100:
#     #give 20% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 20
# elif total_bill > 100:
#     #give 10% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 10
# else:
#     #sorry no discount, 5% service charge applied.
#     print('Sorry, no discount ...')

# print('Total Bill: ', float(total_bill))
