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
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            add_customer()

        elif choice == "2":

            view_customer()

        elif choice == "3":

            update_customer()

        elif choice == "4":

            delete_customer()

        elif choice == "5":
            from main import main_menu

            main_menu()

        else:
            print('INVALID MENU OPTION! Enter 1-5')


def add_customer():
    # creating an empty dictionary
    cus_data = {}

    with open("cus.json", "r") as json_file:
        temp = json.load(json_file)

    cus_data["Customer_Name"] = input("\nEnter customer's full name: ")
    while True:
        try:
            gender_rec = int(input("\nSelect 1 if customer is Male and 2 if customer is Female: "))
        except ValueError:
            print(f"\nINVALID INPUT! Selection can't be an Alphabet")
            continue
        if gender_rec == 1:
            cus_data["Gender"] = "Male"
            break
        elif gender_rec == 2:
            cus_data["Gender"] = "Female"
            break
        else:
            print("\nINVALID INPUT! Please enter 1 or 2!")

    while True:
        try:
            cus_data["Phone_Number"] = int(input("\nEnter customer's phone number: "))
        except ValueError:
            print("\nINVALID INPUT! Customer's phone number can't be an alphabet")
            continue
        break
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
        while True:
            try:
                delete_opt = int(input(f"\nEnter Customer ID(1 - {data_length}) of the customer you want to delete:"))
            except ValueError:
                print(f"\nINVALID INPUT! Customer ID can't be an Alphabet")
                continue
            if delete_opt > data_length:
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                break

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
        while True:
            try:
                update_opt = int(input(f"\nEnter Customer ID(1 - {data_length})"
                                       f"of the customer you want to update their data:"))
            except ValueError:
                print(f"\nINVALID INPUT! Customer ID can't be an Alphabet!")
                continue
            if update_opt > data_length:
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                break

        i = 1
        for entry in temp:
            if i == int(update_opt):
                cus_name = entry["Customer_Name"]
                gender = entry["Gender"]
                tel = entry["Phone_Number"]
                print(f"Name: {cus_name}")
                cus_name = input("Enter updated customer's name: ")
                print(f"Gender: {gender}")
                while True:
                    try:
                        gender_rec = int(input("\nEnter 1 if customer gender is Male and 2 if Female: "))
                    except ValueError:
                        print(f"\nINVALID INPUT! Entered value can't be an Alphabet")
                        continue
                    if gender_rec == 1:
                        gender = "Male"
                        break
                    elif gender_rec == 2:
                        gender = "Female"
                        break
                    else:
                        print("\nINVALID INPUT!")
                print(f"Phone number: {tel}")
                while True:
                    try:
                        tel = int(input("\nEnter updated customer's phone number: "))
                        print("\n")
                    except ValueError:
                        print("\nINVALID INPUT! Customer's phone number can't be an alphabet")
                        continue
                    break
                updated_cus_list.append({"Customer_Name": cus_name, "Gender": gender, "Phone_Number": tel})
                i = i + 1
            else:
                updated_cus_list.append(entry)
                i = i + 1
    with open("cus.json", "w") as json_file:
        json.dump(updated_cus_list, json_file, indent=4)
        print("\nCustomer updated successfully!")


customer_info()
