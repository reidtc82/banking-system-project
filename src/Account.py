from Transaction import Transaction
from util.TranType import TranType
from util.BankExceptions import UnrecognizedTransactionType


class Account:
    trans_hist = []

    def __init__(self, account_number, balance=0.0):
        self.balance = balance
        self.account_number = account_number

    def __credit(self, amt):
        self.balance += amt

    def __debit(self, amt):
        self.balance -= amt

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.trans_hist

    def apply_transaction(self, transaction: Transaction):
        if transaction.get_type() == TranType.DEPOSIT:
            self.__credit(transaction.get_amt())
            self.trans_hist.append(transaction)
        elif transaction.get_type() == TranType.WITHDRAWAL:
            self.__debit(transaction.get_amt())
            self.trans_hist.append(transaction)
        else:
            raise UnrecognizedTransactionType
