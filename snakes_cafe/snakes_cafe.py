from urllib import response


def main():
    first_message = """
    $ python snakes_cafe.py
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************

    >> Enter "quit" to exit 
    >> Enter "meal" to display your order
    """
    print(first_message)


def functionality():
    rest_list = ["wings", "cookies", "spring Rolls", "salmon", "steak", "meat tornado", "a literal garden", "ice cream", "cake", "pie", "coffee", "tea", "unicorn tears"]
    counter = {item:0 for item in rest_list}
    
    
    while True:
        new_index = input("> ")
        if new_index in rest_list:
            counter[new_index] += 1
            print(f"\n** {counter[new_index]} order of {new_index} have been added to your meal **\n")
        elif new_index == "quit":
            break
        elif new_index == "meal":
            for i in [f"{key}: {val}" for key,val in counter.items() if val!=0]:
                print(i)
                
    
        else:
            print(f"The provided item \"{new_index}\" is not on the list.\n")
            while True:
                
                
                response = input("Do you want to order something else ? (yes/no) : ")
                if (response == "yes") or (response == "no"):
                    break
                else:
                    print("Select \"yes\" or \"no\"\n")
            if response == "no":
                break

print("\nThank you for ordering from our restaurant \n")                         
main()
functionality()



                                
