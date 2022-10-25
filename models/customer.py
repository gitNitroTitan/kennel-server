# class Customer():
#     """docstring"""
#     def __init__(self, id, name):
#         self.id = id
#         self.address = name

# new_customer = Customer(1, "Dave Gross")

class Customer():
    """docstring"""
    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

new_customer = Customer(1, "Dave Gross", "54 Oak St", "dave@gmail.com", "password")
