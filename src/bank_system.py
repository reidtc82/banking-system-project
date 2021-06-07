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

    def manage_gl(self):
        print(f"\nManaging a GL")
        if not self.gl_list:
            print(f"No GLs exist. Please create a GL...")
            self.menu_handler("GL Menu")
        else:
            pass

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

    def manage_customer(self):
        print(f"\nManaging a customer")
        if not self.people_list:
            print(f"No Customers exist. PLease create a Customer...")
            self.menu_handler("Customer Menu")
        else:
            pass

    def end_program(self):
        quit()


if __name__ == "__main__":
    print(f"Welcome to BankSys")
    driver = Driver()

    driver.menu_handler("Main Menu")

    driver.end_program()
