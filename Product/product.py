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
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            add_product()

        elif choice == "2":

            view_product()

        elif choice == "3":

            update_product()

        elif choice == "4":

            delete_product()

        elif choice == "5":
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
            prod_data["Product_Price"] = int(input("\nEnter price: "))
        except ValueError:
            print(f"\nINVALID INPUT! Product price can't be an Alphabet")
            continue
        break

    while True:
        try:
            prod_data["Product_Quantity"] = int(input("\nEnter quantity: "))
        except ValueError:
            print(f"\nINVALID INPUT! Product quantity can't be an Alphabet")
            continue
        break
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
    with open("Product/prod.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        while True:
            # try:
            delete_opt = int(input(f"\nEnter Product ID(1 - {data_length}) of the product you want to delete:"))
            # except ValueError:
            #     print(f"\nINVALID INPUT! Product ID can't be an Alphabet")
            #     continue
            if delete_opt not in range(1, data_length):
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                break

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
            # try:
            update_opt = int(input(f"\nEnter Product ID(1 - {data_length})"
                                   f"of the product you want to update its data:"))
            # except ValueError:
            #     print(f"\nINVALID INPUT! Product ID can't be an Alphabet!")
            #     continue
            if update_opt not in range(1, data_length):
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
                print(f"Price: {prod_price}")
                while True:
                    try:
                        prod_price = int(input("\nEnter updated product price: "))
                    except ValueError:
                        print(f"\nINVALID INPUT! Product price can't be an Alphabet")
                        continue
                    break
                print(f"Quantity: {prod_qty}")
                while True:
                    try:
                        prod_qty = int(input("\nEnter updated product quantity: "))
                    except ValueError:
                        print(f"\nINVALID INPUT! Product quantity can't be an Alphabet")
                        continue
                    break
                updated_prod_list.append({"Product_Name": prod_name,
                                          "Product_Price": prod_price,
                                          "Product_Quantity": prod_qty})
                i = i + 1

            else:
                updated_prod_list.append(entry)
                i = i + 1

    with open("Product/prod.json", "w") as json_file:
        json.dump(updated_prod_list, json_file, indent=4)
        print("\nProduct updated successfully!")


# product_info()
