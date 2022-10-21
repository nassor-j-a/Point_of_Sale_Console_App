from email.message import EmailMessage
import ssl
import smtplib
import json
prod_file = "Product/prod.json"
cus_file = "Customer/cus.json"


def p_order():
    while True:
        print("""
        ----------------------------------------------
        Purchase Sub-Menu:-

        1) Purchase products
        2) Purchase history
        3) Back to Main Menu

        ----------------------------------------------
        """)
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            process_order()

        elif choice == "2":

            purchase_history()

        elif choice == "3":
            from main import main_menu

            main_menu()
        else:
            print('\nINVALID MENU OPTION! Enter 1-3')


def process_order():
    fin_order = {}
    with open("Order/cart.json", "r") as json_file:
        order_temp = json.load(json_file)
    # checks if cart is empty
    if not order_temp:
        from Customer.customer import view_customer
        view_customer()
        with open(cus_file, "r") as json_file:
            cus_temp = json.load(json_file)
            data_lent = len(cus_temp)
            while True:
                try:
                    cust_id = int(input(f"\nEnter Customer ID(1-{data_lent}) of the buyer:\n"))
                except ValueError:
                    print(f"\nINVALID INPUT! Selection can't be an Alphabet")
                    continue
                if cust_id > data_lent:
                    print("CUSTOMER DOES NOT EXIST! Enter VALID Customer ID!")
                    continue
                else:
                    break

            i = 1
            for entry in cus_temp:
                if i == int(cust_id):
                    fin_order["Customer Name"] = entry["Customer_Name"]
                    fin_order["Email"] = entry["Email"]
                    order_temp.append(fin_order)
                    i = i + 1
                else:
                    pass
                    i = i + 1
        from Product.product import view_product
        view_product()

        with open(prod_file, "r") as json_file:
            prod_temp = json.load(json_file)
        data_length = len(prod_temp)

        with open("Order/cart.json", "r") as json_file:
            cart_temp = json.load(json_file)
        opt = ''

        while True:
            try:
                opt = int(input(f"\nEnter Product ID(1 - {data_length}) of item you wish to add to cart:"))
            except ValueError:
                print(f"\nINVALID INPUT! Product ID can't be an Alphabet")
                continue
            if opt > data_length:
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                break
        i = 1
        for entry in prod_temp:

            if i == int(opt):
                prod_id = create_prod_id()
                fin_order[prod_id] = {}
                prod_qty = entry["Product_Quantity"]
                fin_order[prod_id]["Product_id"] = opt
                fin_order[prod_id]["Product_Name"] = entry["Product_Name"]
                while True:
                    try:
                        qty = int(input(f"\nEnter quantity (less than or equal to {prod_qty}) you wish to purchase:"))
                    except ValueError:
                        print("\nINVALID INPUT! Quantity can't be an alphabet!")
                        continue
                    if qty > prod_qty:
                        print(f"\nINVALID INPUT! Quantity can't be greater than {prod_qty}!")
                        continue
                    elif qty < 1:
                        print("\nINVALID INPUT! Quantity can't be less than 1!")
                    else:
                        fin_order[prod_id]["Product_Quantity"] = qty
                        break

                fin_order[prod_id]["Product_Price"] = entry["Product_Price"]
                price_tint = float(fin_order[prod_id]["Product_Price"])
                subtt = price_tint * fin_order[prod_id]["Product_Quantity"]
                fin_order[prod_id]["Sub-Total"] = '{:.2f}'.format(subtt)
                # insert/adds contents of selected_prod inside cart_temp
                cart_temp.append(fin_order)
                i = i + 1

            else:
                pass
                i = i + 1
        with open("Order/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\nProduct Added to cart!")
    # knows the cart has values/not empty ~ adding extra products in the prod dict and assigns IDs
    else:
        from Product.product import view_product
        view_product()
        with open(prod_file, "r") as json_file:
            prod_temp = json.load(json_file)
        data_length = len(prod_temp)

        with open("Order/cart.json", "r") as json_file:
            cart_temp = json.load(json_file)

        opt = ''

        while True:
            try:
                opt = int(input(f"\nEnter Product ID(1 - {data_length}) of item you wish to add to cart:"))
            except ValueError:
                print(f"\nINVALID INPUT! Product ID can't be an Alphabet")
                continue
            if opt > data_length:
                print(f"\nINVALID INPUT! Enter a value between 1 and {data_length}")
                continue
            else:
                validate_prod = check_prod(opt)
                if validate_prod == 'y':
                    print('\nProduct already Exist in cart!')
                    continue
                else:
                    break

        i = 1
        for entry in prod_temp:

            if i == int(opt):
                prod_id = create_prod_id()
                fin_order[prod_id] = {}
                prod_qty = entry["Product_Quantity"]
                fin_order[prod_id]["Product_id"] = opt
                fin_order[prod_id]["Product_Name"] = entry["Product_Name"]
                while True:
                    try:
                        qty = int(input(f"\nEnter quantity (less than or equal to {prod_qty}) you wish to purchase:"))
                    except ValueError:
                        print("\nINVALID INPUT! Quantity can't be an alphabet!")
                        continue
                    if qty > prod_qty:
                        print(f"\nINVALID INPUT! Quantity can't be greater than {prod_qty}!")
                        continue
                    elif qty < 1:
                        print("\nINVALID INPUT! Quantity can't be less than 1!")
                    else:
                        fin_order[prod_id]["Product_Quantity"] = qty
                        break
                fin_order[prod_id]["Product_Price"] = entry["Product_Price"]
                price_tint = float(fin_order[prod_id]["Product_Price"])
                subtt = price_tint * fin_order[prod_id]["Product_Quantity"]
                fin_order[prod_id]["Sub-Total"] = '{:.2f}'.format(subtt)
                # Append - insert/adds contents of fin_order inside open_cart_temp
                # removes the list/ leaves the dictionary inside for update/
                # Update adds something extra in an already existing dictionary
                [open_cart_temp] = cart_temp
                # prod_list.append(opt)
                open_cart_temp.update(fin_order)

                i = i + 1

            else:
                pass
                i = i + 1
        with open("Order/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\nProduct Added to cart!")

    while True:
        cont_shopping = int(input("\nPress 1 to continue shopping and 2 to complete purchase:"))
        if cont_shopping == 1:
            process_order()
        elif cont_shopping == 2:
            # calculating total from subtotal
            with open("Order/cart.json", "r") as json_file:
                checkout_temp = json.load(json_file)
            emp_prd = {}
            [opened_checkout_temp] = checkout_temp
            total = 0
            for i in opened_checkout_temp:
                if i == "Customer Name":
                    continue
                elif i == "Email":
                    continue
                else:
                    subt_tint = float(opened_checkout_temp[i]["Sub-Total"])
                    total += subt_tint
            emp_prd["Total"] = "{:.2f}".format(total)
            opened_checkout_temp.update(emp_prd)

            with open("Order/cart.json", "w") as json_file:
                json.dump(checkout_temp, json_file, indent=4)
        break
    # final checkout procedure
    with open("Order/cart.json", "r") as json_file:
        check_temp = json.load(json_file)
    [strip_check_temp] = check_temp
    print("\nYour shopping is:")
    for i in strip_check_temp:
        if i == "Customer Name":
            continue
        elif i == "Email":
            continue
        elif i == "Total":
            print(f"\nTotal: Ksh. {strip_check_temp[i]}")
        else:
            print(f"\nProduct Name: {strip_check_temp[i]['Product_Name']}")
            print(f"Product Quantity: {strip_check_temp[i]['Product_Quantity']}")
            print(f"Product Price: Ksh. {strip_check_temp[i]['Product_Price']}")
            print(f"Sub-Total: Ksh. {strip_check_temp[i]['Sub-Total']}")
    while True:
        checkout_prompt = input("\nDo you wish to proceed with payment? y/n: ")
        if checkout_prompt == 'y':
            amt_tendered()
        elif checkout_prompt == 'n':
            cart = []
            with open("Order/cart.json", "w") as json_file:
                json.dump(cart, json_file, indent=4)
            p_order()
        else:
            print("\nINVALID INPUT! Enter 'y' or 'n'!")
            continue
        break
    change_calculation()

    # printing a receipt
    with open("Order/cart.json", "r") as json_file:
        fin_temp = json.load(json_file)
    [strip_fin_temp] = fin_temp
    forma_t = '-' * 46

    print(f"\n{forma_t}")
    print("-------------------RECEIPT--------------------")
    print(forma_t)

    for i in strip_fin_temp:
        if i == "Customer Name":
            print(f"\nCustomer Name: {strip_fin_temp[i]}")
        elif i == "Email":
            pass
        elif i == "Total":
            print(f"\nTotal: Ksh. {strip_fin_temp[i]}")
        elif i == "Amount Tendered":
            print(f"Amount Tendered: Ksh. {strip_fin_temp[i]}")
        elif i == "Change":
            print(f"Change: Ksh. {strip_fin_temp[i]}")
        else:
            print(f"\nProduct Name: {strip_fin_temp[i]['Product_Name']}")
            print(f"Product Quantity: {strip_fin_temp[i]['Product_Quantity']}")
            print(f"Product Price: Ksh. {strip_fin_temp[i]['Product_Price']}")
            print(f"Sub-Total: Ksh. {strip_fin_temp[i]['Sub-Total']}")

    print(f"\n{forma_t}")
    print("--------Thank you for Shopping with us--------")
    print(f"\n{forma_t}")

    send_mail()
    # product quantity decrement
    with open("Order/cart.json", "r") as json_file:
        pid_temp = json.load(json_file)
    [open_pid] = pid_temp
    for i in open_pid:
        if i == "Customer Name":
            continue
        elif i == "Email":
            continue
        elif i == "Total":
            continue
        elif i == "Amount Tendered":
            continue
        elif i == "Change":
            continue
        else:
            p_id_list = open_pid[i]["Product_id"]
            p_qty_list = open_pid[i]["Product_Quantity"]
            with open(prod_file, "r") as json_file:
                prod_temp = json.load(json_file)
            up_qty_list = []
            j = 1
            for entry in prod_temp:
                if j == p_id_list:
                    prod_name = entry["Product_Name"]
                    prod_qty = entry["Product_Quantity"]
                    prod_price = entry["Product_Price"]
                    prod_qty = prod_qty - p_qty_list
                    up_qty_list.append({"Product_Name": prod_name,
                                        "Product_Quantity": prod_qty,
                                        "Product_Price": prod_price})
                    j = j + 1
                else:
                    up_qty_list.append(entry)
                    j = j + 1
            with open("Product/prod.json", "w") as json_file:
                json.dump(up_qty_list, json_file, indent=4)

    # generating a purchase list
    with open("Order/cart.json", "r") as json_file:
        c_temp = json.load(json_file)
    [strip_c_temp] = c_temp
    with open("Order/order.json", "r") as json_file:
        o_temp = json.load(json_file)

    pur_combo = {}
    order_id = create_pur_id()
    pur_combo[order_id] = strip_c_temp
    if not o_temp:
        o_temp.append(pur_combo)
    else:
        [open_o_temp] = o_temp
        open_o_temp.update(pur_combo)

    with open("Order/order.json", "w") as json_file:
        json.dump(o_temp, json_file, indent=4)
        print("\nOrder record captured!")
    # emptying the cart
    cart = []
    with open("Order/cart.json", "w") as json_file:
        json.dump(cart, json_file, indent=4)

    p_order()


def create_prod_id():
    with open("Order/cart.json", "r") as json_file:
        gen_temp = json.load(json_file)
    if not gen_temp:
        new_id = "Prod1"
        return new_id
    else:
        # Removing the list so that keys in dictionary elements can be read/accessed
        [open_gen_temp] = gen_temp
        # [-1] begins the  list from bottom [1] begins the list from above
        prev_id = list(open_gen_temp)[-1]
        # takes the length of the character from left to right
        length = len(prev_id)
        num = int(prev_id[4:length]) + 1
        new_id = "Prod" + str(num)
        return new_id


def create_pur_id():
    with open("Order/order.json", "r") as json_file:
        od_temp = json.load(json_file)
    if not od_temp:
        new_id = "Ord1"
        return new_id
    else:
        [open_od_temp] = od_temp
        prev_id = list(open_od_temp)[-1]
        length = len(prev_id)
        num = int(prev_id[3:length]) + 1
        new_id = "Ord" + str(num)
        return new_id


def purchase_history():
    while True:
        print("""
             ----------------------------------------------
             Customer Search Sub-Menu:-

             1) General purchase history
             2) Individual customer purchase history
             3) Back to Purchase Sub-Menu

             ----------------------------------------------
                 """)
        c_choice = input('Enter a Menu option to continue:')
        if c_choice == "1":
            completed_orders()
        elif c_choice == "2":
            individual_cust()
        elif c_choice == "3":
            p_order()
        else:
            print('INVALID MENU OPTION! Enter 1-3')


# Generating a purchase list
def completed_orders():
    with open("Order/order.json", "r") as json_file:
        o_temp = json.load(json_file)
    [strip_o_temp] = o_temp
    format_i = '-' * 89
    format_ii = '-' * 33

    print(f"\n{format_ii} {'Processed Orders'} {format_ii}\n")

    for i in strip_o_temp:
        print(f"Order: {i}")
        for j in strip_o_temp[i]:
            if j == "Customer Name":
                print(f"Customer Name: {strip_o_temp[i]['Customer Name']}")
            elif j == "Email":
                pass
            elif j == "Total":
                print(f"\nTotal: Ksh. {strip_o_temp[i]['Total']}")
            elif j == "Amount Tendered":
                print(f"Amount Tendered: Ksh. {strip_o_temp[i]['Amount Tendered']}")
            elif j == "Change":
                print(f"Change: Ksh. {strip_o_temp[i]['Change']}\n")
            else:
                p_name = strip_o_temp[i][j]['Product_Name']
                p_price = strip_o_temp[i][j]['Product_Price']
                p_qty = strip_o_temp[i][j]['Product_Quantity']
                print(f"Product Name: {p_name}, Product Price: {p_price}, "
                      f"Product Quantity: {p_qty}, Sub-Total: Ksh. {strip_o_temp[i][j]['Sub-Total']}")

    print(f"{format_i}")


def individual_cust():
    with open("Order/order.json", "r") as json_file:
        o_temp = json.load(json_file)
    [strip_o_temp] = o_temp
    customer_name = input("Enter full name of customer to view their purchase history:")
    for i in strip_o_temp:
        if strip_o_temp[i]['Customer Name'] == customer_name:
            for j in strip_o_temp[i]:
                if j == "Customer Name":
                    print(f"\nCustomer Name: {strip_o_temp[i]['Customer Name']}")
                elif j == "Email":
                    pass
                elif j == "Total":
                    print(f"\nTotal: Ksh. {strip_o_temp[i]['Total']}")
                elif j == "Amount Tendered":
                    print(f"Amount Tendered: Ksh. {strip_o_temp[i]['Amount Tendered']}")
                elif j == "Change":
                    print(f"Change: Ksh. {strip_o_temp[i]['Change']}\n")
                else:
                    p_name = strip_o_temp[i][j]['Product_Name']
                    p_price = strip_o_temp[i][j]['Product_Price']
                    p_qty = strip_o_temp[i][j]['Product_Quantity']
                    print(f"Product Name: {p_name}, Product Price: {p_price}, "
                          f"Product Quantity: {p_qty}, Sub-Total: Ksh. {strip_o_temp[i][j]['Sub-Total']}")
        else:
            continue


# checking if product exist in cart
def check_prod(option):
    with open("Order/cart.json", "r") as json_file:
        cart_temp = json.load(json_file)
        [cart_list] = cart_temp
    for i in cart_list:
        if i == "Customer Name":
            continue
        elif i == "Email":
            continue
        else:
            if cart_list[i]['Product_id'] == option:
                return 'y'
            else:
                continue
    return 'n'


# amount tendered validation
def amt_tendered():
    with open("Order/cart.json", "r") as json_file:
        check_temp = json.load(json_file)
    [strip_check_temp] = check_temp
    chkt = {}
    tot = float(strip_check_temp["Total"])
    while True:
        try:
            amount_paid = int(input("Enter amount paid:"))
        except ValueError:
            print("\nINVALID INPUT! Amount paid can't be an Alphabet")
            continue
        if amount_paid < tot:
            print("\nAmount tendered can't be less than 'Total' amount!")
            continue
        chkt["Amount Tendered"] = "{:.2f}".format(amount_paid)
        break
    strip_check_temp.update(chkt)
    with open("Order/cart.json", "w") as json_file:
        json.dump(check_temp, json_file, indent=4)


def change_calculation():
    with open("Order/cart.json", "r") as json_file:
        checkit_temp = json.load(json_file)
    [strip_checkit_temp] = checkit_temp
    chkt_it = {}
    converted_amt = float(strip_checkit_temp["Amount Tendered"])
    converted_tot = float(strip_checkit_temp["Total"])
    change = float(converted_amt - converted_tot)
    chkt_it["Change"] = "{:.2f}".format(change)
    strip_checkit_temp.update(chkt_it)
    with open("Order/cart.json", "w") as json_file:
        json.dump(checkit_temp, json_file, indent=4)


def send_mail():

    with open("Order/cart.json", "r") as json_file:
        fin_temp = json.load(json_file)
    [strip_fin_temp] = fin_temp

    email_sender = 'allprojects53@gmail.com'
    email_pass = ''
    email_receiver = ''

    subject = "PURCHASE RECEIPT"

    body = "\n----------------------------------------------"
    body += "-------------------RECEIPT--------------------"
    body += "----------------------------------------------"
    body += "\n"

    for i in strip_fin_temp:
        if i == "Customer Name":
            body += f"\nCustomer Name: {strip_fin_temp[i]}"
        elif i == "Total":
            body += f"\nTotal: Ksh. {strip_fin_temp[i]}"
        elif i == "Email":
            email_receiver = {strip_fin_temp[i]}
        elif i == "Amount Tendered":
            body += f"\nAmount Tendered: Ksh. {strip_fin_temp[i]}"
        elif i == "Change":
            body += f"\nChange: Ksh. {strip_fin_temp[i]}"
        else:
            body += f"\nProduct Name: {strip_fin_temp[i]['Product_Name']} "
            body += f"Product Quantity: {strip_fin_temp[i]['Product_Quantity']} "
            body += f"Product Price: Ksh. {strip_fin_temp[i]['Product_Price']}"
            body += f"\nSub-Total: Ksh. {strip_fin_temp[i]['Sub-Total']}"
            body += "\n"
    body += "\n----------------------------------------------"
    body += "-------Thank you for Shopping with us---------"
    body += "----------------------------------------------"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# p_order()
