import random
playing= True
while (playing):
    secret_number = random. randint(1,25)
    guess_number = int(input("Guess a number: "))
    if (secret_number == guess_number):
        print("I... I can't believe it, your parents were  wrong. Your not a mistake!!!")
    else:
        print("Your parents were right to put you in my basment.")
    play_again = input("Do you want want to stay in my basment, and be my slave?: ")
    if (play_again== "no"):
        playing= True
    else:
        playing = False