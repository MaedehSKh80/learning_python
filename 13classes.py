# # class Point:
# #     def __init__(self, x , y) :
# #         self.x=x
# #         self.y=y

# #     def mov(self):
# #         print('move')

# #     def draw (self):
# #         print('draw')
# # Point = Point (40,20) 
# # print (Point.x)


# ---------------------------------------

# class Person:
#     def __init__(self, name) :
#         self.name = name

#     def talk(self):
#         print(f"hello, I'm {self.name}")

# john = Person("John smith")
# john.talk()

# Bob = Person("Bob smith")
# Bob.talk()


# ---------------------------------------



# class Point:
#     def __init__(self, x , y) :
#         self.x=x
#         self.y=y

#     def mov(self):
#         print('move')

#     def draw (self):
#         print('draw')
# Point = Point (40,20) 
# print (Point.x)


# ---------------------------------------



class Mammal:
    def __init__(self, name) :
        self.name = name

    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat (Mammal):
    pass


