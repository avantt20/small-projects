from PIL import Image

image1 = Image.open("draft.jpg")
image2 = Image.open("hundred.jpg")
image3 = Image.open("wcoaste.jpg")

print("Welcome to the Canucks quiz!")
playing = input("Do you want to play? (yes or no) ").lower()

if playing != "yes":
    quit()
print("Okay let's play")

def quizgame():
    score = 0

    answer = input("Who is the Canucks leading scorer? (last name only) ")
    if answer.lower() == "sedin":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Sedin")

    answer = input("Who is the current Canucks captain? (last name only) ")
    if answer.lower() == "horvat":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Horvat")
    image1.show()

    answer = input("Who was the Canucks first round draft pick in 2015? (last name only) ")
    if answer.lower() == "boeser":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Boeser")

    answer = input("What year did the Canucks last make the playoffs? ")
    if answer.lower() == "2020":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was 2020? ")

    answer = input("What year did the Canucks play their first ever season? ")
    if answer.lower() == "1970":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was 1970")

    answer = input("Who was the Canucks first ever draft pick? (last name only) ")
    if answer.lower() == "tallon":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Tallon")

    answer = input("What year did the Canucks first make the Stanley Cup Finals? ")
    if answer.lower() == "1982":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was 1982")
    image3.show()

    answer = input("Who played the center position for the West Coast Express line? (last name only) ")
    if answer.lower() == "morrison":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Morrison") 

    answer = input("Who did the Canucks play in the 2013 playoffs? (team name only) ")
    if answer.lower() == "sharks":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Sharks")

    answer = input("Who was the first ever Canuck captain? (last name only) ")
    if answer.lower() == "kurtenbach":
        print("That's right!")
        score += 1
    else:
        print("WRONG! The correct answer was Kurtenbach")

    print("You got " + str(score) + " questions right!")

    percentage = (score / 10) * 100
    print("You got " + str(percentage) + " percent on this quiz")

    if percentage == 100.0:
        image2.show()
        print("Wow good job!")
    elif percentage <= 40.0:
        print("You failed bruh")
    else:
        print("Are you happy with your score?")

quizgame()

keep_playing = input("Do you want to take the quiz again? Y or N: ").lower()

while keep_playing == 'y':
    quizgame()
    keep_playing = input("Do you want to keep playing? Y or N: ").lower()
    if keep_playing == 'n':
        print("You have succesfully quit")