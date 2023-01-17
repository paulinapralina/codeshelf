import random
bomb = (2, 5, 8)
safe = (1, 3, 4, 6, 7)
def main():
    win = 0
    if win == 4:
        print('(win)')

print('Zagrajmy w sapera! Wybieraj numery pol od 1 do 9. Uwazaj na bomby!')
def Saper():
    lives = 3
    win = 0
    while win < 4 and lives > 0:
        question = 'Na ktorym polu staniesz?'
        guess = int(input(question))
        if guess in bomb:
            lives -= 1
            print('boooom! Tracisz zycie, zostalo', lives, 'zyc')
        elif guess > 10 or guess == 0 or guess < 0:
            print('wypadles poza plansze!')
            Saper()
        else:
            print('dobrze! jestes na polu',guess)
            win = win + 1
            print('masz', win, 'punktow!')
    else:
        print('Koniec!')
Saper()

