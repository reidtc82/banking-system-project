from Transaction import Transaction
from util.TranType import TranType
from util.BankExceptions import UnrecognizedTransactionType


class Account:
    trans_hist = []
    balance = 0.0

    def __init__(self, account_number, description):
        self.account_number = account_number
        self.description = description

    def _credit(self, amt):
        self.balance += amt

    def _debit(self, amt):
        self.balance -= amt

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.trans_hist

    def get_description(self):
        return self.description

    def apply_transaction(self, transaction: Transaction):
        if transaction.get_type() == TranType.DEPOSIT:
            self.__credit(transaction.get_amt())
            self.trans_hist.append(transaction)
        elif transaction.get_type() == TranType.WITHDRAWAL:
            self.__debit(transaction.get_amt())
            self.trans_hist.append(transaction)
        else:
            raise UnrecognizedTransactionType
