class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I am ",self.name)

class VipUser(User):
    def __init__(self,name,age,balance):
        super().__init__(name,age)
        self.balance = balance
    def show_money(self):
        print("Balance:")

class Guest:
    def say_hello(self):
        print("Goodnight.") 

# g = [User("Minh",21),Guest()]
# for u in g:
#     u.say_hello()




