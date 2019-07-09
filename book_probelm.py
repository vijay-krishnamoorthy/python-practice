cover_price=650
shipping_cost=30
additional_cost=15
#cost per book will be


book_cost = cover_price+30+15
discount = book_cost/100*40
print(discount)
print("Cost per book is",book_cost)
##cost for 25 books is
whole_ship_cost = 25*book_cost
print("Total shipping cost for 25 books will be",whole_ship_cost)
