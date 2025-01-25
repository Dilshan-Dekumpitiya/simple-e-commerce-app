class Customer:
    def __init__(self, name, address,contact):
        self.name = name
        self.address = address
        self.contact = contact
    
    def get_details(self):
        return f'Customer Name: {self.name}, Customer Address: {self.address}, Customer Contact: {self.contact}'
        

