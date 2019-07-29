UserNum = int(raw_input("Enter Number "))

UserWord = raw_input("Enter Word")
if UserNum == 1:
    print(str(UserNum) + UserWord)
elif UserNum <0:
    print("Nope")
else:
    if UserWord [-3:] == "ife":
        print(UserNum + " " + UserNum[-3:] + "ives")

    elif UserWord [-2:] == "sh" or "ch":
        print(UserWord + "es")

    elif UserWord [-2:] == "us":
        print(UserWord[-1:] + "i")

    elif UserWord[-1:] == "y":
        print(str(UserNum) [:-1] + "ies")


# # '''word = "computerz"
# # print(word[:5])  # prints "compu"
# print(word[:-1])  # prints "computer"
# print(word[4:])  # prints "uterz"
# print(word[-3:])  # prints "erz"
