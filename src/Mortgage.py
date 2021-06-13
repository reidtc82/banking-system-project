from SecuredLoan import SecuredLoan
from Person import Person
from LoanApplication import LoanApplication
from Address import Address


class Mortgage(SecuredLoan):
    """A secured loan type. This is secured by real estate property.

    Args:
        SecuredLoan (Loan): The parent class.
    """

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
        property_address: Address,
    ):
        self.__address = property_address
        super(Mortgage, self).__init__(
            loan_id,
            owner,
            assoc_app,
            original_bal,
            interest,
            description,
            collateral,
            collat_value,
        )

    def get_property_address(self):
        return self.__address
