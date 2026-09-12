# class Theaters:
#     def __init__(self, theater_name, price, tickets_available, address):
#         self.theater_name = theater_name
#         self.movies_available = []
#         self.price = price
#         self.tickets_available = tickets_available
#         self.address = address

#     def TheaterFullDetails(self):
#         theater_data = {
#             "theater_name": self.theater_name,
#             "movies_available": self.movies_available,
#             "price": self.price,
#             "tickets_available": self.tickets_available,
#             "address": self.address,
#         }
#         return theater_data

#     def add(self, *movies_data):
#         self.movies_available.extend(movies_data)

#     def remove(self, movies_data):
#         if movies_data in self.movies_available:
#             self.movies_available.remove(movies_data)
#         else:
#             return f"For {movies_data} Tickets is not Available!!"

#     def __len__(self):
#         return self.tickets_available

#     def __str__(self):
#         return f"{self.theater_name} Have {self.tickets_available} Tickets Avaliable!"

#     # Comparision Method
#     def __gt__(self, other):
#         return self.tickets_available > other.tickets_available

#     def __iter__(self):
#         try:
#             data_loop = [f"{key}: {value}" for key,
#                          value in self.TheaterFullDetails().items()]
#             for item in data_loop:
#                 yield item
#         except NameError as e:
#             print("Logic Error Inside The Iterator: ", e)

#     # Helper function to make an object like a function
#     def __call__(self):
#         try:
#             raise TypeError("Objects are not naturally executable functions.")
#         except Exception as e:
#             print(
#                 f"Logic Error : You Can't Call {self.theater_name} as a function() => {e}")
#         return str(f'Program Executed..!!')

#         # Getting an key from the movies-data using magic-method / dunder method
#     def __getitem__(self, key):
#         match key:
#             case "theater_name":
#                 return self.theater_name
#             case "movies_available":
#                 return self.movies_available
#             case "price":
#                 return self.price
#             case "tickets_available":
#                 return self.tickets_available
#             case "address":
#                 return self.address
#     # checking a key exist in from the Theaters object data using magic-method / dunder method

#     def __contains__(self, item):
#         match (item in self.TheaterFullDetails(), item in self.movies_available, item == self.theater_name):
#             case (True, _, _):
#                 return True
#             case (_, True, _):
#                 return True
#             case (_, _, True):
#                 return True
#             case _:
#                 return False


# def create_theater():
#     theater_name = input("Enter theater name: ")
#     price = int(input("Enter ticket price: "))
#     tickets_available = int(input("Enter tickets available: "))
#     address = input("Enter address: ")

#     movies = [
#         movie.strip()
#         for movie in input("Enter movies separated by commas: ").split(",")
#     ]

#     theater = Theaters(
#         theater_name,
#         price,
#         tickets_available,
#         address
#     )

#     theater.add(*movies)

#     return theater


# # --------DISPLAYING OUTPUT----------#
# theater_1 = create_theater()
# print("\n" + "=" * 40)
# print("THEATER 1 DETAILS")
# print("=" * 40)

# for item in theater_1:
#     print(item)

# # print("\n" + "=" * 40)
# # print("THEATER 2 DETAILS")
# # print("=" * 40)

# # theater_2 = create_theater()

# # for item in theater_2:
# #     print(item)

# # print("-" * 30)

# # print(*theater_1, sep="\n")
# # # print("-" * 24)
# # # print(str(theater_1))
# # print("-" * 30)
# # print(*theater_2, sep="\n")
# # # print("-" * 24)
# # # print(str(theater_2))
# # print("-" * 30)

# user_input = input("Enter an attribute?")

# getattr(theater_1, user_input)

# for attr in dir(theater_1):
#     if not attr.startswith("__") and not callable(getattr(theater_1, attr)):
#         value = getattr(theater_1, value)
#         print(f"{attr}: {value}")
