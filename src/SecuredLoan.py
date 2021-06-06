from Person import Person
from Loan import Loan
from LoanApplication import LoanApplication


class SecuredLoan(Loan):
    def __init__(
        self,
        loan_id,
        owner: Person,
        assoc_app: LoanApplication,
        original_bal,
        interest,
        description,
        collateral,
        collat_value,
    ):
        self.collateral = collateral
        self.collat_value = collat_value
        super(SecuredLoan, self).__init__(
            loan_id,
            owner,
            assoc_app,
            original_bal,
            interest,
            description,
        )

    def get_collateral(self):
        return self.collateral

    def get_collat_value(self):
        return self.collat_value

    def set_collateral(self, new_collat):
        self.collateral = new_collat

    def set_collateraal_value(self, new_val):
        self.collat_value = new_val
