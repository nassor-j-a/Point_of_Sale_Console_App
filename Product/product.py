import json


def product_info():
    while True:

        print("""
        ----------------------------------------------
        Product Sub-Menu:-

        1) Add Product

        2) Available Products

        3) Update Product

        4) Delete Product

        5) Back to Main Menu

        ----------------------------------------------
        """)
        choice = int(input('Enter a Menu option to continue:'))

        if choice == 1:

            add_product()

        elif choice == 2:

            view_product()

        elif choice == 3:

            update_product()

        elif choice == 4:

            delete_product()

        elif choice == 5:
            from main import main_menu

            main_menu()
        else:
            print('INVALID MENU OPTION! Enter 1-5')

    exit()


def add_product():
    # creating an empty dictionary
    prod_data = {}

    with open("prod.json", "r") as json_file:
        temp = json.load(json_file)

    prod_data["Product_Name"] = input("\nEnter product's name: ")
    prod_data["Product_Price"] = input("\nEnter price: ")
    prod_data["Product_Quantity"] = input("\nEnter quantity: ")
    temp.append(prod_data)
    with open("prod.json", "w") as json_file:
        json.dump(temp, json_file, indent=4)
        print("\nProduct Added successfully!")


def view_product():
    with open("prod.json", "r") as json_file:
        temp = json.load(json_file)
        i = 1
        for entry in temp:
            prod_name = entry["Product_Name"]
            prod_price = entry["Product_Price"]
            prod_qty = entry["Product_Quantity"]
            print(f"\nProductID: {i}")
            print(f"Product name: {prod_name}")
            print(f"Price: {prod_price}")
            print(f"Quantity: {prod_qty}")
            print("\n")
            i = i + 1


def delete_product():
    view_product()
    sieved_data = []
    with open("prod.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        delete_opt = input(f"\nEnter Product ID(1 - {data_length}) of the product you want to delete:")
        i = 1
        for entry in temp:
            if i == int(delete_opt):
                pass
                i = i + 1
            else:
                sieved_data.append(entry)
                i = i + 1
    with open("prod.json", "w") as json_file:
        json.dump(sieved_data, json_file, indent=4)
        print("\nProduct deleted successfully!")


def update_product():
    view_product()
    updated_prod_list = []
    with open("prod.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        update_opt = input(f"\nEnter Product ID(1 - {data_length}) of the product you want to update their data:")
        i = 1
        for entry in temp:
            if i == int(update_opt):
                prod_name = entry["Product_Name"]
                prod_price = entry["Product_Price"]
                prod_qty = entry["Product_Quantity"]
                print(f"Product name: {prod_name}")
                prod_name = input("Enter new product name: ")
                print(f"Price: {prod_price}")
                prod_price = input("Enter new product price: ")
                print(f"Quantity: {prod_qty}")
                prod_qty = input("Enter new product quantity: ")
                print("\n")
                updated_prod_list.append({"Product_Name": prod_name,
                                          "Product_Price": prod_price,
                                          "Product_Quantity": prod_qty})
                i = i + 1
            else:
                updated_prod_list.append(entry)
                i = i + 1
    with open("prod.json", "w") as json_file:
        json.dump(updated_prod_list, json_file, indent=4)
        print("\nProduct updated successfully!")


product_info()
