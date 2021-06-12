import Address


class Person:
    def __init__(self, id, name, phone, email, ssn_tin, address: Address):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.ssn_tin = ssn_tin
        self.address = address

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_ssn_tin(self):
        return self.ssn_tin

    def get_address(self):
        return self.address

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_address(self, address: Address):
        self.address = address
