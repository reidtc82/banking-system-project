from Account import Account
from Person import Person


class CustomerAccount(Account):
    overdraft_amount = 0.0

    def __init__(
        self,
        account_number,
        description,
        owner: Person,
        overdraft_limit=0.0,
    ):
        self.owner = owner
        self.overdraft_limit = overdraft_limit
        super().__init__(account_number, description)

    def get_od_limit(self):
        return self.overdraft_limit

    def get_od_amt(self):
        return self.overdraft_amount

    def set_od_limit(self, new_limit):
        self.overdraft_limit = new_limit
