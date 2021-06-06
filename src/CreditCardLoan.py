from Person import Person
from Loan import Loan
from LoanApplication import LoanApplication


class CreditCardLoan(Loan):
    def __init__(
        self,
        loan_id,
        owner: Person,
        assoc_app: LoanApplication,
        interest,
        description,
        credit_limit,
        bin,
        original_bal=0.0,
    ):
        self.credit_limit = credit_limit
        self.__bin = bin
        super(CreditCardLoan, self).__init__(
            loan_id, owner, assoc_app, original_bal, interest, description
        )

    def get_bin(self):
        return self.__bin

    def get_credit_limit(self):
        return self.credit_limit

    def increase_credit_limit(self, amount=0.0):
        self.credit_limit += amount
