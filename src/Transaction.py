from util.TranType import TranType
from datetime import datetime


class Transaction:
    """A basic transaction"""

    def __init__(self, tran_amt, tran_type: TranType, merchant_code, description):
        self.__tran_amt = tran_amt
        self.__tran_type = tran_type
        self.__merchant_code = merchant_code
        self.__description = description
        self.__tran_date = datetime.now()

    def get_amt(self):
        return self.__tran_amt

    def get_type(self):
        return self.__tran_type

    def get_merchant_code(self):
        return self.__merchant_code

    def get_description(self):
        return self.__description

    def get_tran_date(self):
        return self.__tran_date
