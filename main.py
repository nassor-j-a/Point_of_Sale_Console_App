
def main_menu():
    while True:
        print("""
        ----------------------------------------------
        -----------------GROCERY SHOP-----------------
        ----------------------------------------------
        Menu:-
            1) Purchase 
            2) Product
            3) Customer
            4) Exit
        ----------------------------------------------
        """)

        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            from Order.process_order import p_order
            p_order()

        elif choice == "2":

            from Product.product import product_info
            product_info()

        elif choice == "3":

            from Customer.customer import customer_info
            customer_info()

        elif choice == "4":

            exit()

        else:
            print('\nINVALID OPTION! Enter 1 - 4!')
            main_menu()


main_menu()
