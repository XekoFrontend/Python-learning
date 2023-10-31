BOOK_PRICE = 100
DISCOUNT_PERCENTAGE = 10

print(f"If you buy more than 10 books, you will receive a 10% discount")
cart = int(input("Add to cart: " ))

if cart > 0 or cart <= 10:
  total = cart * BOOK_PRICE
  print("Total: " + str(total) + "$")
elif cart > 10:
  discount = (10 * 100) + ((cart - 10) * 90)
  print(str(discount))
else:
  input("Your cart has no books.\nAdd to cart: ")


