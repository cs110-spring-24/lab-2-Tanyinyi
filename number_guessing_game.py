import random
num=random.randint(1,100)
guess_num=0

lower_bound=1
upper_bound=100


while True:
    guess_num=guess_num+1
    user = input(f"Guess a number between {lower_bound} and {upper_bound}): ")
    user=int(user)
    if user<num:
        print("Too low")
        lower_bound=user+1
    elif user>num:
        print("Too high")
        upper_bound=user-1
    else:
        break
      
print(f"You guess {guess_num} to solve it!")


