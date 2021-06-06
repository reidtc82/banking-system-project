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
    __REG_D_MAX = 6
    withdrawal_count = 0

    def __init__(
        self, account_number, owner: Person, overdraft_limit, interest, balance=0.0
    ):
        self.interest = interest
        super().__init__(
            account_number, owner, overdraft_limit=overdraft_limit, balance=balance
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
        if transaction.get_type() == TranType.DEPOSIT:
            self.balance += transaction.get_amt
            self.trans_hist.append(transaction)
        elif transaction.get_type() == TranType.WITHDRAWAL:
            if self.withdrawal_count < self.__REG_D_MAX:
                if self.balance - transaction.get_amt() < 0.0:
                    if (
                        abs(self.balance - transaction.get_amt())
                        <= self.overdraft_limit
                        and abs(self.balance - transaction.get_amt())
                        <= self.overdraft_amount
                    ):
                        self.balance -= transaction.get_amt()
                        self.trans_hist.append(transaction)
                    else:
                        raise OverdraftLimitExceeded
                else:
                    self.balance -= transaction.get_amt()
                    self.trans_hist.append(transaction)
            else:
                raise RegulationDLimitMet
        else:
            raise UnrecognizedTransactionType
