import random
cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(cards)
score = 0

while True:
    choice = input('peak the card? y / n \n')
    if choice == 'y':
        card = cards.pop()
        print(f'you get {card}')
        score += card
        if score > 21:
            print('you lose')
            break
        elif score == 21:
            print('you win')
            break
        else:
            print(f'you have {score}')
    elif choice == 'n':
        print(f'your game is over, u have {score}')
        break
