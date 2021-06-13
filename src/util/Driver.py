from Address import Address
from DraftAccount import DraftAccount
from LoanApplication import LoanApplication
from RegDAccount import RegDAccount
from util.AppStatus import AppStatus
from util.GLType import GLType
from GLAccount import GLAccount
from Customer import Customer
from Loan import Loan
import pickle


class Driver:
    __prompt = f"Enter menu selection: "
    __menus = {}

    fake_db = {
        "account_list": [],
        "people_list": [],
        "loan_list": [],
        "applications_list": [],
        "gl_list": [],
    }

    def __init__(self):
        if (not self.fake_db[key] for key in self.fake_db.keys()):
            try:
                self.load_db()
                print(f"fakedatabase opened")
            except:
                self.write_db()
                print(f"fakedatabase created")

        self.__menus = {
            "Main Menu": {
                "Account Manager": self.account_menu,
                "GL Manager": self.gl_menu,
                "Loan Manager": self.loan_menu,
                "Customer Manager": self.customer_menu,
                "Exit": self.end_program,
            },
            "Account Menu": {
                "Create New": self.create_account,
                "Manage Existing": self.manage_account,
                "Return": self.main_menu,
            },
            "GL Menu": {
                "Create New": self.create_gl,
                "Manage Existing": self.manage_gl,
                "Return": self.main_menu,
            },
            "Loan Menu": {
                "New Loan Application": self.create_application,
                "Work Application": self.work_application,
                "Work Existing Loan": self.work_loan,
                "Return": self.main_menu,
            },
            "Customer Menu": {
                "New Customer": self.create_customer,
                "Manage Existing": self.manage_customer,
                "Return": self.main_menu,
            },
        }

    def start(self):
        self.menu_handler("Main Menu")

    def menu_handler(self, this_menu):
        print(f"\n{this_menu}")
        menu_items = list(self.__menus[this_menu].keys())
        for i, v in enumerate(menu_items):
            print(f"{i} {v}")
        selection = int(input("Enter selection... "))
        self.__menus[this_menu][menu_items[selection]]()

    def main_menu(self):
        self.menu_handler("Main Menu")

    def account_menu(self):
        self.menu_handler("Account Menu")

    def gl_menu(self):
        self.menu_handler("GL Menu")

    def loan_menu(self):
        self.menu_handler("Loan Menu")

    def customer_menu(self):
        self.menu_handler("Customer Menu")

    def create_account(self):
        print(f"\nAccount Creation")
        if not self.fake_db["people_list"]:
            print(f"No Customers exist. Please create a customer before an Account...")
            self.menu_handler("Customer Menu")
        elif not self.fake_db["gl_list"]:
            print(f"No GL accounts exist. Please create a GL account first...")
            self.menu_handler("GL Menu")
        else:
            print(f"1 Checking")
            print(f"2 Savings")
            ac_type = int(input(f"Enter account type... "))
            account_number = input(f"Enter new account number... ")
            description = input(f"Enter description... ")
            owner = input(f"Enter owner's customer ID... ")
            draft_income_gl = input(f"Enter fee GL number... ")
            overdraft_limit = input(f"Enter overdraft limit... ")
            if ac_type == 1:
                fee_amt = input(f"Enter fee amount... ")
                temp_ac = DraftAccount(
                    account_number,
                    description,
                    owner,
                    draft_income_gl,
                    fee_amt,
                    overdraft_limit,
                )
                self.fake_db["account_list"].append(temp_ac)
                self.write_db()
            elif ac_type == 2:
                interest = input(f"Enter interest rate... ")
                temp_ac = RegDAccount(
                    account_number, description, owner, overdraft_limit, interest
                )
                self.fake_db["account_list"].append(temp_ac)
                self.write_db()
            else:
                print(f"That is not a valid account type...")
                self.menu_handler("Account Menu")
        self.menu_handler("Account Menu")

    def manage_account(self):
        print(f"\nManaging an Account")
        if not self.fake_db["account_list"]:
            print(f"No Accounts exist. Please create an Account...")
            self.menu_handler("Account Menu")
        else:
            menu = ["List All", "Get Balance", "List Transactions", "Return"]

            ac_nums = {}
            for ac in self.fake_db["account_list"]:
                ac_nums[ac.get_account_number()] = ac

            selection = None
            while selection != 3:
                print("\n")
                for i, v in enumerate(menu):
                    print(f"{i} {v}")

                selection = int(input("Enter selection... "))
                if selection == 0:
                    print("\n")
                    for i, v in enumerate(self.fake_db["account_list"]):
                        print(f"{v.get_account_number()} {v.get_description()}")
                elif selection == 1:
                    ac_sel = input(f"Input Account number... ")
                    print(ac_nums.keys())
                    if ac_sel not in ac_nums.keys():
                        print(f"That account does not exist...")
                    else:
                        print(
                            f"\nAccount {ac_sel} balance is {ac_nums[ac_sel].get_balance()}"
                        )
                elif selection == 2:
                    ac_sel = input(f"Input Account number... ")
                    if ac_sel not in ac_nums.keys():
                        print(f"That account does not exist...")
                    else:
                        print("\n")
                        for i, v in enumerate(
                            ac_nums[ac_sel].get_transaction_history()
                        ):
                            print(
                                f"{v.get_tran_date()} {v.get_tran_amt()} {v.get_description()}"
                            )

            self.menu_handler("Account Menu")

    def create_gl(self):
        print(f"\nGL Creation")

        types = [
            GLType.ASSET,
            GLType.EXPENSE,
            GLType.PAYABLE,
            GLType.LIABILITY,
        ]
        ac_num = input(f"Enter a new GL Account Number... ")
        desc = input(f"Enter GL Account description... ")

        for i, v in enumerate(types):
            print(f"{i} {v}")
        gl_type = types[int(input(f"Select GL Account Type... "))]

        self.fake_db["gl_list"].append(GLAccount(ac_num, gl_type, desc))

        self.write_db()

        self.menu_handler("GL Menu")

    def manage_gl(self):
        print(f"\nManaging a GL")
        if not self.fake_db["gl_list"]:
            print(f"No GLs exist. Please create a GL...")
            self.menu_handler("GL Menu")
        else:
            menu = ["List All", "Get Balance", "List Transactions", "Return"]

            gl_nums = {}
            for gl in self.fake_db["gl_list"]:
                gl_nums[gl.get_account_number()] = gl

            selection = None
            while selection != 3:
                print("\n")
                for i, v in enumerate(menu):
                    print(f"{i} {v}")

                selection = int(input("Enter selection... "))
                if selection == 0:
                    print("\n")
                    for i, v in enumerate(self.fake_db["gl_list"]):
                        print(f"{v.get_account_number()} {v.get_description()}")
                elif selection == 1:
                    gl_sel = input(f"Input GL Account number... ")
                    print(gl_nums.keys())
                    if gl_sel not in gl_nums.keys():
                        print(f"That GL does not exist...")
                    else:
                        print(
                            f"\nGL {gl_sel} balance is {gl_nums[gl_sel].get_balance()}"
                        )
                elif selection == 2:
                    gl_sel = input(f"Input GL Account number... ")
                    if gl_sel not in gl_nums.keys():
                        print(f"That GL does not exist...")
                    else:
                        print("\n")
                        for i, v in enumerate(
                            gl_nums[gl_sel].get_transaction_history()
                        ):
                            print(
                                f"{v.get_tran_date()} {v.get_tran_amt()} {v.get_description()}"
                            )

            self.menu_handler("GL Menu")

    def create_application(self):
        print(f"\nApplication Creation")
        if not self.fake_db["people_list"]:
            print(f"No Customers exist. PLease create a Customer first...")
            self.menu_handler("Customer Menu")
        elif not self.fake_db["account_list"]:
            print(f"No Accounts exist. Please create an Account first...")
            self.menu_handler("Account Menu")
        else:
            application_id = input(f"Enter new application ID... ")
            first_name = input(f"Enter first name of applicant... ")
            last_name = input(f"Enter last name of applicant... ")
            ssn = input(f"Enter ssn... ")
            description = input(f"Enter loan description... ")
            credit_score = int(input(f"Enter credit score... "))
            app_type = input(f"Application type... ")
            status = AppStatus.SUBMITTED
            temp_app = LoanApplication(
                application_id,
                first_name,
                last_name,
                ssn,
                description,
                credit_score,
                app_type,
                status,
            )
            self.fake_db["application_list"].append(temp_app)
            self.write_db()
        self.menu_handler("Loan Menu")

    def work_application(self):
        print(f"\nWorking an Application")
        if not self.fake_db["applications_list"]:
            print(f"No Applications exist. Please create an Application...")
            self.menu_handler("Loan Menu")
        else:
            app_id = input(f"Enter application id... ")
            print(f"\n1 Approve")
            print(f"2 Deny")
            decision = int(input(f"Enter choice... "))
            if decision == 1:
                owner = self.fake_db["people_list"][input(f"Enter owner id... ")]
                interest = input(f"Input interest rate... ")
                temp_ln = Loan(
                    *self.fake_db["application_list"][app_id].approve_application(
                        self, app_id, owner, interest
                    )
                )
                self.fake_db["loan_list"].append(temp_ln)
                self.write_db()
            elif decision == 2:
                self.fake_db["application_list"].deny_application()
                self.write_db()
            else:
                self.menu_handler("Loan Menu")
        self.menu_handler("Loan Menu")

    def work_loan(self):
        print(f"\nWorking a loan")
        if not self.fake_db["loan_list"]:
            print(f"No Loans exist. Please book a Loan from an Application...")
            self.menu_handler("Loan Menu")
        else:
            sel_ln = self.fake_db["loan_list"][int(input(f"Enter loan ID... "))]
            selection = int(
                input(f"1 Make payment\n2 Check balance\nEnter selection... ")
            )
            if selection == 1:
                sel_ln.apply_payment(float(input(f"Enter payment amount... ")))
                self.write_db()
            elif selection == 2:
                print(f"Loan {sel_ln.get_id()} balance is {sel_ln.get_balance()}")
            else:
                self.menu_handler("Loan Menu")

        self.menu_handler("Loan Menu")

    def create_customer(self):
        print(f"\nCustomer Creation")
        id = input("Enter Customer ID... ")
        name = input("Enter Customer name... ")
        ssn_tin = input("Enter Customer SSN/TIN...")
        phone = input("Enter phone... ")
        email = input("Enter email... ")
        credit_score = input("Enter credit score... ")

        address = self.create_address()
        self.fake_db["people_list"].append(
            Customer(id, credit_score, name, phone, email, ssn_tin, address)
        )

        self.write_db()

        self.menu_handler("Customer Menu")

    def create_address(self):
        street = input("Enter street... ")
        city = input("Enter city... ")
        state = input("Enter state... ")
        postal = input("Enter postal... ")
        country = input("Enter country... ")

        return Address(street, city, state, postal, country)

    def manage_customer(self):
        print(f"\nManaging a customer")
        if not self.fake_db["people_list"]:
            print(f"No Customers exist. PLease create a Customer...")
            self.menu_handler("Customer Menu")
        else:
            menu = [
                "List all Customers",
                "List Accounts",
                "List Loans",
                "List Applications",
                "Update Address",
                "Return",
            ]

            selection = None
            while selection != 5:
                print("\n")
                for i, v in enumerate(menu):
                    print(f"{i} {v}")

                cust_ids = {}
                for cust in self.fake_db["people_list"]:
                    cust_ids[cust.get_id()] = cust

                selection = int(input("Enter selection... "))

                if selection == 0:
                    print("\n")
                    for i, v in enumerate(self.fake_db["people_list"]):
                        print(f"{v.get_id()} {v.get_name()}")
                elif selection == 1:
                    selection = input("Enter customer id... ")
                    if selection not in cust_ids.keys():
                        print("That customer does not exist... ")
                    else:
                        print("\n")
                        for i, v in enumerate(cust_ids[selection].get_accounts()):
                            print(v.get_account_number())
                elif selection == 2:  # loans
                    selection = input("Enter customer id... ")
                    if selection not in cust_ids.keys():
                        print("That customer does not exist... ")
                    else:
                        print("\n")
                        for i, v in enumerate(cust_ids[selection].get_loans()):
                            print(v.get_id())
                elif selection == 3:  # applicaitons
                    selection = input("Enter customer id... ")
                    if selection not in cust_ids.keys():
                        print("That customer does not exist... ")
                    else:
                        print("\n")
                        for i, v in enumerate(cust_ids[selection].get_applications()):
                            print(v.get_application_id())
                elif selection == 4:  # update address
                    selection = input("Enter customer id... ")
                    if selection not in cust_ids.keys():
                        print("That customer does not exist... ")
                    else:
                        print("\n")
                        print(
                            f"Old address:\n{cust_ids[selection].get_address().print_mail()}"
                        )
                        cust_ids[selection].set_address(self.create_address())
                        print(
                            f"New address:\n{cust_ids[selection].get_address().print_mail()}"
                        )
            self.write_db()
            self.menu_handler("Customer Menu")

    def end_program(self):
        quit()

    def load_db(self):
        with open("fake_db.pickle", "rb") as f:
            self.fake_db = pickle.load(f)

    def write_db(self):
        with open("fake_db.pickle", "wb") as f:
            pickle.dump(self.fake_db, f)
