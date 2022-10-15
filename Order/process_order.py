import json
prod_file = "Product/prod.json"
cus_file = "Customer/cus.json"


def p_order():
    while True:
        print("""
        ----------------------------------------------
        Order Sub-Menu:-

        1) Purchase products

        2) List purchases

        3) Back to Main Menu

        ----------------------------------------------
        """)
        choice = input('Enter a Menu option to continue:')

        if choice == "1":

            process_order()

        elif choice == "2":

            completed_orders()

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
        data_lent = len(cus_temp) + 1
        while True:
            cust_id = int(input(f"\nEnter Customer ID(1-{data_lent}) of the buyer:"))
            if cust_id in range(1, data_lent):
                break
            else:
                print("CUSTOMER DOES NOT EXIST! Enter VALID Customer ID!")
                continue

        i = 1
        for entry in cus_temp:
            if i == int(cust_id):
                fin_order["Customer Name"] = entry["Customer_Name"]
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

        opt = int(input(f"Enter Product ID(1 - {data_length}) of item you wish to add to cart:"))
        i = 1
        for entry in prod_temp:

            if i == int(opt):
                prod_id = create_prod_id()
                fin_order[prod_id] = {}
                prod_qty = entry["Product_Quantity"]
                fin_order[prod_id]["Product_id"] = opt
                fin_order[prod_id]["Product_Name"] = entry["Product_Name"]
                fin_order[prod_id]["Product_Price"] = entry["Product_Price"]
                fin_order[prod_id]["Product_Quantity"] = int(input(f"\nEnter quantity (less than or equal "
                                                                   f"to {prod_qty}) you wish to purchase:"))
                fin_order[prod_id]["Sub-Total"] = fin_order[prod_id]["Product_Price"] * fin_order[
                    prod_id]["Product_Quantity"]
                # insert/adds contents of selected_prod inside cart_temp
                cart_temp.append(fin_order)
                # prod_list.append(opt)
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
            # [cart_list] = cart_temp
            # result = cart_list.strip("[]{}")

        opt = int(input(f"Enter Product ID(1 - {data_length}) of item you wish to add to cart:"))
        i = 1
        for entry in prod_temp:

            if i == int(opt):
                prod_id = create_prod_id()
                fin_order[prod_id] = {}
                prod_qty = entry["Product_Quantity"]
                fin_order[prod_id]["Product_id"] = opt
                fin_order[prod_id]["Product_Name"] = entry["Product_Name"]
                fin_order[prod_id]["Product_Price"] = entry["Product_Price"]
                fin_order[prod_id]["Product_Quantity"] = int(input(f"\nEnter quantity (less than or equal "
                                                                   f"to {prod_qty}) you wish to purchase:"))
                fin_order[prod_id]["Sub-Total"] = fin_order[prod_id]["Product_Price"] * fin_order[
                    prod_id]["Product_Quantity"]
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
            new_id = "Total"
            total = 0
            for i in opened_checkout_temp:
                if i == "Customer Name":
                    continue
                else:
                    total += opened_checkout_temp[i]["Sub-Total"]
            emp_prd[new_id] = total
            opened_checkout_temp.update(emp_prd)

            with open("Order/cart.json", "w") as json_file:
                json.dump(checkout_temp, json_file, indent=4)
        break

    # printing a receipt
    with open("Order/cart.json", "r") as json_file:
        fin_temp = json.load(json_file)
    [strip_fin_temp] = fin_temp

    print("\n----------------------------------------------")
    print("-------------------RECEIPT--------------------")
    print("----------------------------------------------")
    for i in strip_fin_temp:
        if i == "Customer Name":
            print(f"\nCustomer Name: {strip_fin_temp[i]}")
        elif i == "Total":
            print(f"\nTotal is Ksh: {strip_fin_temp[i]}")
        else:
            print(f"\nProduct Name: {strip_fin_temp[i]['Product_Name']}")
            print(f"Product Price: {strip_fin_temp[i]['Product_Price']}")
            print(f"Product Quantity: {strip_fin_temp[i]['Product_Quantity']}")
            print(f"Sub-Total: {strip_fin_temp[i]['Sub-Total']}")

    print("\n----------------------------------------------")
    print("-------Thank you for Shopping with us---------")
    print("----------------------------------------------")

    # product quantity decrement
    with open("Order/cart.json", "r") as json_file:
        pid_temp = json.load(json_file)
    [open_pid] = pid_temp
    for i in open_pid:
        if i == "Customer Name":
            continue
        elif i == "Total":
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
                    prod_price = entry["Product_Price"]
                    prod_qty = entry["Product_Quantity"]
                    prod_qty = prod_qty - p_qty_list
                    up_qty_list.append({"Product_Name": prod_name,
                                        "Product_Price": prod_price,
                                        "Product_Quantity": prod_qty})
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
    cart = []
    with open("Order/cart.json", "w") as json_file:
        json.dump(cart, json_file, indent=4)

    exit()


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


# Generating a purchase list
def completed_orders():
    with open("Order/order.json", "r") as json_file:
        o_temp = json.load(json_file)
    [strip_o_temp] = o_temp

    print("\n------- Processed Orders ---------\n")

    for i in strip_o_temp:
        print(f"Order: {i}")
        for j in strip_o_temp[i]:
            if j == "Customer Name":
                print(f"Customer Name: {strip_o_temp[i]['Customer Name']}")
            elif j == "Total":
                print(f"Total is Ksh:  {strip_o_temp[i]['Total']}\n")
            else:
                p_name = strip_o_temp[i][j]['Product_Name']
                p_price = strip_o_temp[i][j]['Product_Price']
                p_qty = strip_o_temp[i][j]['Product_Quantity']
                sub = strip_o_temp[i][j]['Sub-Total']
                print(f"Product Name: {p_name}, Product Price: {p_price}, "
                      f"Product Quantity: {p_qty}, Sub-Total: {sub}")
    exit()

# p_order()
