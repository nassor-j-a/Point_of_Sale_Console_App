import json
from rich.console import Console
from rich.table import Table


def product_info():
    while True:

        print("""
        ----------------------------------------------
        Product Sub-Menu:-

        1) Add Product
        2) List Products
        3) Search Product
        4) Update Product
        5) Delete Product
        6) Back to Main Menu

        ----------------------------------------------
        """)
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            add_product()

        elif choice == "2":

            view_product()

        elif choice == "3":

            search_prod()

        elif choice == "4":

            update_product()

        elif choice == "5":

            delete_product()

        elif choice == "6":
            from main import main_menu

            main_menu()
        else:
            print('\nINVALID MENU OPTION! Enter 1-5')


def add_product():
    # creating an empty dictionary
    prod_data = {}

    with open("Product/prod.json", "r") as json_file:
        temp = json.load(json_file)

    prod_data["Product_Name"] = input("\nEnter product's name: ")

    while True:
        try:
            prod_data["Product_Quantity"] = int(input("\nEnter quantity: "))
        except ValueError:
            print(f"\nINVALID INPUT! Product quantity can't be an Alphabet")
            continue
        break
    while True:
        try:
            p_price = int(input("\nEnter price: "))
        except ValueError:
            print(f"\nINVALID INPUT! Product price can't be an Alphabet")
            continue
        prod_data["Product_Price"] = '{:.2f}'.format(p_price)
        break
    while True:
        add_ver = input("\nDo you really want to add customer? y/n: ")
        if add_ver == 'y':
            break
        elif add_ver == 'n':
            product_info()
        else:
            print("\nINVALID INPUT! Enter y/n")
            continue
    temp.append(prod_data)
    with open("Product/prod.json", "w") as json_file:
        json.dump(temp, json_file, indent=4)
        print("\nProduct Added successfully!")


def view_product():
    with open("Product/prod.json", "r") as json_file:
        temp = json.load(json_file)
        i = 1
        for entry in temp:
            prod_name = entry["Product_Name"]
            prod_qty = entry["Product_Quantity"]
            prod_price = entry["Product_Price"]
            print(f"ProductID: {i}")
            print(f"Product name: {prod_name} , Quantity: {prod_qty}, Price: Ksh. {prod_price}")
            i = i + 1


def delete_product():
    view_product()
    sieved_data = []
    with open("Product/prod.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        while True:
            try:
                delete_opt = int(input(f"\nEnter Product ID(1 - {data_length}) of the product you want to delete:"))
            except ValueError:
                print(f"\nINVALID INPUT! Product ID can't be an Alphabet")
                continue
            if delete_opt > data_length:
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                break
        while True:
            upd_ver = input("\nDo you really want to delete the product? y/n: ")
            if upd_ver == 'y':
                break
            elif upd_ver == 'n':
                product_info()
            else:
                print("\nINVALID INPUT! Enter y/n")
                continue

        i = 1
        for entry in temp:
            if i == int(delete_opt):
                pass
                i = i + 1
            else:
                sieved_data.append(entry)
                i = i + 1
    with open("Product/prod.json", "w") as json_file:
        json.dump(sieved_data, json_file, indent=4)
        print("\nProduct deleted successfully!")


def update_product():
    view_product()
    updated_prod_list = []
    with open("Product/prod.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        while True:
            try:
                update_opt = int(input(f"\nEnter Product ID(1 - {data_length})"
                                       f"of the product you want to update its data:"))
            except ValueError:
                print(f"\nINVALID INPUT! Product ID can't be an Alphabet!")
                continue
            if update_opt > data_length:
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                break
        i = 1
        for entry in temp:
            if i == int(update_opt):
                prod_name = entry["Product_Name"]
                prod_price = entry["Product_Price"]
                prod_qty = entry["Product_Quantity"]
                print(f"Product name: {prod_name}")
                prod_name = input("Enter updated product name: ")
                print(f"Quantity: {prod_qty}")
                while True:
                    try:
                        prod_qty = int(input("\nEnter updated product quantity: "))
                    except ValueError:
                        print(f"\nINVALID INPUT! Product quantity can't be an Alphabet")
                        continue
                    break
                print(f"Price: Ksh. {prod_price}")
                while True:
                    try:
                        updtprod_price = int(input("\nEnter updated product price: "))
                    except ValueError:
                        print(f"\nINVALID INPUT! Product price can't be an Alphabet")
                        continue
                    prod_price = '{:.2f}'.format(updtprod_price)
                    break
                while True:
                    upd_ver = input("\nDo you really want to update the product details? y/n: ")
                    if upd_ver == 'y':
                        break
                    elif upd_ver == 'n':
                        product_info()
                    else:
                        print("\nINVALID INPUT! Enter y/n")
                        continue
                updated_prod_list.append({"Product_Name": prod_name,
                                          "Product_Quantity": prod_qty,
                                          "Product_Price": prod_price})
                i = i + 1

            else:
                updated_prod_list.append(entry)
                i = i + 1

    with open("Product/prod.json", "w") as json_file:
        json.dump(updated_prod_list, json_file, indent=4)
        print("\nProduct updated successfully!")


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
    with open("Product/prod.json", "r") as json_file:
        c_prod_temp = json.load(json_file)
    for entry in c_prod_temp:
        if prodcon_name in entry['Product_Name']:
            print(f"Product Name: {entry['Product_Name']}")
            print(f"Product Quantity: {entry['Product_Quantity']}")
            print(f"Product Price: {entry['Product_Price']}")
            return 'y'
        else:
            continue
    return


# product_info()
