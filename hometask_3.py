from random import randint

def win():
    count = 0

    while True:
        kub1 = randint(1, 6)
        kub2 = randint(1, 6)
        combo = kub1 + kub2
        count = count + 1
        if combo == 8:
            print(kub1, kub2, count)
            break

win()
