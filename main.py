def main_menu():

    while True:
        print("""
        ----------------------------------------------
        -----------------GROCERY SHOP-----------------
        ----------------------------------------------
        Menu:-

        1) Order

        2) Product

        3) Customer

        4) Search

        5) Exit
        ----------------------------------------------
        """)

        try:
            choice = int(input('Enter a Menu option to continue:'))

            if choice == 1:

                from Order.process_order import p_order
                p_order()

                # To avoid continuous looping
                break

            elif choice == 2:

                from Product.product import product_info

                product_info()

                break

            elif choice == 3:

                from Customer.customer import customer_info

                customer_info()

                break

            elif choice == 4:

                from search import search_here

                search_here()

                break

            elif choice == 5:

                # exit can't be here, the loop will still execute
                break

            else:
                print('INVALID OPTION! Enter 1 - 4!')
                main_menu()

        except ValueError:

            print('System does not recognize alphabets! Enter 1 - 4!')
    exit()


main_menu()
