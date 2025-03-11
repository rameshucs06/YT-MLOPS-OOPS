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
                            5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.singup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
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

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to sign in first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your messge has been sent to {frnd}")
        else:
            print("You need to sign in first to post something...")
        print("\n")
        self.menu()


user1 = chatbook()    