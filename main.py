from Customer.customer import customer_info

from Products.product import product_info

    
def main_menu():
    print("""
    ----------------------------------------------
    ------------WAKAGUKU GROCERY SHOP-------------
    ----------------------------------------------
    Menu:-
    
    1) Order
    
    2) Product
    
    3) Customer
    
    4) Search
    
    5) Exit
    ----------------------------------------------
    """) 
    
    # handles non integer value that has been handled from ending the program
    while True:
        
        # Handles non integer inputs from user
        try:
            choice = int(input ('Enter a Menu option to continue:\n'))       
                
            if choice == 1:
                    
                from Order.process_order import p_order           
                p_order()
                
                #To avoid continuous looping
                break
                    
            elif choice == 2:
                    
                product_info()
                
                break
                        
            elif choice == 3:
                
                customer_info()
                
                break
                    
            elif choice == 4:
                    
                from search import search_here
                search_here()
                
                break
            
            elif choice == 5:
                
                #exit can't be here, the loop will still execute
                break   
                
            else: 
                print('INCORRECT INPUT! Enter 1 - 4!')
                main_menu()
        
        except ValueError:
            
            print('INCORRECT INPUT! Enter 1 - 4!')
    exit

main_menu()
