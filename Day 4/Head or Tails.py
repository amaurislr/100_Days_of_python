import random

random_head_or_tails = random.randint(a=0, b=1)

if random_head_or_tails == 0:
    print("You get heads")
else:
    print("You get tails")