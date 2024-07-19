import re

class User:
    def __init__(self, name="", identifier="", email="", password=""):
        self.name = name
        self.identifier = identifier
        self.email = email
        self.password = password

    def set_name(self):
        self.name = input("Enter the user name: ")

    def set_identifier(self):
        self.identifier = input("Enter the identifier: ")

    def set_email(self):
        self.email = input("Enter the Email: ")

    def set_password(self):
        self.password = input("Enter the password: ")

    def set_values(self, name, identifier, email, password):
        self.name = name
        self.identifier = identifier
        self.email = email
        self.password = password

    def get_values(self):
        print(f"The name of user is: {self.name}")
        print(f"The identifier of user is: {self.identifier}")
        print(f"The email of user is: {self.email}")

    def is_password_valid(self):
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return bool(re.match(pattern, self.password))

    def get_name(self):
        return self.name

    def get_identifier(self):
        return self.identifier

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password


class Authenticator:
    def __init__(self):
        self.capacity = 20
        self.users = [User()] * self.capacity
        self.users[0] = self.add_admin()
        self.user_count = 1
        self.deleted_user_count = 0
        self.deleted_users = [User()] * self.capacity

    def add_admin(self):
        admin = User()
        admin.set_values("Admin", "admin", "admin@systems.com", "Admin@123")
        return admin

    def is_identifier_unique(self, user):
        for i in range(self.user_count):
            if self.users[i].identifier == user.identifier:
                return False
        return True

    def validate_signup(self, user):
        if not self.is_identifier_unique(user):
            print("The identifier is already taken. Kindly select another identifier.")
            return False
        if not user.is_password_valid():
            print("The password is too weak. Enter a strong password.")
            return False
        return True

    def signup(self):
        if self.user_count == self.capacity:
            self.resize_users_array()

        user = User()
        user.set_name()
        user.set_identifier()
        user.set_email()
        user.set_password()

        if not self.validate_signup(user):
            return User()

        self.users[self.user_count] = user
        self.user_count += 1
        print("Sign-up/New User added Successfully")
        print()
        return user

    def login(self):
        user = User()
        user.set_identifier()
        user.set_password()

        for i in range(self.user_count):
            if self.users[i].get_identifier() == user.identifier and self.users[i].get_password() == user.password:
                print("Login Successful.....")
                if self.users[i].get_identifier() == "admin":
                    self.admin_menu()
                else:
                    self.user_menu(user)
                return True

        print("Invalid Credentials. Please try again.")
        print()
        return False

    def main_menu(self):
        to_continue = True

        while to_continue:
            print("#####################################################")
            print("\t\tUser Authentication System")
            print("#####################################################")
            print()
            print("Welcome. Please select the correct option: ")
            print("1 - Sign Up.")
            print("2 - Login.")
            print("3 - Exit.")
            choice = int(input("Select the correct option: "))

            if choice == 1:
                user = self.signup()
                if user.identifier:
                    self.user_menu(user)
            elif choice == 2:
                self.login()
            elif choice == 3:
                print("Thanks for using. Now Exiting")
                to_continue = False
            else:
                print("Invalid choice. Please try again.")

    def logout(self, user):
        user = User()
        print("Successfully Logged Out")

    def unsubscribe(self, user):
        if self.deleted_user_count == self.capacity:
            self.resize_deleted_users_array()

        for i in range(self.user_count):
            if self.users[i].get_identifier() == user.get_identifier():
                for j in range(i, self.user_count - 1):
                    self.users[j] = self.users[j + 1]
                self.user_count -= 1
                user.get_values()
                self.deleted_users[self.deleted_user_count] = user
                self.deleted_user_count += 1
                print("Unsubscribed/Deleted Successfully")
                return

        print("User not found.")

    def delete_user(self):
        user = User()
        user = self.find_user()
        self.unsubscribe(user)

    def find_user(self):
        user = User()
        user.set_identifier()

        for i in range(self.user_count):
            if self.users[i].get_identifier() == user.get_identifier():
                return self.users[i]

        print("User not found.")
        return User()

    def change_password(self, user):
        new_password = input("Enter new password: ")
        user.password = new_password
        index = self.find_index(user)
        if index >= 0:
            self.users[index] = user
        print("Password changed successfully.")

    def find_index(self, user):
        for i in range(self.user_count):
            if self.users[i].get_identifier() == user.get_identifier():
                return i
        print("User not found.")
        return -1

    def change_email(self, user):
        new_email = input("Enter new email: ")
        user.email = new_email
        index = self.find_index(user)
        if index >= 0:
            self.users[index] = user
        print("Email changed successfully.")

    def display_all_users(self):
        for i in range(1, self.user_count):
            print("__________________________________________________________")
            print(f"User {i} Details:")
            self.users[i].get_values()
            print("__________________________________________________________")

    def display_deleted_users(self):
        for i in range(self.deleted_user_count):
            print("______________________________________________________________")
            print(f"Deleted User {i + 1} Details:")
            self.deleted_users[i].get_values()
            print("_______________________________________________________________")

    def user_menu(self, user):
        to_quit = True

        while to_quit:
            print()
            print("###################################################")
            print("\t\tUser Menu")
            print("###################################################")
            print()
            print("1 - Change Email")
            print("2 - Change Password")
            print("3 - Logout")
            print("4 - Unsubscribe")
            user_choice = int(input("Please select an option: "))

            if user_choice == 1:
                self.change_email(user)
            elif user_choice == 2:
                self.change_password(user)
            elif user_choice == 3:
                self.logout(user)
                to_quit = False
            elif user_choice == 4:
                self.unsubscribe(user)
                to_quit = False
            else:
                print("Invalid choice. Please try again.")

    def admin_menu(self):
        to_quit = True

        while to_quit:
            print()
            print("###################################################")
            print("\t\tAdmin Options:")
            print("###################################################")
            print()
            print("1. Add a user")
            print("2. Delete a user")
            print("3. Change the password of a given user")
            print("4. Change email of a given user")
            print("5. Display user records")
            print("6. Display deleted user records")
            print("7. Logout")
            admin_choice = int(input("Select an option: "))

            if admin_choice == 1:
                self.signup()
            elif admin_choice == 2:
                self.delete_user()
            elif admin_choice == 3:
                user = self.find_user()
                if user.get_identifier():
                    self.change_password(user)
                else:
                    print("Invalid Identifier")
            elif admin_choice == 4:
                user = self.find_user()
                if user.get_identifier():
                    self.change_email(user)
                else:
                    print("Invalid Identifier")
            elif admin_choice == 5:
                self.display_all_users()
            elif admin_choice == 6:
                self.display_deleted_users()
            elif admin_choice == 7:
                user = User()
                self.logout(user)
                to_quit = False
            else:
                print("Invalid choice. Please try again.")

    def resize_users_array(self):
        new_capacity = self.capacity * 2
        new_users = [User()] * new_capacity
        for i in range(self.user_count):
            new_users[i] = self.users[i]
        self.users = new_users
        self.capacity = new_capacity

    def resize_deleted_users_array(self):
        new_capacity = self.capacity * 2
        new_deleted_users = [User()] * new_capacity
        for i in range(self.deleted_user_count):
            new_deleted_users[i] = self.deleted_users[i]
        self.deleted_users = new_deleted_users
        self.capacity = new_capacity


if __name__ == "__main__":
    authenticator = Authenticator()
    authenticator.main_menu()
