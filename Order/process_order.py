def p_order():
    while True:
        print("""
        ----------------------------------------------
        Order Sub-Menu:-

        1) Process an order

        2) Processed order(s)

        3) Back to Main Menu

        ----------------------------------------------
        """)
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            print('-----Under construction-----')
        elif choice == "2":

            print('-----Under construction-----')
        elif choice == "3":
            from main import main_menu

            main_menu()
        else:
            print('INVALID MENU OPTION! Enter 1-3')


p_order()
