class admin ():
    def __init__(self, admin_ID, name, admin_passcode):
        self.name=str(name)
        self.admin_ID=int(admin_ID)
        self.admin_passcode=int(admin_passcode)

class customer ():
    def __init__(self, custID, name, badges):
        self.custID=int(custID)
        self.name = str(name)
        self.badges = int(badges)

class orders ():
    def __init__(self, item, price):
        self.item=str(item)
        self.orders=int(price)

class inventory():
    def __init__(self,item_name, new_item, price):
        self.item_name=str(item_name)
        self.new_item=str(new_item)
        self.price=int(price)