from PIL import Image

image1 = Image.open("learners.jpg")
image2 = Image.open("walk.jpg")
image3 = Image.open("win.jpg")
image4 = Image.open("dead.jpg")

#This is what is displayed if the user enters class for their first choice and drive for their second choice and cereal for their third choice
def fourth_choice_cereal():
    option = input("There is no milk left cause your dad didn't come back. Do you eat cereal RAW or with WATER? ").lower()
    if option == "raw":#now the user can pick to either eat cereal raw or with water
        print("Congrats JiDion would be proud")
        image3.show()
    elif option == "water":
        image4.show()
        print("You died from being gobind :( RIP")
    else:
        print("Invalid option. You Lose")

#This is what is displayed if the user enters class for their first choice and drive for their second choice
def third_choice_drive():
    option = input("You arrive at school and see Mr. Kilpatrick stare at you with a menacing look. Do you say good MORNING or IGNORE him? ").lower()
    if option == "morning":#now the user can pick to either say good morning or ignore
        print("Mr KP says morning back and you have a good rest of your day. Good Job")
        image3.show()
    elif option == "ignore":
        image4.show()
        print("Mr KP is furious. He yells " + name + ", stop wearing your hoodie! and you die from shock. RIP :( ")
    else:
        print("Invalid option. You Lose")

#This is what is displayed if the user enters skip for their first choice and eat for their second choice
def third_choice_eat():
    option = input("There are leftovers  of lasagna in the fridge. Do you eat LASAGNA or CEREAL? ").lower()
    if option == "lasagna":#now the user can pick to either eat lasagna or cereal
        image4.show()
        print("You didn't heat up the food proper. You got salmonella and died :( ")
    elif option == "cereal":
        fourth_choice_cereal()
    else:
        print("Invalid option. You Lose")

#This is what is displayed if the user enters skip for their first choice
def second_choice_skip():
    option = input("You skipped class. Now are you going to SLEEP in or EAT breakfast? ").lower()
    if option == "sleep": #now the user can pick to either eat or sleep
        image4.show()
        print("You had a nightmare and died from shock in your sleep. RIP :( ")
    elif option == "eat":
        third_choice_eat()
    else:
        print("Invalid option. You Lose")

#This is what is displayed if the user enters class for their first choice
def second_choice_class():
    image1.show()
    image2.show()
    option = input("As you're getting ready to go to class, you realize no one can drive you to school. Do you DRIVE with your learners license or WALK for 15 minutes? ").lower()
    if option == "drive": #now the user can pick to either walk or drive to school
        print(" A cop catches you, but let's you off with a warning")
        third_choice_drive() 
    elif option == "walk":
        image4.show()
        print(" A reckless driver ran you over on the sidewalk. You died :( ")
    else:
        print("Invalid option. You lose")

# this is the first option the user gets to pick. If they choose skip the code goes to the function second_choice_skip and if they choose 
def first_choice():
    option = input("You wake up late, and you are now 5 minutes late for school. Do you SKIP or go to CLASS? ").lower()
    if option == "skip":
        second_choice_skip()
    elif option == "class":
        second_choice_class()
    else:
        print("Invalid option. You Lose")

name = input("Enter your name to begin: ") #this is the first thing you see when you click run. It asks user for their name

check = name.isalpha()
if check == True:
    print("Instructions: Pick one of the two options listed in the question above. Input one of the words written in ALL CAPS")
    answer = input("Welcome " + name + ". A dangerous journey lies ahead of you, do you wish to proceed? (Y) or (N) ").lower()
    if answer == "y":
        first_choice()
    else:
        print("You have successfully quit") #this code allows the user to decide if they want to go on an adventure or not.
elif check != True:
    print("Invalid name input. Your name cannot contain numbers. Click run and try again")