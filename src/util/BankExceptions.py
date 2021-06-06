class VaultLimitExceeded(Exception):
    def __init__(
        self, message="Employee vault limit exceeded. Cannot purchase more cash."
    ):
        self.message = message
        super().__init__(self.message)


class InsufficientDrawerBalance(Exception):
    def __init__(self, message="Employee drawer balance insufficient for sale."):
        self.message = message
        super().__init__(self.message)


class UnrecognizedTransactionType(Exception):
    def __init__(
        self,
        message="This transaction type is not recognized. Transaction will not be recorded.",
    ):
        self.message = message
        super().__init__(self.message)


class OverdraftLimitExceeded(Exception):
    def __init__(
        self,
        message="Overdraft limit has been exceeded. Transaction will not be recorded.",
    ):
        self.message = message
        super().__init__(self.message)


class RegulationDLimitMet(Exception):
    def __init__(
        self,
        message="Regulation D limit has been exceeded. Transaction will not be recorded.",
    ):
        self.message = message
        super().__init__(self.message)
