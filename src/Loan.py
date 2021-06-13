from Person import Person
import LoanApplication


class Loan:
    _balance = 0.0

    def __init__(
        self,
        loan_id,
        owner: Person,
        assoc_app: LoanApplication,
        original_bal,
        interest,
        description,
    ):
        self.id = loan_id
        self.owner = owner
        self.__assoc_app = assoc_app
        self.__original_bal = original_bal
        self._balance = original_bal
        self.interest = interest
        self.description = description

    def set_interest(self, interest):
        self.interest = interest

    def set_description(self, description):
        self.description = description

    def apply_interest(self):
        self._balance *= 1 + self.interest

    def apply_payment(self, payment):
        self._balance -= payment

    def get_id(self):
        return self.id

    def get_owner(self):
        return self.owner

    def get_application(self):
        return self.__assoc_app

    def get_original_balance(self):
        return self.__original_bal

    def get_balance(self):
        return self._balance

    def get_interest(self):
        return self.interest

    def get_description(self):
        return self.description
