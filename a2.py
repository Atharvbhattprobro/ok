costprice =float(input("Enter the cp: "))
sellprice =float(input("Enter the sp: "))

if(sellprice>costprice):
    print("you have a profit")
    profit = sellprice - costprice
    print("your profit is :", profit)
else :
    print("you have a loss")
    loss= costprice-sellprice
    print("your loss is :", loss)
  