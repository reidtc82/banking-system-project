from Person import Person
from Loan import Loan
from LoanApplication import LoanApplication


class CreditCardLoan(Loan):
    """An unsecured type of loan. Differing in that the limit is revolving.

    Args:
        Loan (Loan): Parent class that is inherited from.
    """

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
        """Just to increase the limit.

        Args:
            amount (float, optional): This is the amount to be added to the limit.
                                      Use negative value for subtraction.
                                      Defaults to 0.0.
        """
        self.credit_limit += amount
