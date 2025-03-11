class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()



    def menu(self):
        user_input = input("""Welcom to chatbook !! How would you like to proceed?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit""")
        if user_input == "1":
            self.singup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


    def singup(self):
        email = input("enter your email here -> ")
        pwd = input("enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up succesfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("You  have signed in succesfully !!")
                self.loggedin = True
            else:
                print("Please input correct credential..")
        print("\n")
        self.menu()

obj = chatbook()    