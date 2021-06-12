from Person import Person
import Address


class Customer(Person):
    ofac_clear = False
    ofac_date = None
    applications = []
    accounts = []
    loans = []
    ctr = 0.0

    def __init__(self, id, credit_score, name, phone, email, ssn_tin, address: Address):
        self.id = id
        self.credit_score = credit_score
        super(Customer, self).__init__(id, name, phone, email, ssn_tin, address)

    def get_daily_ctr(self):
        return self.ctr

    def get_ofac_clear(self):
        return self.ofac_clear

    def get_ofac_date(self):
        return self.ofac_date

    def get_credit_score(self):
        return self.credit_score

    def get_applications(self):
        return self.applications

    def get_loans(self):
        return self.loans

    def get_accounts(self):
        return self.accounts

    def apply_ctr(self, cash_tran_amt):
        self.ctr += cash_tran_amt

    def reset_ctr(self):
        self.ctr = 0.0

    def set_ofac(self, ofac_result):
        self.ofac_clear = ofac_result

    def set_ofac_date(self, ofac_date):
        self.ofac_date = ofac_date

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def add_application(self, new_app):
        self.applications.append(new_app)

    def add_loan(self, new_loan):
        self.loans.append(new_loan)

    def add_account(self, new_acct):
        self.accounts.append(new_acct)
