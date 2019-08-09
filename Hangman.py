import random
import os


def randword(file):
    filef = open(file, 'r')
    words = filef.readlines()
    n = random.randint(0, len(words))
    return words[n]


def winner():
    print('          ¶¶ ¶¶  ¶¶ ¶¶ ')
    print('         ¶¶ ¶¶ ¶¶ ¶¶ ¶¶¶')
    print('     ¶¶¶¶¶            ¶¶¶¶¶¶¶')
    print('   ¶¶¶¶¶               ¶¶¶¶¶¶¶')
    print('  ¶¶¶¶¶                  ¶¶¶¶¶')
    print('  ¶¶¶¶                    ¶¶¶')
    print('   ¶¶                      ¶¶¶')
    print('   ¶                        ¶¶¶¶') 
    print('  ¶¶     ¶¶¶      ¶¶        ¶¶¶¶¶¶¶') 
    print('  ¶     ¶¶¶¶     ¶¶¶¶¶      ¶¶¶¶¶¶ ¶')
    print('  ¶    ¶¶¶¶¶    ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶  ¶')
    print('  ¶¶  ¶¶¶¶¶      ¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶   ¶')
    print('   ¶  ¶¶¶          ¶¶¶¶   ¶¶¶¶¶¶¶¶¶   ¶')
    print('   ¶¶                    ¶¶¶¶¶¶¶¶¶¶   ¶¶¶') 
    print('   ¶¶¶     ¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶')
    print('   ¶¶¶¶¶   ¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶')
    print('   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶')
    print('   ¶¶¶¶¶¶¶¶  ¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶')
    print('    ¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
    print('    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶')
    print('    ¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶')
    print('  ¶¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶')
    print('  ¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶')
    print('   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶')
    print('                   ¶¶¶¶¶¶¶¶¶¶¶')
    print('                   ¶¶¶¶¶¶¶¶¶¶')
    print('YOU WIN!!!')


guess = 0
n = 0
word = randword('sowpods.txt').strip().upper()
loc = [' _'] * (len(word))
letters = []
guessword = ''.join(loc)
while n <= 6:
    letters.sort()
    print(f'You have {6 - n} incorrect attempts remaining.')
    print(f'Letters guessed: {" ".join(letters)}')
    if n == 0:
        print('  ______\n  |    |\n  |\n  |\n  |\n  |\n__|__')
    if n == 1:
        print('  ______\n  |    |\n  |    o\n  |\n  |\n  |\n__|__')
    if n == 2:
        print('  ______\n  |    |\n  |    o\n  |    |\n  |\n  |\n__|__') 
    if n == 3:
        print('  ______\n  |    |\n  |   \\o\n  |    |\n  |\n  |\n__|__')
    if n == 4:
        print('  ______\n  |    |\n  |   \\o/\n  |    |\n  |\n  |\n__|__')
    if n == 5:
        print('  ______\n  |    |\n  |   \\o/\n  |    |\n  |   /\n  |\n__|__')
    if n == 6:
        print('  ______\n  |    |\n  |   \\o/\n  |    |\n  |   / \\\n  |\n__|__')
        print('YOU LOSE!!!')
        break    
    print(guessword)
    guess = input('Guess a Letter: ').upper()
    os.system('cls')
    if not guess.isalpha():
        print('Letters only.')
        n += 1
    elif len(guess) > 1:
        if guess == word:
            guessword = word
        else:
            print('Wrong.')
            n += 1
    elif guess in letters:
        print(f'You already guessed {guess}!!!')
        n += 1
    elif guess in word:
        letters.append(guess)
        for i in range (0, len(word)):
            if word[i] == guess:
                loc[i] = word[i]
        guessword = ''.join(loc)
    else:
        letters.append(guess)
        print(f'There is no {guess} in the word!')
        n += 1
    
    if guessword == word:
        os.system('cls')
        winner()
        break
    
print('The word was obviously ' + word)