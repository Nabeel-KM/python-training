class User:
    def __init__(self, email= "", user="", password="", designation=""):
        self.email = email
        self.user = user
        self.password = password
        self.designation = designation

    def change_password(self, new_password):
        self.password = new_password   
    
    def change_designation(self, new_designation):
        self.designation = new_designation

    def get_user_info(self):
        print (f"User: {self.user} works as a {self.designation}. You can contact him at {self.email}")


user_one = User("nabeel@gmail.com","Nabeel", 123456, "DevOps Engineer")
user_one.get_user_info()

user_one.change_designation("Mechanical Engineer")

user_one.get_user_info()
