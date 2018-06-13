Quantity = int(input("Enter quantity:"))
if Quantity*100>1000:
    print("cost is",(Quantity*100)-(0.1*Quantity*100))
else:
    print("cost is",Quantity*100)