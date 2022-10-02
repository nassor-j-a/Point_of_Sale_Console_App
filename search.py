def search_here():
    while True:
        print("""
         ----------------------------------------------
         Search Sub-Menu:-

         1) Search for Product

         2) Search for Customer

         3) Back to Main Menu

         ----------------------------------------------
         """)
        choice = int(input('Enter a Menu option to continue:'))

        if choice == 1:

            print('-----Under construction-----')

        elif choice == 2:

            print('-----Under construction-----')

        elif choice == 3:

            from main import main_menu

            main_menu()
        else:
            print('INVALID MENU OPTION! Enter 1-3')
    exit()


search_here()
