import json


def customer_info():

    while True:

        print("""
        ----------------------------------------------
        Customer Sub-Menu:-

        1) Add Customer

        2) Available Customers

        3) Update Customer

        4) Delete Customer

        5) Back to Main Menu

        ----------------------------------------------
        """)
        choice = int(input('Enter a Menu option to continue:'))

        if choice == 1:

            add_customer()

            break

        elif choice == 2:

            view_customer()
        elif choice == 3:

            update_customer()

        elif choice == 4:

            delete_customer()

        elif choice == 5:
            from main import main_menu

            main_menu()

        else:
            print('INVALID MENU OPTION! Enter 1-5')

    exit()


def add_customer():
    # creating an empty dictionary
    cus_data = {}

    with open("cus.json", "r") as json_file:
        temp = json.load(json_file)

    cus_data["Customer_Name"] = input("\nEnter customer's full name: ")
    cus_data["Gender"] = input("\nEnter customer's gender: ")
    cus_data["Phone_Number"] = input("\nEnter customer's phone number: ")
    temp.append(cus_data)
    with open("cus.json", "w") as json_file:
        json.dump(temp, json_file, indent=4)
        print("\nCustomer Added successfully!")


def view_customer():
    with open("cus.json", "r") as json_file:
        temp = json.load(json_file)
        i = 1
        for entry in temp:
            cus_name = entry["Customer_Name"]
            gender = entry["Gender"]
            tel = entry["Phone_Number"]
            print(f"\nCustomerID: {i}")
            print(f"Name: {cus_name}")
            print(f"Gender: {gender}")
            print(f"Phone number: {tel}")
            print("\n")
            i = i + 1


def delete_customer():
    view_customer()
    sieved_data = []
    with open("cus.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        delete_opt = input(f"\nEnter Customer ID(1 - {data_length}) of the customer you want to delete:")
        i = 1
        for entry in temp:
            if i == int(delete_opt):
                pass
                i = i+1
            else:
                sieved_data.append(entry)
                i = i + 1
    with open("cus.json", "w") as json_file:
        json.dump(sieved_data, json_file, indent=4)
        print("\nCustomer deleted successfully!")


def update_customer():
    view_customer()
    updated_cus_list = []
    with open("cus.json", "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        update_opt = input(f"\nEnter Customer ID(1 - {data_length}) of the customer you want to update their data:")
        i = 1
        for entry in temp:
            if i == int(update_opt):
                cus_name = entry["Customer_Name"]
                gender = entry["Gender"]
                tel = entry["Phone_Number"]
                print(f"Name: {cus_name}")
                cus_name = input("Enter new customer's name: ")
                print(f"Gender: {gender}")
                gender = input("Enter new customer's gender: ")
                print(f"Phone number: {tel}")
                tel = input("Enter new customer's phone number: ")
                print("\n")
                updated_cus_list.append({"Customer_Name": cus_name, "Gender": gender, "Phone_Number": tel})
                i = i + 1
            else:
                updated_cus_list.append(entry)
                i = i + 1
    with open("cus.json", "w") as json_file:
        json.dump(updated_cus_list, json_file, indent=4)
        print("\nCustomer updated successfully!")


customer_info()
