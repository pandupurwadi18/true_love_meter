# -- True Love Meter --
# Pandu Purwadi
print("Welcome to the True Love Meter! \n This is just for fun")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
lower_name = combine_name.lower()
count_ten = str(lower_name.count("t") + lower_name.count("r") + lower_name.count("u") + lower_name.count("e"))
count_single = str(lower_name.count("l") + lower_name.count("o") + lower_name.count("v") + lower_name.count("e"))

score = count_ten + count_single
score = int(score)

if score < 10 or score > 90 :
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50 :
    print(f"Your score is {score}, you are alright together.")
else :
    print(f"Your score is {score}.")