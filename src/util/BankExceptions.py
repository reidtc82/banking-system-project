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
