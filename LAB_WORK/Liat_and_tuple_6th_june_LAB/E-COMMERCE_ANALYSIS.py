#Detailes of orders
orders = [    
    ("Laptop", 55000),   
    ("Mouse", 800),  
    ("Keyboard", 1500),   
    ("Monitor", 12000),   
    ("Pen Drive", 600) ]
#Displaying all products costing more than 1000
print("Products costs more than 1000: ")
for item in orders:
    if orders[1]>1000:
        print(orders[0],orders[1])