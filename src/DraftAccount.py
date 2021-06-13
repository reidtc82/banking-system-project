from CustomerAccount import CustomerAccount
from Person import Person
from Transaction import Transaction
from util.TranType import TranType
from util.BankExceptions import UnrecognizedTransactionType, OverdraftLimitExceeded
from GLAccount import GLAccount


class DraftAccount(CustomerAccount):
    """Inherits from CustomerAccount

    Args:
        CustomerAccount (Account): PArent of this class.
    """

    def __init__(
        self,
        account_number,
        description,
        owner: Person,
        draft_income_gl: GLAccount,
        fee_amt=0.0,
        overdraft_limit=0.0,
    ):
        self.fee_amt = fee_amt
        self.draft_income_gl = draft_income_gl
        super().__init__(
            account_number, description, owner, overdraft_limit=overdraft_limit
        )

    def get_fee(self):
        return self.fee_amt

    def set_fee(self, new_fee):
        self.fee_amt = new_fee

    def apply_transaction(self, transaction: Transaction):
        """Overrides super. In draft accounts there is additional behavior to check balance
           and apply overdraft in the case of insufficient funds (NSF).

        Args:
            transaction (Transaction): The transaction to be applied.

        Raises:
            OverdraftLimitExceeded: Raised when OD limit is exceeded by the transaction.
            UnrecognizedTransactionType: Same behavior as super.
        """
        if transaction.get_type() == TranType.DEPOSIT:
            self.balance += transaction.get_amt()
            self.trans_hist.append(transaction)
        elif transaction.get_type() == TranType.WITHDRAWAL:
            if self.balance - transaction.get_amt() < 0.0:
                if (
                    abs(self.balance - transaction.get_amt()) <= self.overdraft_limit
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
        elif transaction.get_type() == TranType.FEE:
            self.apply_fee(self.draft_income_gl)
        else:
            raise UnrecognizedTransactionType

    def apply_fee(self, receiving_gl: GLAccount):
        """Allows the application of a fee.

        Args:
            receiving_gl (GLAccount): The GL account to recieve the fee proceeds.
        """
        self.apply_transaction(
            Transaction(self.fee_amt, TranType.FEE, 0, f"Fee charge")
        )
        self.draft_income_gl.apply_transaction(
            Transaction(self.fee_amt, TranType.DEPOSIT, 0, f"Fee income applied")
        )
