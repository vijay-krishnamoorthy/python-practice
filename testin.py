l = [{'order number': 12354, 'title': 'Computer Pogramming', 'quantity': 5, 'price': 449},{'order number': 12355, 'title': 'Pogramming for beginners', 'quantity': 8, 'price': 649},{'order number': 12356, 'title': 'Computer Basics', 'quantity': 3, 'price': 179}]
prod=lambda x,y: x*y
listt=[]

for i in l:
    temp = []
    temp.append(i['title'])
    temp.append(prod(i['quantity'], i['price']))
    listt.append(tuple(temp))

print(listt)

