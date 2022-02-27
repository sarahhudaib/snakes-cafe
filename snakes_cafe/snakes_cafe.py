def restaurant_menu():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
  
    quit_rest= input("*** To quit at any time, type quit ***\n")
    if quit_rest == "quit":
        print("*******       Bye Bye           ******")
        print("**************************************")
    
    else:
       print("**************************************")
       print("**    Please see our menu below.    **")
       print("**************************************")
       
       print (appetizers())
       print (entrees())
       print (desserts())
       print (drinks())
       print (order_now())
 

def appetizers():
    print("\n")
    print("Appetizers")
    print("----------")
    appetizer_rest=["Wings","Cookies","Spring Rolls"]
    for i in appetizer_rest:
       print('\n'.join(appetizer_rest))
    
def entrees():
    print("\n")
    print("Entrees")
    print("-------")
    entrees_rest=["Salmon","Steak ","Meat Tornado","A Literal Garden"]
    for i in entrees_rest:
       print('\n'.join(entrees_rest))

def desserts():
    print("\n")
    print("Desserts")
    print("--------")
    desserts_rest=["Ice Cream","Cake ","Pie"]
    for i in desserts_rest:
       print('\n'.join(desserts_rest))

def drinks():
    print("\n")
    print("Drinks")
    print("------")
    drinks_rest=["Coffee","Tea ","Unicorn Tears"]
    for i in drinks_rest:
       print('\n'.join(drinks_rest))

def order_now():
    print("*** What would you like to order? ****")
    print("**************************************")
    oreder_rest= input("> ")


print (restaurant_menu())
