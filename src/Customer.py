from Person import Person
import Address


class Customer(Person):
    ofac_clear = False
    ofac_date = None
    applications = []
    accounts = []
    loans = []

    def __init__(
        self, id, ctr, credit_score, name, phone, email, ssn_tin, address: Address
    ):
        self.id = id
        self.ctr = ctr
        self.credit_score = credit_score
        super(Customer, self).__init__(name, phone, email, ssn_tin, address)
