from Address import Address
from util.GLType import GLType
from GLAccount import GLAccount
from Customer import Customer

class Driver:
    __prompt = f"Enter menu selection: "
    __menus = {}

    account_list = []
    people_list = []
    loan_list = []
    applications_list = []
    gl_list = []

    def __init__(self):

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
        if not self.people_list:
            print(f"No Customers exist. Please create a customer before an Account...")
            self.menu_handler("Customer Menu")
        else:
            pass

    def manage_account(self):
        print(f"\nManaging an Account")
        if not self.account_list:
            print(f"No Accounts exist. Please create an Account...")
            self.menu_handler("Account Menu")
        else:
            pass

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

        self.gl_list.append(GLAccount(ac_num, gl_type, desc))

        self.menu_handler("GL Menu")

    def manage_gl(self):
        print(f"\nManaging a GL")
        if not self.gl_list:
            print(f"No GLs exist. Please create a GL...")
            self.menu_handler("GL Menu")
        else:
            menu = ["List All", "Get Balance", "List Transactions", "Return"]
            

            gl_nums = {}
            for gl in self.gl_list:
                gl_nums[gl.get_account_number()] = gl

            selection = None
            while selection != 3:
                print('\n')
                for i, v in enumerate(menu):
                    print(f"{i} {v}")

                selection = int(input("Enter selection... "))
                if selection == 0:
                    print('\n')
                    for i, v in enumerate(self.gl_list):
                        print(f"{v.get_account_number()} {v.get_description()}")
                elif selection == 1:
                    gl_sel = input(f"Input GL Account number... ")
                    print(gl_nums.keys())
                    if gl_sel not in gl_nums.keys():
                        print(f'That GL does not exist...')
                    else:
                        print(f'\nGL {gl_sel} balance is {gl_nums[gl_sel].get_balance()}')
                elif selection == 2:
                    gl_sel = input(f"Input GL Account number... ")
                    if gl_sel not in gl_nums.keys():
                        print(f"That GL does not exist...")
                    else:
                        print('\n')
                        for i,v in enumerate(gl_nums[gl_sel].get_transaction_history()):
                            print(f"{v.get_tran_date()} {v.get_tran_amt()} {v.get_description()}")
            
            self.menu_handler("GL Menu")

    def create_application(self):
        print(f"\nApplication Creation")
        if not self.people_list:
            print(f"No Customers exist. PLease create a Customer first...")
            self.menu_handler("Customer Menu")
        elif not self.account_list:
            print(f"No Accounts exist. Please create an Account first...")
            self.menu_handler("Account Menu")
        else:
            pass

    def work_application(self):
        print(f"\nWorking an Application")
        if not self.applications_list:
            print(f"No Applications exist. Please create an Application...")
            self.menu_handler("Loan Menu")
        else:
            pass

    def work_loan(self):
        print(f"\nWorking a loan")
        if not self.loan_list:
            print(f"No Loans exist. Please book a Loan from an Application...")
            self.menu_handler("Loan Menu")
        else:
            pass

    def create_customer(self):
        print(f"\nCustomer Creation")
        id = input("Enter Customer ID... ")
        name = input("Enter Customer name... ")
        ssn_tin = input("Enter Customer SSN/TIN...")
        street = input("Enter street... ")
        city = input("Enter city... ")
        state = input("ENter state... ")
        postal = input("Enter postal... ")
        country = input("Enter country... ")
        phone = input("Enter phone... ")
        email = input("Enter email... ")
        credit_score = input("Enter credit score... ")

        address = Address(street, city, state, postal, country)
        self.people_list.append(Customer(id, credit_score, name, phone, email, ssn_tin, address))

        self.menu_handler("Customer Menu")

    def manage_customer(self):
        print(f"\nManaging a customer")
        if not self.people_list:
            print(f"No Customers exist. PLease create a Customer...")
            self.menu_handler("Customer Menu")
        else:
            menu = ["List all Customers", "List Accounts", "List Loans", "List Applications", "Update Address", "Return"]

            selection = None
            while selection != 5:
                print('\n')
                for i, v in enumerate(menu):
                    print(f"{i} {v}")

                cust_ids = {}
                for cust in self.people_list:
                    cust_ids[cust.get_id()] = cust

                selection = int(input("Enter selection... "))

                if selection == 0:
                    print('\n')
                    for i, v in enumerate(self.people_list):
                        print(f"{v.get_id()} {v.get_name()}")
                elif selection == 1:
                    selection = input("Enter customer id... ")
                    if selection not in cust_ids.keys():
                        print("That customer does not exist... ")
                    else:
                        print('\n')
                        for i,v in enumerate(cust_ids[selection].get_accounts()):
                            print(v.get_account_number())
                elif selection == 2:
                    pass
                elif selection == 3:
                    pass
                elif selection != 4:
                    pass



            self.menu_handler("Customer Menu")

    def end_program(self):
        quit()


if __name__ == "__main__":
    print(f"Welcome to BankSys")
    driver = Driver()

    driver.menu_handler("Main Menu")

    driver.end_program()
