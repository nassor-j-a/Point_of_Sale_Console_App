# data = {
#         "Customer Name": "Haifa Mbarak",
#         "Prod1": {
#             "Product_Name": "Pepper",
#             "Product_Price": 10,
#             "Product_Quantity": 3,
#             "Sub-Total": 30
#         },
#         "Prod2": {
#             "Product_Name": "Tumeric",
#             "Product_Price": 150,
#             "Product_Quantity": 4,
#             "Sub-Total": 600
#         }
#     }
# if not data:
#     print(data)
# else:
#     for i in data:
#         if i == "Customer Name":
#             continue
#         else:
#             print(data[i]["Sub-Total"])
# data = {
#         "Customer Name": "Haifa Mbarak",
#         "Prod1": {
#             "Product_Name": "Garlic",
#             "Product_Price": 50,
#             "Product_Quantity": 2,
#             "Sub-Total": 100
#         },
#         "Prod2": {
#             "Product_Name": "Pepper",
#             "Product_Price": 10,
#             "Product_Quantity": 3,
#             "Sub-Total": 30
#         },
#         "Prod3": {
#             "Product_Name": "Egg-plant",
#             "Product_Price": 115,
#             "Product_Quantity": 5,
#             "Sub-Total": 575
#         },
#         "Total": 705
#     }
# # print(data)
# for i in data:
#     if i == "Customer Name":
#         print(f"Name is: {data[i]}")
#         # print(f"Name is: {data[i]['Product_Name']}")
#         # print(f"Name is: {data[i]['Product_Name']}")
#     elif i == "Total":
#         print(f"Total is Ksh: {data[i]}")
#     else:
#         print(data[i]["Product_Name"])
#         print(data[i]["Product_Price"])
#         print(data[i]["Product_Quantity"])
#         print(data[i]["Sub-Total"])
# exit()
# c_name = open_customer[customer_id]["name"]
#                 print(f"Customer: {c_name}")
#                 for item in item_data:
#
#                     p_name = item_data[item]["product name"]
#                     p_quantity = item_data[item]["product quantity"]
#                     p_cost = item_data[item]["product cost"]
#                     print(f"Product: {p_name}   Quantity: {p_quantity}   Cost: {p_cost} ")
#                     print(f"Total Cost: {total} Ksh.")
users = [
    {'name': 'John',
    'age': '13',
    'place': 'Earth',
    'dob': '12/12/12'

    },
    {
        'name': 'Bob',
        'age': '11',
        'place': 'moon',
        'dob': '12/12/12'
    }
]

for i in users:
    if 'John' in i['name']:
        print(i['name'])
        print(i['place'])
        print(i['dob'])

