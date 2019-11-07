# ask for age
age = input("How old are you? \n")
if age != "":
    age = int(age)
    if age >= 18 and age <21:
        print("You can enter, but need a wristband")
    elif age >= 21:
        print("you are good to enter and you can drink")
    else:
        print("you can't come in, little one :(")
else:
    print("please enter an age")

# 18-21 wristband
#21+ drink, normal entry
#too young sorry
