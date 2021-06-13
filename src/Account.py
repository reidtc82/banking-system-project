from Transaction import Transaction
from util.TranType import TranType
from util.BankExceptions import UnrecognizedTransactionType


class Account:
    """Parent account class

    Raises:
        UnrecognizedTransactionType: Raised when transaction type is not recognized.

    """

    trans_hist = []
    _balance = 0.0

    def __init__(self, account_number, description):
        self.account_number = account_number
        self.description = description

    def __credit(self, amt):
        """Private function for applying credit to account

        Args:
            amt (float): The amount to credi tto the balance.
        """
        self._balance += amt

    def __debit(self, amt):
        """Private function to debit account

        Args:
            amt (float): The amount to deit to the balance.
        """
        self._balance -= amt

    def get_account_number(self):
        """Accessor for the account number

        Returns:
            string: This is the account number.
        """
        return self.account_number

    def get_balance(self):
        """Accessor for balance

        Returns:
            float: This is the balance.
        """
        return self._balance

    def get_transaction_history(self):
        """Accessor for transaction history

        Returns:
            [Transaction]: Returns list of transactions that have been applied to this account.
        """
        return self.trans_hist

    def get_description(self):
        """Accessor for description

        Returns:
            string: The account's description
        """
        return self.description

    def apply_transaction(self, transaction: Transaction):
        """Public function to apply a transaction.

        Determines type of transaction byt it's type and calls the private functions
        __credit or __debit to apply it to the balance.

        Args:
            transaction (Transaction): This si the transaction to apply to the balance.

        Raises:
            UnrecognizedTransactionType: Raised if the transaction passed has a type thaat is not
                                         allowed for application to an account balance.
        """
        if transaction.get_type() == TranType.DEPOSIT:
            self.__credit(transaction.get_amt())
            self.trans_hist.append(transaction)
        elif transaction.get_type() == TranType.WITHDRAWAL:
            self.__debit(transaction.get_amt())
            self.trans_hist.append(transaction)
        else:
            raise UnrecognizedTransactionType
