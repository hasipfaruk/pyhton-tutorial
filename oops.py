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
#         self.__balance=0
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




# class Atm:
#     # Constructor
#     def __init__(self):
#         self.pin = ""
#         self.balance = 0
#         self.menu()

#     def menu(self):
#         user_input = input("""
#         Hello, How can I help you?
#         1. Press 1 to create pin
#         2. Press 2 to deposit
#         3. Press 3 to withdraw
#         4. Press 4 to check balance
#         5. Press 5 to exit
#         """)

#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdraw()
#         elif user_input == "4":
#             self.check_balance()  # Renamed method
#         elif user_input == "5":
#             exit()  # Fixed exit call
#         else:
#             print("Invalid option! Please try again.")
#             self.menu()

#     def create_pin(self):
#         self.pin = input("Enter your pin: ")
#         print("Your pin is created successfully")
#         self.menu()

#     def deposit(self):
#         entered_pin = input("Enter your pin: ")
#         if entered_pin == self.pin:
#             amount = int(input("Enter the amount you want to deposit: "))
#             self.balance += amount
#             print("Amount deposited successfully")
#         else:
#             print("Incorrect PIN! Access denied.")
#         self.menu()

#     def withdraw(self):
#         entered_pin = input("Enter your pin: ")
#         if entered_pin == self.pin:
#             amount = int(input("Enter the amount you want to withdraw: "))
#             if amount > self.balance:
#                 print("Insufficient balance")
#             else:
#                 self.balance -= amount
#                 print("Amount withdrawn successfully")
#         else:
#             print("Incorrect PIN! Access denied.")
#         self.menu()

#     def check_balance(self):
#         entered_pin = input("Enter your pin: ")
#         if entered_pin == self.pin:
#             print(f"Your balance is {self.balance}")
#         else:
#             print("Incorrect PIN! Access denied.")
#         self.menu()


# # Creating ATM object
# obj = Atm()



# class SoftwareEngineeringDept:
#     def __init__(self):
#         self.student= ""
#         self.menu()


#     def menu(self):
#         userinput= input("""
#                         Welcome to the software Engineering department:
#                         please select an option for further process:
#                             1.Register a student
#                             2.view student's data
#                             3.Update student details
#                             4.Delete student record
#                             5.Exit.""")
#         if userinput== "1":
#             self.register_stu()
#         elif userinput== "2":
#             self.view_stu()
#         elif userinput== "3":
#             self.update_stu()
#         elif userinput=="4":
#             self.del_stu()
#         elif userinput=="5":
#             print('thank you! Exiting.....')
#         else: 
#             print("Alert: invalid option,please select the valid option.")
#         self.menu()


#     def register_stu(self):
#         stu_id=input("Enter student id: ")
#         if stu_id  in self.students:
#             print("Student already exsists:")
#         else:
#             name=input("Enter student name: ")
#             year=input("Enter year of study: ")
#             print("Student Registered successfully! ")
#             self.menu()

#     def view_stu(self):
#         stu_id=input("Enter Student id: ")
#         if stu_id in self.students:
#             print("student details: ")
#         self.menu()

#     def update_stu(self):
#         stu_id=input("Enter Student id yiu want to update:")
#         if stu_id in self.students:
#             name=input("Enter new name: ")
#             year=input("Enter new year")
#             print("Student daetails updated successfully! ")
#             self.menu()

#     def del_stu(self):   
#         stu_id=input("Enter Student id yiu want to delete: ")
#         if stu_id in self.students:
#             del self.students[stu_id]
#             print("Student Record deleted successfully!")
#         else:
#             print("Id didn't find: ")
#             self.menu()

# obj=SoftwareEngineeringDept()





# Test Code is here
# class SoftwareEngineeringDept:
#     def __init__(self):
#         self.students = {}  # Dictionary to store student records
#         self.menu()

#     def menu(self):
#         userinput = input("""
#         Welcome to the Software Engineering Department:
#         Please select an option for further process:
#         1. Register a student
#         2. View student's data
#         3. Update student details
#         4. Delete student record
#         5. Exit
#         Select an option: """).strip()

#         if userinput == "1":
#             self.register_stu()
#         elif userinput == "2":
#             self.view_stu()
#         elif userinput == "3":
#             self.update_stu()
#         elif userinput == "4":
#             self.del_stu()
#         elif userinput == "5":
#             print("Thank you! Exiting...")
#             exit()
#         else:
#             print("⚠ Alert: Invalid option, please select a valid option.")

#         self.menu()  # Keep displaying the menu until the user exits

#     def register_stu(self):
#         stu_id = input("Enter student ID: ").strip()
#         if stu_id in self.students:
#             print("⚠ Student already exists!")
#         else:
#             name = input("Enter student name: ").strip()
#             year = input("Enter year of study: ").strip()
#             self.students[stu_id] = {"name": name, "year": year}
#             print("✅ Student registered successfully!")
#         self.menu()

#     def view_stu(self):
#         stu_id = input("Enter student ID: ").strip()
#         if stu_id in self.students:
#             print("📄 Student Details:")
#             print(f"ID: {stu_id}, Name: {self.students[stu_id]['name']}, Year: {self.students[stu_id]['year']}")
#         else:
#             print("⚠ Student ID not found!")
#         self.menu()

#     def update_stu(self):
#         stu_id = input("Enter the student ID you want to update: ").strip()
#         if stu_id in self.students:
#             name = input("Enter new name: ").strip()
#             year = input("Enter new year of study: ").strip()
#             self.students[stu_id] = {"name": name, "year": year}
#             print("✅ Student details updated successfully!")
#         else:
#             print("⚠ Student ID not found!")
#         self.menu()

#     def del_stu(self):
#         stu_id = input("Enter the student ID you want to delete: ").strip()
#         if stu_id in self.students:
#             del self.students[stu_id]
#             print("✅ Student record deleted successfully!")
#         else:
#             print("⚠ Student ID not found!")
#         self.menu()


# # Create an instance of the class
# obj = SoftwareEngineeringDept()




# Encapsulation

# class Atm:
#     # Constructor
#     def __init__(self):
#         self.pin = "" # Public attribute
#         self.__balance = 0 # Private attribute
#         self.menu() # Call menu method
#     # setter
#     def set_balance(self, balance):
#         self.__balance = balance
#         if self.__balance == int:
#             print("Balance set successfully!")
#         else:
#             print("Invalid balance!")
#     def get_balance(self):
#         return self.__balance

#     def menu(self):
#         user_input = input("""
#         Hello, How can I help you?
#         1. Press 1 to create pin
#         2. Press 2 to deposit
#         3. Press 3 to withdraw
#         4. Press 4 to check balance
#         5. Press 5 to exit
#         """)

#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdraw()
#         elif user_input == "4":
#             self.check_balance()  # Renamed method
#         elif user_input == "5":
#             exit()  # Fixed exit call
#         else:
#             print("Invalid option! Please try again.")
#             self.menu()

#     def create_pin(self):
#         self.pin = input("Enter your pin: ")
#         print("Your pin is created successfully")
#         self.menu()

#     def deposit(self):
#         entered_pin = input("Enter your pin: ")
#         if entered_pin == self.pin:
#             amount = int(input("Enter the amount you want to deposit: "))
#             self.__balance += amount
#             print("Amount deposited successfully")
#         else:
#             print("Incorrect PIN! Access denied.")
#         self.menu()

#     def withdraw(self):
#         entered_pin = input("Enter your pin: ")
#         if entered_pin == self.pin:
#             amount = int(input("Enter the amount you want to withdraw: "))
#             if amount > self.__balance:
#                 print("Insufficient balance")
#             else:
#                 self.__balance -= amount
#                 print("Amount withdrawn successfully")
#         else:
#             print("Incorrect PIN! Access denied.")
#         self.menu()

#     def check_balance(self):
#         entered_pin = input("Enter your pin: ")
#         if entered_pin == self.pin:
#             print(f"Your balance is {self.__balance}")
#         else:
#             print("Incorrect PIN! Access denied.")
#         self.menu()


# Creating ATM object
# obj = Atm()

# obj=Atm()





# Question 1 
# Create a Python program that lets a user play Rock-Paper-Scissors against the computer.

# Use random.choice(["rock", "paper", "scissors"]) to pick the computer’s move.

# Compare moves and display the result.


# Question 2
# Create a ShoppingCart class with:

# Attributes: A dictionary to store items and their prices.

# Methods:

# add_item(item, price): Adds an item.

# remove_item(item): Removes an item.

# view_cart(): Displays the cart with total price.



# import random

# choices = ["rock", "paper", "scissors"]

# def get_winner(user, computer):
#     if user == computer:
#         return "It's a tie!"
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     print("Welcome to Rock-Paper-Scissors!")
#     user_choice = input("Enter rock, paper, or scissors: ").lower()

#     if user_choice not in choices:
#         print("Invalid choice! Please enter rock, paper, or scissors.")
#         return play_game()  

#     computer_choice = random.choice(choices)
    
#     print(f"Computer chose: {computer_choice}")

#     result = get_winner(user_choice, computer_choice)
#     print(result)

# # Run the game
# play_game()



import random 
choices=["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter rock, paper, or scissors: ").lower()
if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
else:
        print(f"Computer chose: {computer_choice}")
        # print(get_winner(user_choice, computer_choice))





# 2nd Question

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        """Add an item to the cart."""
        if item in self.cart:
            self.cart[item] += price  # Update price if item already exists
        else:
            self.cart[item] = price
        print(f"{item} added to cart.")

    def remove_item(self, item):
        """Remove an item from the cart."""
        if item in self.cart:
            del self.cart[item]
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    def view_cart(self):
        """Display the cart items and total price."""
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = sum(self.cart.values())
            print("\nShopping Cart:")
            for item, price in self.cart.items():
                print(f"- {item}: ${price:.2f}")
            print(f"Total Price: ${total:.2f}\n")


cart = ShoppingCart()
cart.add_item("Laptop", 1200)
cart.add_item("Headphones", 150)
cart.view_cart()
cart.remove_item("Laptop")
cart.view_cart()
