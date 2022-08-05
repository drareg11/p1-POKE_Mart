import mysql.connector 
import pokedata_base as p
import re
import logging
from Poke_Mart import admin, customer, orders

try:
    cnx = mysql.connect.connector(user=p.user, password=p.password, host=p.host, database="Project_1")
    my_cursor = cnx.cursor
except mysql.connector.Error as mce:
    print(mce.msg)
except Exception as e:
    print("Error:With Quitting the Program")

logging.basicConfig(filename="POKEmart.log",level=logging.DEBUG,format='%(asctime)s :: %(message)s')

def insert_records():
    logging.basicConfig(filename="POKEmart.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    restart = True
    logging.info("Logging into the web")
    while restart :
        print("\n*****---WELCOME TO THE POKE Mart---****** :")
        print("\t1) ADMIN Log In\n")
        print("\t2) Customer Log In\n")
        print("\t3) New Customer Create Account\n")
        print("\t4) Quit\n")

        valid = False
        while not valid:
            try:
                input_type = int(input(" Enter Option >>>>"))
                valid= True
            except:
                print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")
                logging.error(" Invalid selection ")
        

        if input_type ==1:
            print("***ADMIN LOG IN PORTAL***\n")
            admin_login()
        elif input_type ==2:
            print("***CUSTOMER LOG IN PORTAL***\n")
            customer_login()
        elif input_type==3:
            print("***NEW CUSTOMER CREATE ACCOUNT***\n")
            add_new_customer()
        elif input_type ==4:
            print("***Quiting the program ..........<><><>***\n")
            logging.info("User Quits the Program ")
            restart = False
        else:
            print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]\nRestarting The Store>>>>>>>.........")
            logging.info("Invalid input was entered ")

def admin_login():
    print("****WELCOME TO THE ADMIN PORTAL****\nLOGIN BELOW!!")
    restart = True
    while restart == True:

        while True:
            try:
                name =str(input("Enter ADMINISTRATOR name >"))
                if re.search("[a-zA-Z]",name):
                    break
                else:
                    raise ValueError
                    print("\nInvalid name format")
            except ValueError as ve :
                print("Invalid NAME format.  NAME MUST BE A STRING FORMAT:")
            else:
                break

        valid = False
        while not valid:
            try:
                passwrd =int(input("enter password"))
                valid = True
            except:
                print("Invalid Input. PASSWORD must be an Integer : ####")

        add = admin(name,passwrd)
        query_admin = f"SELECT * FROM admin where name ='{add.name}' and password ={add.passwrd}"
        my_cursor.execute(query_admin)
        record = my_cursor.fetchone()
        

        if record != None:
            print(f"\nADMIN Log in successful .......\nWELCOME {add.name}")
            logging.info("Successfully Loged Into The ADMIN portal")

            restart = True
            while restart == True:
                print(f"\nSELECT OPTION [1 , 2 , 3 , 4]")
                print("\t1) Add Records ")
                print("\t2) View  Records ")
                print("\t3) Update Existing Records ")
                print("\t4) Delete Existing Records ")
                print("\t5) quit ")

                valid = False
                while not valid:
                    try:
                        select = int(input(f"\nEnter Option: >>>>>>>>>>\n" ))
                        valid = True
                    except:
                        print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 5]")

                if select ==1:
                    print("Welcome to the Admin ADD RECORDS section\n Select Record To Add: ")
                    print("\t1) Add New ADMIN ")
                    print("\t2) Add New Customer ")
                    print("\t3) Add Items to Inventory  ")
                    print("\t4) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the ADD RECORDS section {add.name} \n>>>>>"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        add_new_admin()
                        restart=True
                    elif select ==2:
                        add_new_customer()
                        restart=True
                    elif select ==3:
                        add_new_item()
                        restart = True
                    elif select ==4:
                        print("***Quiting the ADD RECORDS SECTION ..........<><><>***\n")
                        restart = False
                        break
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                        restart = True
                elif select == 2:
                    print("Welcome to the Admin VIEW RECORDS section\n Select Record To Add: ")
                    print("\t1) View Existing ADMIN accounts")
                    print("\t2) View Existing Customers/Trainers")
                    print("\t3) View All Inventory")
                    print("\t4) View Customer History")
                    print("\t5) View All Placed Orders")
                    print("\t6) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the VIEW RECORDS section {add.name}"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        view_Admin()
                    elif select == 2:
                        view_exist_customers()
                    elif select == 3:
                        view_Inventory()
                    elif select == 4:
                        view_customer_history()
                    elif select == 5:
                        view_all_orders()
                    elif select == 6:
                        print("***Quiting the VIEW RECORDS SECTION ..........<><><>***\n")
                        restart= False
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4 , 5 , 6]")
                elif select ==3:
                    print("Welcome to the Admin UPDATE RECORDS section\n Select Record To Add: ")
                    print("\t1) Modify Existing ADMIN Details")
                    print("\t2) Modify Existing Customers Details")
                    print("\t3) Modify Inventory")
                    print("\t4) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the MODIFY RECORDS section {add.name}"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        modify_admin()
                    elif select == 2:
                        modify_customer_record()
                    elif select == 3:
                        modify_inventory()
                    elif select == 4:
                        print("***Quiting the UPDATE RECORDS SECTION ..........<><><>***\n")
                        break
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                elif select ==4:
                    print("Welcome to the Admin DELETE RECORDS section\nSelect Record To DELETE: \n")
                    print("\t1) Delete Existing ADMIN Accounts")
                    print("\t2) Delete Existing Customers Accounts")
                    print("\t3) Delete Item in Inventory")
                    print("\t4) quit ")

                    valid = False
                    while not valid:
                        try:
                            select = int(input(f"Select option from the DELETE RECORDS section {add.name}"))
                            valid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")
                    if select == 1:
                        delete_admin()
                    elif select == 2:
                        delete_customer_records()
                    elif select == 3:
                        delete_item()
                    elif select == 4:
                        print("***Quiting the UPDATE RECORDS SECTION ..........<><><>***\n")
                        restart= False
                        break
                    else:
                        print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                        #call delete options  here
                elif select == 5:
                    print("***Quiting the ADMIN SECTION ..........<><><>***\n")
                    restart = False
                    break
                else:
                    print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]")
                    logging.info("Invalid input was entered ")
                    restart = True

        else :
            print(f"\nUnregistered Admin:Unauthorised access to the ADMIN Portal \nExiting To HOME.............")
            logging.info("Unauthorised Login Attempt was Declined ")

def customer_login():
    while True: 
        print("\t1) Existing Customer Log in")
        print("\t2) New Customer, SIGN UP Today!")
        print("\t3) Quit")

        valid = False
        while not valid:
            try:
                input_type = int(input("Enter Option >>>>"))
                valid = True
            except:
                print("Invalid Input. Enter Input : [1 , 2 , 3 ]")


        if input_type ==1:
            print(f"Welcome Back Customer . Enter Log In details below:  \n")
            while True:
                try:
                    name = str(input(f"Registered Customer NAME >>>>>>\n"))
                    if re.search("[a-zA-Z]",name):
                        break
                    else:
                        raise  ValueError
                except ValueError as ve :
                    print("invalid name format :    NAME MUST BE A STRING:")
                else:
                    break


            valid = False
            while not valid:
                try:
                    custID = int(input("Registered Customer ID >>>>>>\n"))
                    valid = True
                except:
                    print("Invalid input Enter ")

            query_customer_login = f"SELECT  * FROM  customers WHERE name ='{name}' AND customerID = {custID};"
            

            my_cursor.execute(query_customer_login)
            record = my_cursor.fetchone()
            

            if record != None:
                logging.info("successful log into customer portal")
                print("Customer Log in successful....\n")
                print("\t1) Place an Order")
                print("\t2) View all orders")
                print("\t3) Quit")

                valid = False
                while not valid:
                    try:
                        input_type = int(input("Make Selection >>>>"))
                        valid = True
                    except:
                        print("Invalid input Enter ")
                if input_type == 1:
                    add_new_order()
                elif input_type == 2:
                    view_customer_history()
                elif input_type == 3:
                    print("***Quiting the CUSTOMERS SECTION ..........<><><>***\n")
                    break
                print(" Please log in! ")
            else:
                print("Unsuccessful Log in Attempt: Wrong Details Entered ")

        elif input_type == 2:
            print("New Customer Account Creation Page ")
            add_new_customer()

        elif input_type == 3:
            print("Quiting The Program")
            break
        else:
            print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]\n")
            logging.info("Invalid input was entered ")

# #########  MORE FUNCTIONS########
def add_new_admin():
    pass

def add_new_item():
    pass

def add_new_customer():
    pass

def view_Admin():
    pass

def view_exist_customers():
    pass

def view_Inventory():
    pass

def view_customer_history():
    pass

def view_all_orders():
    pass

def modify_admin():
    pass

def modify_customer_record():
    pass

def modify_inventory():
    pass

def delete_admin():
    pass

def delete_customer_records():
    pass

def delete_item():
    pass

def add_new_order():
    pass 


#     #CURSOR-  points to various tables allowing to insert into our database and query our databses

my_cursor = cnx.cursor()


query = "SELECT * FROM employees_3nf"

my_cursor.execute(query)

for record in my_cursor:
        print(record)

my_cursor.close()
cnx.close()