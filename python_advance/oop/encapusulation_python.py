# class Bank_Account:
#     def __init__(self, name, balance, withdraw, deposit):
#         self.name = name,
#         self.withdraw = withdraw,
#         self.deposit = deposit,

#     def get_amount(self):
#         print(f"You're total balance is {self.__balance}")

#     def withdraw_amount(self):
#         print("your withdraw amount is {self.withdraw}")

#     def deposit_amount(self):
#         print(f"You're Total deposit is {self.deposit}")


# class Acc_holder(Bank_Account):
#     def __str__(self):
#         print(f"{self.greet_user} You're total balance is {self.__balance} And your withdraw amount is {self.withdraw_amount} and you deposit total i s {self.deposit_amount}")

#     def greet_user(self):
#         print("Welcome {self.name} To HDFC Bank Have a nice day.")


# acc_holder1 = Acc_holder("kumar", 500, 200, 400)

# acc_holder1.withdraw_amount()


# class Resturant:

#     def __init__(self, name, resturant_name, address, role, shift, work):
#         self.name = name
#         self.resturant_name = resturant_name
#         self.address = address
#         self.role = role
#         self.shift = shift
#         self.work = work

#     def greet_user(self):
#         print(
#             f"Hello {self.name}, Welcome to {self.resturant_name} Feel Free to contact {self.address} if any quaries")


# class Staff(Resturant):

#     def start_work(self):
#         print(f"{self.name} you're role is {self.role} so start working on {self.work} and from tomorrow onwards you got {self.shift} shift")


# class Waiter(Staff):

#     def introduction(self):
#         self.greet_user()
#         print("We are happy to see you onboard..")
#         self.start_work()


# class Cheif(Staff):
#     def introduction(self):
#         self.greet_user()
#         self.start_work()


# waiter = Waiter(
#     "Samuel",
#     "Kumar's Hub",
#     "richard's street california, USA",
#     "waiter",
#     "Morning",
#     "Clean"
# )
# cheif = Cheif(
#     "Ravi",
#     "Kumar's Hub",
#     "richard's street california, USA",
#     "Cheif",
#     "Morning",
#     "Cooking"
# )

# # waiter.introduction()

# cheif.introduction()


# @PROPERTY IN PYTHON

# class Employee:
#     def __init__(self, name, level):
#         self._name = name
#         self._level = level

#     def __str__(self):
#         return f'{self._name}: {self._level}'

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name: str):
#         if not isinstance(new_name, str) or not new_name.strip():
#             raise ValueError("Name must be a non-empty string!")
#         self._name = new_name

#     @property
#     def level(self):
#         return self._level


# charlie_brown = Employee('Charlie Brown', 'trainee')
# print(f"before: {charlie_brown}")

# try:
#     charlie_brown.name = "kumar"
# except AttributeError as e:
#     print(f"Error: {e}")


# print(f"After: {charlie_brown}")
# print(charlie_brown.level)


class GameCharacter:

    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):

        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self, levels=2):
        self._level += levels
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")

    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self.health}\nMana: {self.mana}\n"


hero = GameCharacter('Kumar Nallana')  # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up

hero.level_up()
