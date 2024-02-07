
fruit_shop = {}

menu="""
              WELCOME TO FRUIT MARKET

            1) Manager
            2) Customer 

"""
status=True
while status:
    print(menu)
    print("\nfruit market manager\n")
    print("1) add fruit stock :")
    print("2) view fruit stock :")
    print("3) update fruit stock :")

    choice=int(input("enter your choice :"))

    if choice==1:
        print("\nADD FRUIT STOCK :")
        fruit_name=input("enter a fruit name :")
        qty=input("enter fruit qty (in kg) :")
        price=input("enter fruit price (for kg) :")

        if fruit_name in fruit_shop:
            fruit_shop[fruit_name]['qty'] += int(qty)
            fruit_shop[fruit_name]['price'] +=int(price)

        else:
            fruit_shop[fruit_name]={'qty' : int(qty),'price' : int(price)}

    elif choice==2:
        print("\nVIEW FRUIT STOCK :")
        for fruit, item in fruit_shop.items():
            print(f"(fruit): {fruit}, qty:{item['qty']}, price:{item['price']}")

    elif choice==3:
        print("\nUPDATE FRUIT STOCK :")

    new_choice=input("do you want to add more fruit stock press y for yes and press n for no :")
    if new_choice=='y':
        status=True
    else:
        status=False    
        
        
   
       

    


