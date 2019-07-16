units_used = int(input('Enter the no of units consumed by the customer :'))
service_tax=1.5
if(units_used <= 100):
    bill_amount=units_used*service_tax*1
    print("The Electricity bill amount with TAX is",bill_amount)
elif(units_used <= 200):
    bill_amount = units_used*service_tax*1.5
    print("The Electricity bill amount with TAX is", bill_amount)
elif(units_used <= 500):
    bill_amount = units_used*service_tax*3
    print("The Electricity bill amount with TAX is", bill_amount)
else:
    bill_amount = units_used*service_tax*5
    print("The Electricity bill amount with TAX is", bill_amount)
