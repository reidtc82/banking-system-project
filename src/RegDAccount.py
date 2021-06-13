from CustomerAccount import CustomerAccount
from Person import Person
from Transaction import Transaction
from util.TranType import TranType
from util.BankExceptions import (
    UnrecognizedTransactionType,
    RegulationDLimitMet,
    OverdraftLimitExceeded,
)


class RegDAccount(CustomerAccount):
    """Regulation D is applied to US savings accounts and limits total count of monthly withdrawals.

    Args:
        CustomerAccount (Account): The parent class.

    Raises:
        OverdraftLimitExceeded: As in super, this is raised when the overdraft limit is exceeded.
        RegulationDLimitMet: Raised when maximum withdraws allowed are met.
        UnrecognizedTransactionType: As in super, raised when the transaction type is not allowed.

    """

    __REG_D_MAX = 6
    withdrawal_count = 0

    def __init__(
        self, account_number, description, owner: Person, overdraft_limit, interest
    ):
        self.interest = interest
        super().__init__(
            account_number, description, owner, overdraft_limit=overdraft_limit
        )

    def get_withdrawal_count(self):
        return self.withdrawal_count

    def get_interest(self):
        return self.interest

    def set_interest(self, new_int):
        self.interest = new_int

    def reset_withdrawal_count(self):
        self.withdrawal_count = 0

    def apply_transaction(self, transaction: Transaction):
        """Overrides super as the behaviors for applying certain transactions differs.
           For reg D accounts, infinite deposits are allowed, but only
           a specified number of withdrawals.

        Args:
            transaction (Transaction): The transaction to apply.

        Raises:
            OverdraftLimitExceeded: Raised when the limit is exceeded.
            RegulationDLimitMet: Raised when the limit is is met.
            UnrecognizedTransactionType: Rasied when teh transaction type is not allowed.
        """
        if transaction.get_type() == TranType.DEPOSIT:
            self._balance += transaction.get_amt
            self.trans_hist.append(transaction)
        elif transaction.get_type() == TranType.WITHDRAWAL:
            if self.withdrawal_count < self.__REG_D_MAX:
                if self._balance - transaction.get_amt() < 0.0:
                    if (
                        abs(self._balance - transaction.get_amt())
                        <= self.overdraft_limit
                        and abs(self._balance - transaction.get_amt())
                        <= self.overdraft_amount
                    ):
                        self._balance -= transaction.get_amt()
                        self.trans_hist.append(transaction)
                    else:
                        raise OverdraftLimitExceeded
                else:
                    self._balance -= transaction.get_amt()
                    self.trans_hist.append(transaction)
            else:
                raise RegulationDLimitMet
        else:
            raise UnrecognizedTransactionType
