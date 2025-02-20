# nterms = int(input("How many Fibonacci Valus? "))
# # first two terms
# # n1, n2 = 0, 1
# n1=0
# n2=1
# count = 0
# # check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#     print("Fibonacci sequence upto",nterms,":")
#     print(n1)
# # generate fibonacci sequence
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#  # update values
#         n1 = n2
#         n2 = nth
#         count += 1




# num = int(input("Enter a number: "))
# # Calculate the number of digits in num
# num_str = str(num)
# num_digits = len(num_str)
# # Initialize variables
# sum_of_powers = 0
# temp_num = num
# # Calculate the sum of digits raised to the power of num_digits
# while temp_num > 0:
#     digit = temp_num % 10
#     sum_of_powers += digit ** num_digits
#     temp_num //= 10
# # Check if it's an Armstrong number
# if sum_of_powers == num:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

# import math

# OOPS
# class and object

# class Atm:
#     # Constructor
#     def __init__(self):
#         self.pin=""
#         self.balance=0
#         self.menu()
#     def menu(self):
#         user_input=input("""
#         Hello, How can I help you?
#         1. Press 1 to create pin
#         2. Press 2 to deposit
#         3. Press 3 to withdraw
#         4. Press 4 to balance
#         5. Press 5 to exit
#         """)
#         if user_input=="1":
#             self.create_pin()
#         elif user_input=="2":
#             self.deposit()
#         elif user_input=="3":
#             self.withdraw()
#         elif user_input=="4":
#             self.balance()
#         elif user_input=="5":
#             exit

#     def create_pin(self):
#         self.pin=input("Enter your pin: ")
#         print("Your pin is created successfully")
#         self.menu()
#     def deposit(self):
#         amount=int(input("Enter the amount you want to deposit: "))
#         self.balance+=amount
#         print("Amount deposited successfully")
#         self.menu()
#     def withdraw(self):
#         amount=int(input("Enter the amount you want to withdraw: "))
#         if amount>self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             print("Amount withdrawn successfully")
#         self.menu()
#     def Check_balance(self):
#         print(f"Your balance is {self.balance}")
#         self.menu()

# obj=Atm()




class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello, How can I help you?
        1. Press 1 to create pin
        2. Press 2 to deposit
        3. Press 3 to withdraw
        4. Press 4 to check balance
        5. Press 5 to exit
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()  # Renamed method
        elif user_input == "5":
            exit()  # Fixed exit call
        else:
            print("Invalid option! Please try again.")
            self.menu()

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Your pin is created successfully")
        self.menu()

    def deposit(self):
        entered_pin = input("Enter your pin: ")
        if entered_pin == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Incorrect PIN! Access denied.")
        self.menu()

    def withdraw(self):
        entered_pin = input("Enter your pin: ")
        if entered_pin == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print("Amount withdrawn successfully")
        else:
            print("Incorrect PIN! Access denied.")
        self.menu()

    def check_balance(self):
        entered_pin = input("Enter your pin: ")
        if entered_pin == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Incorrect PIN! Access denied.")
        self.menu()


# Creating ATM object
obj = Atm()
