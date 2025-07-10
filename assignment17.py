import random
def lucky_guess(guess,range_num):
    random_guess = random.randint(1,range_num)
    for attempt in range(1,6):
        if guess==random_guess:
            print("sucess")
            break
        else:
            print("try again")
        guess= int(input("Take another guess"))
lucky_guess(4,50)    
