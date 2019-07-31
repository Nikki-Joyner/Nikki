# students = ["Alice", "Javi", "Damien" ] #Considered a list, however in java its called a array - "List of strings"
# students.append("Delilah")  #Considered "push" like in java
# print(students)

# students = ["Alice", "Javi", "Damien" ]
# students.insert(1,"zoey")
# print(students)

'''smith_siblings = ["Emily", "Monique", "Gio", "Alice" , "Javi", "Mike"]
for name in smith_siblings:
    print(name + " Smith")
#[ count = 0
# for name in smith_siblings:
#     count = count + 1
# print(count)]

print(len(smith_siblings))'''



'''smith_siblings = ["Emily", "Monique", "Gio", "Alice" , "Javi", "Mike"]
for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"
print(smith_siblings)'''



# [superheroes = ["Captain Marvel", "Wonder woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
#
# demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5"))
#
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 heroes:", superheroes)
# else:
#     print("Hero not found")]

names = ["Rickson", "Bran", "Arya", "Sansa", "Jon", "Rob"]
#print(names)[::-1]
#print(names)[4:2:-1] #Star:End"Step of what to do
#names =names[::-1]
print(names)[::3] #alternates
