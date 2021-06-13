from Account import Account
from util.GLType import GLType


class GLAccount(Account):
    """General Ledger account

    Args:
        Account (Object): The parent class.
    """

    def __init__(self, account_number, gl_type: GLType, description):
        self.gl_type = gl_type
        super().__init__(account_number, description)

    def get_type(self):
        return self.gl_type

    def set_type(self, new_type: GLType):
        self.gl_type = new_type
