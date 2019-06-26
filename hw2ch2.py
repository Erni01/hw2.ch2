# 2. N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will each single student get?
# How many apples will remain in the basket? The program reads the numbers N and K.
# It should print the two answers for the questions above. (Each N student will take K apples, and remains X)


def sharing(apples, students):
    remain = apples % students
    proportion = apples // students
    print("Each student will take " + str(proportion) + " apples, and in the basket will remains " + str(remain) + ".")


sharing(11, 3)