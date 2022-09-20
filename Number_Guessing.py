import random
number = random.randint(1, 10)

def guess():
    while True:
        try:
            guess = int(input('please enter an integer value between 0-10: '))
            if guess > 10:
                continue
            else:
                break

        except ValueError:
            continue
    return guess

print(number)

n = 0
while(n < 2):
    estm = guess()
    n+=1


    if estm > number:
        print('Go down')
                


    if estm < number:
        print('Go up')
        

    if number == estm:
        break

if number == estm:
    print('Congratulation')

if number != estm:
    estm = guess()
    if number == estm:
        print('Congratulation')
    else:
        print('Game Over')
        print(f'The number was {number}')











