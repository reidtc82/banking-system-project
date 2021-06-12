from util.AppStatus import AppStatus
from util.AppType import AppType
from Loan import Loan
import datetime


class LoanApplication:
    loan_amount = 0.0
    decision_date = None

    def __init__(
        self,
        application_id,
        first_name,
        last_name,
        ssn,
        description,
        credit_score: int,
        app_type: AppType,
        status=AppStatus.SUBMITTED,
    ):
        self.application_id = application_id
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.description = description
        self.credit_score = credit_score
        self.app_type = app_type
        self.app_status = status
        self.submission_date = datetime.datetime.now()

    def get_application_id(self):
        return self.application_id

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_ssn(self):
        return self.ssn

    def get_credit_score(self):
        return self.credit_score

    def get_app_type(self):
        return self.app_type

    def get_app_status(self):
        return self.app_status

    def set_loan_amount(self, amount):
        self.loan_amount = amount

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def set_app_type(self, app_type):
        self.app_type = app_type

    def cancel_application(self):
        self.app_status = AppStatus.CANCELLED
        self.decision_date = datetime.datetime.now()

    def approve_application(self, id, owner, interest):
        self.app_status = AppStatus.APPROVED
        self.decision_date = datetime.datetime.now()
        return Loan(id, owner, self, self.loan_amount, interest, self.description)

    def deny_application(self):
        self.app_status = AppStatus.DENIED
        self.decision_date = datetime.datetime.now()
