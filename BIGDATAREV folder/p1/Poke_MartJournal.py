# import logging
# import mysql.connector
# import pokedata_base as p
# from Poke_Mart import admin, customer, orders, inventory
# from pokepython_mysql import insert_records, admin_login, customer_login, view_customer_history, modify_customer_records, modify_admin, view_all_customers, add_new_order

# def main():
#     try:
#         cnx = mysql.connector.connect(user=p.user, password=p.password, host=p.host, database="Project_1")
#         my_cursor = cnx.cursor
#     except mysql.connector.Error as mce:
#         print(mce.msg)
#         return
#     except Exception as e:
#         print("ERROR:Exiting the program")
#         return
#     logging.basicConfig(filename="POKEmart.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
#     my_cursor.close() #CHECK IF THESE ARE NEEDED HERE
#     cnx.close()


# insert()
# admin_login()










if __name__ == "__main__":
    main()


