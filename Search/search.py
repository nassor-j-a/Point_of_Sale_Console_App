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

            cus_search()

        elif choice == "3":

            from main import main_menu

            main_menu()
        else:
            print('INVALID MENU OPTION! Enter 1-3')


# search for a product by name
def search_prod():
    while True:
        prod_name = input("\nEnter name of product to search:")
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


def cus_search():
    while True:
        print("""
                 ----------------------------------------------
                 Customer Search Sub-Menu:-

                 1) Search by Name
                 2) Search by Phone Number
                 3) Back to Search Sub-Menu

                 ----------------------------------------------
                 """)
        c_choice = input('Enter a Menu option to continue:')
        if c_choice == "1":
            search_cusname()
        elif c_choice == "2":
            search_cuspnum()
        elif c_choice == "3":
            search_here()
        else:
            print('INVALID MENU OPTION! Enter 1-3')


# search for customer by name
def search_cusname():
    while True:
        cus_name = input("\nEnter name of customer to search:")
        check = confirm_cusname(cus_name)
        if check == 'y':
            break
        else:
            print("\nCustomer not found! Please input an existing Customer name")


def confirm_cusname(cuscon_name):
    with open(cus_file, "r") as json_file:
        c_cus_temp = json.load(json_file)
    for entry in c_cus_temp:
        if cuscon_name in entry['Customer_Name']:
            print(f"Product Name: {entry['Customer_Name']}")
            print(f"Product Price: {entry['Gender']}")
            print(f"Product Quantity: {entry['Phone_Number']}")
            return 'y'
        else:
            continue
    return


# search for customer by phone number
def search_cuspnum():
    while True:
        cus_phone = input("\nEnter customer's Phone Number to search:")
        check = confirm_cuspnum(cus_phone)
        if check == 'y':
            break
        else:
            print("\nCustomer not found! Please input an existing Customer's Phone Number")


def confirm_cuspnum(cus_conphone):
    with open(cus_file, "r") as json_file:
        c_cus_temp = json.load(json_file)
    for entry in c_cus_temp:
        phon = entry['Phone_Number']
        phon = str(phon)
        if cus_conphone in phon:
            print(f"Product Name: {entry['Customer_Name']}")
            print(f"Product Price: {entry['Gender']}")
            print(f"Product Quantity: {entry['Phone_Number']}")
            return 'y'
        else:
            continue
    return
# search_here()
