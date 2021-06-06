class Driver:
    __prompt = f"Enter menu selection: "
    __menus = {
        "main_menu": [
            {"text": "Account Manager", "value": 0},
            {"text": "GL Manager", "value": 1},
            {"text": "Exit", "value": -1},
        ],
        "account_menu": [{"text": "Create New", "value": 2},{"text":"Manage Existing", "value": 3},{"text":"Return...","value": 4}],
        "gl_menu": [],
        "loan_menu": [],
    }
    account_list = []
    people_list = []
    loan_list = []
    applications_list = []

    def __init__(self):
        pass

    def main_menu(self) -> int:
        print(f"Main Menu:")
        print(f"(1) {self.__menus['main_menu'][0]['text']}")
        print(f"(2) {self.__menus['main_menu'][1]['text']}")
        print(f"(3) {self.__menus['main_menu'][2]['text']}")
        return int(input(self.__prompt))

    def account_menu(self) -> int:
        print(f"Account Manager")
        print(f"(1) Create new account")
        print(f"(2) Existing account")
        print(f"(3) Return")
        return int(input(self.__prompt))

    def end_program(self):
        # Do all the clean up and saving of stuff
        quit()


if __name__ == "__main__":
    print(f"Welcome to BankSys")
    driver = Driver()
    selection = driver.main_menu()
    while selection >= 0:
        if selection == -1:
            break
        elif selection == 0:
            selection = driver.account_menu()
        elif selection == 1:
            selection = driver.gl_menu()
        elif selection == 2:
            selection = driver.create_account()
        elif selection == 3:
            selection = driver.manage_existing()
        
        else:
            selection = driver.main_menu()

        

    driver.end_program()
