import json
prod_file = "Product/prod.json"
cus_file = "Customer/cus.json"


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
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            search_prod()

        elif choice == "2":

            print('-----Under construction-----')

        elif choice == "3":

            from main import main_menu

            main_menu()
        else:
            print('INVALID MENU OPTION! Enter 1-3')


# search for a product by name
def search_prod():
    while True:
        prod_name = input("\nEnter product name of product to search:")
        check = confirm_prod(prod_name)
        if check == 'y':
            break
        else:
            print("\nProduct does not exist. Please input an existing Product name")


def confirm_prod(prodcon_name):
    with open(prod_file, "r") as json_file:
        c_prod_temp = json.load(json_file)
    for entry in c_prod_temp:
        if prodcon_name in entry['Product_Name']:
            print(f"Product Name: {entry['Product_Name']}")
            print(f"Product Price: {entry['Product_Price']}")
            print(f"Product Quantity: {entry['Product_Quantity']}")
            return 'y'
        else:
            continue
    return
# search_here()
