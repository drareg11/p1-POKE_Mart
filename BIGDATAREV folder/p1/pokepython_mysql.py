import mysql.connector 
import pokedata_base as p
import re
import logging
from Poke_Mart import admin, customer, orders, inventory

try:
    cnx = mysql.connector.connect(user=p.user, password=p.password, host=p.host, database="Project_1")
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

        invalid = False
        while not invalid:
            try:
                input_type = int(input(" Enter Option >>>>"))
                invalid= True
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
            create_new_cust()
        elif input_type ==4:
            print("***Quiting the program ..........<><><>***\n")
            logging.info("User Quits the Program ")
            restart = False
        else:
            print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]\nRestarting The Store>>>>>>>.........")
            logging.info("Invalid input was entered ")
####LOGIN FUNCT.
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
                    # print("\nInvalid name format")
            except ValueError as ve :
                print("Invalid NAME format.  NAME MUST BE A STRING FORMAT:")
            else:
                return

        invalid = False
        while not invalid:
            try:
                admin_passcode =int(input("enter password"))
                invalid = True
            except:
                print("Invalid Input. PASSWORD must be an Integer : ####")

        add = admin(name, admin_passcode)
        query_admin = f"SELECT * FROM admin where name ='{add.name}' and password ={add.admin_passcode}"
        my_cursor.execute(query_admin)
        record = my_cursor.fetchone()
        

        if record != None:
            print(f"\nADMIN Log in successful .......\nWELCOME {add.name}")
            logging.info("Successfully Loged Into The ADMIN portal")

            restart = True
            while restart == True:
                print(f"\nSELECT OPTION [1 , 2 , 3 , 4]")
                print("\t1) Add NEW acct. or inventory to Records ")
                print("\t2) View  Records ")
                print("\t3) Update Existing Records ")
                print("\t4) Delete Existing Records ")
                print("\t5) quit ")

                invalid = False
                while not invalid:
                    try:
                        select = int(input(f"\nEnter Option: >>>>>>>>>>\n" ))
                        invalid = True
                    except:
                        print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 5]")

                if select ==1:
                    print("Welcome to the Admin ADD RECORDS section\n Select Record To Add: ")
                    print("\t1) Add New ADMIN ")
                    print("\t2) Add New Customer ")
                    print("\t3) Add NEW Items to Inventory  ")
                    print("\t4) quit ")

                    invalid = False
                    while not invalid:
                        try:
                            select = int(input(f"Select option from the ADD NEW RECORDS section {add.name} \n>>>>>"))
                            invalid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        add_new_admin()
                        restart=True
                    elif select ==2:
                        create_new_cust()
                        restart=True
                    elif select ==3:
                        add_new_items()
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

                    invalid = False
                    while not invalid:
                        try:
                            select = int(input(f"Select option from the VIEW RECORDS section {add.name}"))
                            invalid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        view_Admin(admin)
                    elif select == 2:
                        view_exist_customers(admin)
                    elif select == 3:
                        view_Inventory(admin)
                    elif select == 4:
                        view_customer_history(admin)
                    elif select == 5:
                        view_all_orders(admin)
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

                    invalid = False
                    while not invalid:
                        try:
                            select = int(input(f"Select option from the MODIFY RECORDS section {add.name}"))
                            invalid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")

                    if select == 1:
                        modify_admin(admin)
                    elif select == 2:
                        modify_customer_record(admin)
                    elif select == 3:
                        modify_inventory(admin)
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

                    invalid = False
                    while not invalid:
                        try:
                            select = int(input(f"Select option from the DELETE RECORDS section {add.name}"))
                            invalid = True
                        except:
                            print("Invalid Input. Enter an Integer : [1 , 2 , 3 , 4]")
                    if select == 1:
                        delete_admin(admin)
                    elif select == 2:
                        delete_customer_records(admin)
                    elif select == 3:
                        delete_item(admin)
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

        invalid = False
        while not invalid:
            try:
                input_type = int(input("Enter Option >>>>"))
                invalid = True
            except:
                print("Invalid Input. Enter Input : [1 , 2 , 3 ]")


        if input_type ==1:
            print(f"Welcome Back Customer . Enter Log-In details below:  \n")
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


            invalid = False
            while not invalid:
                try:
                    custID = int(input("Registered Customer ID >>>>>>\n"))
                    invalid = True
                except:
                    print("Invalid input Enter integers only")

            query_customer_login = f"SELECT  * FROM  customers WHERE name ='{name}' AND customerID = {custID};"
            

            my_cursor.execute(query_customer_login)
            record = my_cursor.fetchone()
            

            if record != None:
                logging.info("successful log into customer portal")
                print("Customer Log in successful....\n")
                print("\t1) Place an Order")
                print("\t2) View order History")
                print("\t3) Quit")

                invalid = False
                while not invalid:
                    try:
                        input_type = int(input("Make Selection >>>>"))
                        invalid = True
                    except:
                        print("Invalid input Entered ")
                if input_type == 1:
                    purchase(orders)
                elif input_type == 2:
                    view_customer_history(customer)
                elif input_type == 3:
                    print("***Quiting the CUSTOMERS SECTION ..........<><><>***\n")
                    break
                print(" Please log in! ")
            else:
                print("Unsuccessful Log in Attempt: Wrong Details Entered ")

        elif input_type == 2:
            print("New Customer Account Creation Page ")
            create_new_cust(customer)

        elif input_type == 3:
            print("Quiting The Program")
            break
        else:
            print("Invalid Integer. Enter Input : [1 , 2 , 3 , 4]\n")
            logging.info("Invalid input was entered ")


# ######### NEW ACCT FUNCT. ########

def create_new_cust(): 
    print(f"*****WELCOME NEW CUSTOMER!.... Enter: \tName \t# of Bages ")
    while True:
        try:
            name = str(input(f"Please Enter your name"))
            if re.search("[a-zA-Z]", name):
                break
            else:
                raise ValueError
                
        except ValueError as ve:
            print(f"Invalid name Formaat, NAME HAS TO BE A STRING ")
        else:
            break
    
    invalid = False
    while not invalid:
        try:
            badges = int(input(f"Enter number of Trainer Badges Obtained"))
            invalid = True
        except: 
            print("Invalid input ENTERED ")

        
        
    new_customer=customer(name, badges) 
    query_add_new_customer =f"INSERT INTO customers ( customerID, name, badges)VALUES('{new_customer.custID}''{new_customer.name}','{new_customer.badges}')"
    my_cursor.execute(query_add_new_customer)
    cnx.commit()
    print(f"New Customer Details :\n{new_customer}\n")
    logging.info("new customer account was created ")

def add_new_admin():
   print("****Welcome NEW Admin! Please provide master-admin-code: >>>>>>")
invalid = False
while not invalid:
    try:
        confirmPassword = int(input("Enter master Admin password >>>>:\n"))
        invalid = True
    except:
        print("Invalid Input. Enter an Integer ")

        my_cursor.excute(f"SELECT * FROM mstradmin")       
        for value in my_cursor:
            confirmPassword = value[2]


    while confirmPassword == 28669236:
        print("Successful log in ")
        logging.info("Master Admin acct. logged in ")

        print(f"\nWelcome NEW Admin......... PLEASE Enter YOUR NAME: \n")
while True:
    try:
        name = str(input(f">>>>>>>"))
        if re.search("[a-zA-Z]", name):
                break
        else:
            raise ValueError
                
    except ValueError as ve:
        print("Invalid Name Format........NAME MUST BE A STRING :")

        invalid = False
        while not invalid:
            try:
                admin_passcode = int(input("Enter New Admin Passcode: >>>\n"))
                invalid = True
            except:
                print("Invalid Input. PASSCODE must be an Integer \n")

        add = admin(name, admin_passcode)
        query_add_new_admin = f"INSERT INTO admin (name,passcode)VALUES ('{name}','{admin_passcode}')"

        my_cursor.execute(query_add_new_admin)
        cnx.commit()
        logging.info("a new admin account was created")
        print(f"A new Admin was added \nName: {name} \nPasscode: {admin_passcode}")
        break
else:
    print("Incorrect login ")


def purchase():
    A = "SELECT * FROM inventory"
    my_cursor.execute(A)
    print("***POKEmart Inventory***")

    for record in my_cursor:
        print(record)
        new_items=inventory(record[0], record[1])
    
    invalid = False
    while not invalid:
        try:
            selected_item = str(input("Enter name of Item to Purchase: >>>\n"))
            invalid = True
        except: 
            print("Invalid input Item needs to be a STRING")
    invalid = False
    while not invalid:
        try:
           customerID=int(input("PLease confirm Customer ID"))
           invalid= True
        except: 
            print("INvalid input Customer ID must be an integer")
    B = f"SELECT * FROM inventory WHERE name = {selected_item}"
    my_cursor.execute(B)
    for value in my_cursor:
        name = value [1]
        price = value[2]
    
    query_purchase_byname = f"INSERT INTO orders(customerID, customer, item-name,  price) VALUES('{customerID}','{name}','{selected_item}','{price}')"
    cnx.commit()
    logging.info("A new purchase was made")


def add_new_items(): 
    print("UPDATING INVENTORY PORTAL!!")
    while True:
        try:
            new_item = str(input(f">>>>>>>"))
            if re.search("[a-zA-Z]", name):
                    break
            else:
                raise ValueError
                
        except ValueError as ve:
            print("Invalid Name Format........NAME MUST BE A STRING :")
        else:
            break
    invalid = False
    while invalid != True:
        try:
            price=int(input("Enter Price of New Item to be entered "))
            invalid = True
        
        except ValueError:
            print("Price must be an Integer value: \n")
            invalid = False
        else:
            pass
    print(f"new Item added to INVENTORY")
    query_add_item = f"INSERT INTO inventory (item, price)VALUES ('{new_item}','{price}') "
    my_cursor.execute(query_add_item)
    cnx.commit()
    logging.info("new computer was added to the inventory")

def view_Admin():
    query_all_admin = "SELECT * FROM admin"
    my_cursor.execute(query_all_admin)
    for record in my_cursor:
        print(record)
    logging.info("all admins deatails were viewed")

def view_exist_customers():
    invalid = False
    while not invalid:
        try:
            custID = int(input("Enter Customer ID to view Their Orders: >>>\n"))
            invalid = True
        except:
            print("Invalid Input . Customer ID must be an Integer ")
    query_show_customers_order = f"SELECT * FROM orders WHERE customerID ={custID}"
    my_cursor.execute(query_show_customers_order)
    for record in my_cursor:
        print(record)
        if record == None:
            print("No Previous History")
        logging.info("all placed orders were viewed")

def view_Inventory():
    query_show_all_items = "SELECT * FROM inventory"
    my_cursor.execute(query_show_all_items)
    for record in my_cursor:
        print(record)
    logging.info("inventory was viewed")

def view_customer_history():
    query_show_customer_history = "SELECT * FROM customers"
    my_cursor.execute(query_show_customer_history)
    for record in my_cursor:
        print(record)
    logging.info("CUSTOMER HISTORY was viewed")

def view_all_orders():
    query_show_customer_order = "SELECT * FROM orders"
    my_cursor.execute(query_show_customer_order)
    for record in my_cursor:
        print(record)
    logging.info("ORDER HISTORY was viewed")

def modify_admin():
    my_cursor.execute(f"SELECT * FROM  admin")
    for record in my_cursor:
        print(record)

    admin_id = input("Enter the Admin ID :\n")
    query_admin_to_modify = f"SELECT * FROM admin WHERE adminID ={admin_id}"
    my_cursor.execute(query_admin_to_modify)
    for record in my_cursor:
        print(record)

    for record in my_cursor:
        print(f"\t{record[0]}: NAME: '{record[1]}', PASSWORD: {record[2]}")
    col_to_modify = input("Select Column to modify(name ,password)")
    modified_value = input(f"What will you want to change the  {col_to_modify} to? \n")

    if col_to_modify == 'name':
        new_value = f"UPDATE admin SET {col_to_modify} = '{modified_value}' WHERE adminID ={admin_id}"
    elif col_to_modify == 'passcode':
        new_value = f"UPDATE admin SET {col_to_modify} = '{modified_value}' WHERE adminID ={admin_id}"
    else:
        pass
    my_cursor.execute(new_value)
    cnx.commit()
    logging.info(" An Admin record was modified")

def modify_customer_record():
    query_customer_modify="SELECT * FROM customers"
    my_cursor.execute(query_customer_modify)

    for record in my_cursor:
        print(f"\t{record[0]}: NAME: {record[1]}, Badges: {record[2]}")
    customer_to_modify= input("Enter customers ID")
    col_to_modify= input("Select Column to modify(name, badges)")
    modified_value= input(f"what will you want to change {col_to_modify} to?")

    if col_to_modify =='name':
        new_value=f"UPDATE customers SET {col_to_modify} = '{modified_value}' WHERE customerID ={customer_to_modify}"
    elif col_to_modify== 'badges':
        new_value = f"UPDATE customers SET {col_to_modify} = '{modified_value}' WHERE customerID ={customer_to_modify}"
    else:
        pass
    my_cursor.execute(new_value)
    cnx.commit()
    logging.info("Customer details was modified  ")   

def modify_inventory():
    my_cursor.execute(f"SELECT * FROM  inventory")
    for rec in my_cursor:
        print(rec)

    invalid = False
    while invalid != True:
        try:
            item_name = str(input(f">>>>>>>"))
            if re.search("[a-zA-Z]", name):
                    break
            else:
                raise ValueError
                
        except ValueError as ve:
            print("Invalid Name Format........NAME MUST BE A STRING :")
        except:
            print("Invalid Input. Enter a String ")
        else:
            break
    query_inventory_to_modify= f"SELECT * FROM inventory WHERE item-name  ={item_name}"
    my_cursor.execute(query_inventory_to_modify)
    for record in my_cursor:
        print(record)

    for record in my_cursor:
        print(f"\t{record[0]}: ITEM_NAME: {record[1]}, PRICE: {record[2]} ")
    restart =True
    while restart == True:
        col_to_modify = input("Select Column to modify(item-name, price)")
        if col_to_modify not in ("item-name","price"):
            print("Wrong Format ")
            break

        modified_value = input(f"What will you want to change the  {col_to_modify} to? \n")

        if col_to_modify == 'item-name':
            new_value = f"UPDATE inventory SET {col_to_modify} = '{modified_value}' WHERE item ={item_name}"
        elif col_to_modify == 'price':
            new_value = f"UPDATE inventory SET {col_to_modify} = '{modified_value}' WHERE computerID ={price}"
        else:
            print("Wrong Value Entered ")
            restart =True

        my_cursor.execute(new_value)
        cnx.commit()
        logging.info("INVENTORY was modified ")
        exit()

def delete_admin():
    invalid = False
    while not invalid:
        try:
            input_type = int(input(" Enter Option >>>>"))
            invalid= True
        except:
            print("Invalid Input. Enter an Integer")
            logging.error(" Invalid selection ")

    my_cursor.execute(f"SELECT * FROM admin")
    for value in my_cursor:
        confirmPassword= value[2]

    while confirmPassword ==value[2]:
        print("Successful log in ")
        logging.info("Admin account logged into Delete Admin Portal   ")
        my_cursor.execute(f"SELECT * FROM  admin")
        for record in my_cursor:
            print(record)
        valid = False
        while not valid:
            try:
                admin_id = int(input("Enter the Admin ID to DELETE >>>>:\n"))
                valid = True
            except:
                print("Invalid Input. Enter an Integer ")

        query_admin_to_delete = f"DELETE from admin where adminID = {admin_id}"
        my_cursor.execute(query_admin_to_delete)

        cnx.commit()
        print("Deletion completed..........")
        logging.info("an admin was deleted from the records")
        break
    else:
        print("Incorrect login \nOnly MASTER ADMIN can delete an Administrator")

def delete_customer_records():
    pass

def delete_item():
    pass


    


#     #CURSOR-  points to various tables allowing to insert into our database and query our databses

