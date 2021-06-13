from Person import Person
from SecuredLoan import SecuredLoan
from Address import Address
from LoanApplication import LoanApplication


class AutoLoan(SecuredLoan):
    """A child to SecuredLoan for specific loan types for vehicles.

    Args:
        SecuredLoan (Loan): This is a secured loan type that would have
                            collateral. In this child AutoLoan that
                            collateral is a vehicle.
    """

    def __init__(
        self,
        loan_id,
        owner: Person,
        assoc_app: LoanApplication,
        original_bal,
        interest,
        description,
        collat_value,
        make,
        model,
        year,
        classification="New",
    ):
        self._make = make
        self._model = model
        self._year = year
        self._classification = classification
        super(AutoLoan, self).__init__(
            loan_id,
            owner,
            assoc_app,
            original_bal,
            interest,
            description,
            f"{classification} {year} {make} {model}",
            collat_value,
        )

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_classification(self):
        return self._classification
