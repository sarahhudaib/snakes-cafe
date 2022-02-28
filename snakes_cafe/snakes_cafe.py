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
    food_list = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
    orders_list = {}
    counter = 0
    while(True):
        
        user_input = input(">").lower()
        if user_input == "quit":
            break
        
        elif user_input in food_list:
            if user_input in orders_list:
                counter += 1
                
            else:
                counter = 1
                orders_list.update({user_input: counter})
                # orders_list.append(user_input)
                print(f'\n** {counter} order of {user_input} have been added to your meal**\n')
                
                
        # handeling the error of choosing an item not been added to the list
        else:
            print(f"The Product ({user_input}) that you entered is invalid. Please try again.\n")
            while True:
                check = input("Would you like to order anything else? (y/n) : ")
                if (check == "y") or (check == "n"):
                    break
                else:
                    print("Please select \"y\" or \"n\"\n")
                    if check == "n":
                        break

                                

                                
main()
functionality()



                                
