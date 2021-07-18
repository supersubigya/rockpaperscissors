import os #to use the OS structure commands
import gtts #to translate text to speech
import random #for the random integer generator
from playsound import playsound #to play the output sound


#converts text to speech
def text_speech(speech):
    speech_file = gtts.gTTS(speech) #converting text to speech using google text to speech (gTTS)
    speech_file.save("speech.mp3") #saving the audio output recieved from gTTS 

    playsound("speech.mp3") #used to play the saved audio file

    os.remove("speech.mp3") #used in removing the audio file after use


#generates random number to determine computer choice of either rock, paper and scissors
def random_number():
    r_int = random.randint(0, 2)
    if r_int == 0:
        return "rock"
    elif r_int == 1:
        return "paper"
    elif r_int == 2:
        return "scissors"


#checks who wins or weather the game ends on draw
def check_win(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "-- Its a Draw!"
    elif comp_choice == "paper" and user_choice == "rock":
        return "-- Computer wins the game!"
    elif comp_choice == "rock" and user_choice == "scissors":
        return "-- Computer wins the game!"
    elif comp_choice == "scissors" and user_choice == "paper":
        return "-- Computer wins the game!"
    else:
        return "-- User won the game this time!"


#checks if the input entered by user is valid or not
def check_value(user_input):
    valid_tpl = ("rock", "scissors", "paper")
    if user_input.lower() in valid_tpl:
        return True
    else:
        return False


#prints the output according the fulfilled conditions
def output_text(user_choice, comp_choice, result):
    if result == "-- Its a Draw!":
        text_speech(f"You entered {user_choice}. Computer chose {comp_choice}.")
        print("-- Its a Draw!")

    elif result == "-- Computer wins the game!":
        text_speech(f"You entered {user_choice}. Computer chose {comp_choice}.")
        print("-- Computer wins the game!")
    
    else:
        text_speech(f"You entered {user_choice}. Computer chose {comp_choice}.")
        print("-- User won the game this time!")


#counts and stores scores of number of draws, computer wins and user wins
def scores(result, scores_list):
    if result == "-- Its a Draw!":
        scores_list[0] += 1
    elif result == "-- User won the game this time!":
        scores_list[1] += 1
    else:
        scores_list[2] += 1
    return scores_list


#first = draw counts, second = user wins counts and third = computer wins count
scores_list = [0, 0, 0]

print("\n") #line break

flag = True
while flag:
    #executed when the game is started for the first time
    text_speech("Please enter either Rock, Paper or Scissors : ")
    user_choice = input("Please enter either Rock, Paper or Scissors : ")
    user_choice = user_choice.lower()

    check = check_value(user_choice)

    while check is False: #executed when the user input is incorrect
        text_speech("Error! Please input Rock, Paper or Scissors.")
        user_choice = input("Choose either Rock, Paper or Sciccors >>>")
        check = check_value(user_choice)
    
    comp_choice = random_number()
    result = check_win(user_choice, comp_choice)
    output_text(user_choice, comp_choice, result)
    scores_list = scores(result, scores_list)

    print("\n") #line break

    count = input("Do you like to continue? (yes/no) : ") #executed to know if the user wants to continue the game.

    if count.lower() != "yes":
        flag = False


else:
    text_speech("Thank you so much for playing this game!") #executed before final scoreboard is displayed
    
    #final scoreboard displaying draws, user wins and computer wins
    print(f"""\n\t\t----SCOREBOARD----\n
    \t\tNumber of draws : {scores_list[0]}
    \t\tUser Wins : {scores_list[1]}
    \t\tComputer Wins : {scores_list[2]}""")
