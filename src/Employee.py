from Customer import Customer
from util.BankExceptions import InsufficientDrawerBalance, VaultLimitExceeded
import Address


class Employee(Customer):
    drawer_balance = 0.0

    def __init__(
        self,
        employee_id,
        role,
        department,
        salary,
        credit_score,
        name,
        phone,
        email,
        ssn_tin,
        address: Address,
        v_access=False,
        wd_limit=50000.00,
        dep_limit=50000.00,
        vault_limit=50000.00,
    ):
        self.employee_id = employee_id
        self.role = role
        self.department = department
        self.vault_access = v_access
        self.withdrawal_limit = wd_limit
        self.deposit_limit = dep_limit
        self.vault_limit = vault_limit
        self.salary = salary
        super(Employee, self).__init__(
            employee_id, credit_score, name, phone, email, ssn_tin, address
        )

    def get_employee_id(self):
        return self.employee_id

    def get_role(self):
        return self.role

    def get_department(self):
        return self.department

    def get_withdrawal_limit(self):
        return self.withdrawal_limit

    def get_deposit_limit(self):
        return self.deposit_limit

    def get_drawer_balance(self):
        return self.drawer_balance

    def get_salary(self):
        return self.salary

    def get_vault_access(self):
        return self.vault_access

    def set_role(self, new_role):
        self.role = new_role

    def set_department(self, new_department):
        self.department = new_department

    def set_vault_access(self, access: bool):
        self.vault_access = access

    def set_withdrawal_limit(self, new_limit):
        self.withdrawal_limit = new_limit

    def set_deposit_limit(self, new_limit):
        self.deposit_limit = new_limit

    def set_salary(self, new_salary):
        self.salary = new_salary

    def buy_vault_cash(self, amount):
        if self.drawer_balance + amount < self.vault_limit:
            self.drawer_balance += amount
        else:
            raise VaultLimitExceeded

    def sell_vault_cash(self, amount):
        if self.drawer_balance - amount >= 0.0:
            self.drawer_balance -= amount
        else:
            raise InsufficientDrawerBalance
