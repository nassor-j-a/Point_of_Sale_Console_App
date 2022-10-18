import json
import re


def customer_info():

    while True:

        print("""
        ----------------------------------------------
        Customer Sub-Menu:-

        1) Add Customer
        2) List Customers
        3) Search Customer
        4) Update Customer
        5) Delete Customer
        6) Back to Main Menu

        ----------------------------------------------
        """)
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            add_customer()

        elif choice == "2":

            view_customer()

        elif choice == "3":

            cus_search()

        elif choice == "4":

            update_customer()

        elif choice == "5":

            delete_customer()

        elif choice == "6":
            from main import main_menu

            main_menu()

        else:
            print('INVALID MENU OPTION! Enter 1-5')


def add_customer():
    # creating an empty dictionary
    cus_data = {}

    with open("Customer/cus.json", "r") as json_file:
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
        mail = input("\nEnter customer's email:")
        confirm_format = checky(mail)
        if confirm_format == 'y':
            cus_data["Email"] = mail
            break
        else:
            print("\nINVALID EMAIL FORMAT! Email format must be of: \"username@company.domain\"")
            continue

    while True:
        ftel_in = input("\nEnter customer's phone number:  ")
        confirm_pformat = check_numformat(ftel_in)
        if confirm_pformat == 'y':
            cus_data["Phone_Number"] = ftel_in
            break
        else:
            print("\nINVALID PHONE NUMBER FORMAT! Enter values (0-9) and 10 digits long!")
            continue

    temp.append(cus_data)
    with open("Customer/cus.json", "w") as json_file:
        json.dump(temp, json_file, indent=4)
        print("\nCustomer Added successfully!")


def view_customer():
    with open("Customer/cus.json", "r") as json_file:
        temp = json.load(json_file)
        i = 1
        for entry in temp:
            cus_name = entry["Customer_Name"]
            gender = entry["Gender"]
            mail = entry["Email"]
            tel = entry["Phone_Number"]
            print(f"CustomerID: {i}")
            print(f"Name: {cus_name}, Gender: {gender}, Email: {mail}, Phone number: {tel}")
            i = i + 1


def delete_customer():
    view_customer()
    sieved_data = []
    with open("Customer/cus.json", "r") as json_file:
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
                i = i + 1
            else:
                sieved_data.append(entry)
                i = i + 1

    with open("Customer/cus.json", "w") as json_file:
        json.dump(sieved_data, json_file, indent=4)
        print("\nCustomer deleted successfully!")


def update_customer():
    view_customer()
    updated_cus_list = []
    with open("Customer/cus.json", "r") as json_file:
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
                mail = entry["Email"]
                tel = entry["Phone_Number"]
                print(f"\nName: {cus_name}")
                cus_name = input("Enter updated customer's name: ")
                print(f"\nGender: {gender}")
                while True:
                    try:
                        gender_rec = int(input("Enter 1 if customer gender is Male and 2 if Female: "))
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
                print(f"\nEmail: {mail}")
                while True:
                    mail_in = input("Enter updated customer's email:")
                    confirm_format = checky(mail_in)
                    if confirm_format == 'y':
                        mail = mail_in
                        break
                    else:
                        print("\nINVALID EMAIL FORMAT! Email format must be of: \"username@company.domain\"")
                        continue
                print(f"\nPhone number: {tel}")
                while True:
                    tel_in = input("Enter updated customer's phone number: ")
                    confirm_pformat = check_numformat(tel_in)
                    if confirm_pformat == 'y':
                        tel = tel_in
                        break
                    else:
                        print("\nINVALID PHONE NUMBER FORMAT! Enter values (0-9) and 10 digits long!")
                        continue
                updated_cus_list.append({"Customer_Name": cus_name, "Gender": gender, "Email": mail,
                                         "Phone_Number": tel})
                i = i + 1
            else:
                updated_cus_list.append(entry)
                i = i + 1
    with open("Customer/cus.json", "w") as json_file:
        json.dump(updated_cus_list, json_file, indent=4)
        print("\nCustomer updated successfully!")


def cus_search():
    while True:
        print("""
             ----------------------------------------------
             Customer Search Sub-Menu:-

             1) Search by Name
             2) Search by Phone Number
             3) Back to Customer Sub-Menu

             ----------------------------------------------
                 """)
        c_choice = input('Enter a Menu option to continue:')
        if c_choice == "1":
            search_cusname()
        elif c_choice == "2":
            search_cuspnum()
        elif c_choice == "3":
            customer_info()
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
    with open("Customer/cus.json", "r") as json_file:
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
    with open("Customer/cus.json", "r") as json_file:
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


# Email format validation
def checky(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return 'y'
    else:
        return


# number format validation
def check_numformat(telno):
    regex = r'^[01 | 07]{2}[0-9]{8}$'
    if re.fullmatch(regex, telno):
        return 'y'
    else:
        return
# customer_info()
