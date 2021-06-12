class Address:
    def __init__(self, street, city, state, postal, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postal = postal

    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_postal_code(self, postal):
        self.postal = postal

    def set_country(self, country):
        self.country = country

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_postal_code(self):
        return self.postal

    def get_country(self):
        return self.country

    def print_mail(self):
        print(f"{self.street}\n{self.city}, {self.state} {self.postal}")
