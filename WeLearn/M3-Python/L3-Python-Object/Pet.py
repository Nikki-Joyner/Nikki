'''class Pet(object):

    def __init__(self,name, age):
        self.name = name
        self.age = age

pet_1 = Pet("Tyco", 12)
pet_2 = Pet("Chloe", 7)
pet_3 = Pet("Crush", 3)
pet_4 = Pet("Squirt", 4)

print("My pet %s is %s years old" % (pet_1.name, pet_1.age))
print("My pet %s is %s years old" % (pet_2.name, pet_2.age))
print("My pet %s is %s years old" % (pet_3.name, pet_3.age))
print("My pet %s is %s years old" % (pet_4.name, pet_4.age))'''
# ------
# class Pet(object):
#     def __init__(self, name, age, animal):
#         self.name = name
#         self.age = age
#         self.animal = animal
#         self.is_hungry = False
#         self.mood = "happy"
#
#     def eat(self):
#         print("> %s is eating..." % self.name)
#         if self.is_hungry:
#             self.is_hungry = False
#         else:
#             print("> %s may have eaten too much" % self.name)
#             self.mood = "lethargic"
#
# my_pet = Pet("Fido",3,"dog")
# my_pet.is_hungry = True
# print("Is my pet hungry? %s" % my_pet.is_hungry)
# my_pet.eat()
# print('How about now? %s' % my_pet.is_hungry)
# print("My pet is feelings %s" % my_pet.mood)
# ------
