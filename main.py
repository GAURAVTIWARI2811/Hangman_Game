if __name__ == "__main__":
    import random
    from hangmanwords import word
    from hangmanart import stages, logo
    choosen = random.choice(word)
    lives = 7
    const  = len(stages)
    print(logo)
    x = []
    end_of_game = False
    for i in range(len(choosen)):
        x += "-"
    while end_of_game is not True:
        guess = input("Guess a letter : ")
        for i in range(len(choosen)):
            if guess == choosen[i]:
                x[i] = guess

        if guess not in choosen:
            print("You Guessed Wrong \n")
            lives -= 1
            print(stages[lives])
            if lives ==0:
                end_of_game = True
                print("GAME OVER \n")
                print("Right Word was {}".format(choosen).upper())

        print("".join(x))

        if "-" not in x:
            print("You Win")








