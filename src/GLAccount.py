from Account import Account
from util.GLType import GLType


class GLAccount(Account):
    def __init__(self, account_number, gl_type: GLType, balance=0.0):
        self.gl_type = gl_type
        super().__init__(account_number, balance=balance)

    def get_type(self):
        return self.gl_type

    def set_type(self, new_type: GLType):
        self.gl_type = new_type
