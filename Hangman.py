import random
def randword(file):
    filef=open(file, 'r')
    words=filef.readlines()
    n=random.randint(0, len(words))
    return words[n]

guess=0
n=0
word=randword('sowpods.txt').strip().upper()
loc=[' _']*(len(word))
letters=[]
guessword=''.join(loc)
while n<6 and guessword != word:
    print(guessword)
    guess=input('Guess a Letter: ').upper()
    if not guess.isalpha():
        print('Please choose a letter\n')
    elif guess==word:
        guessword=word
    elif len(guess) > 1:
        print('Pick a single letter\n')
    elif guess in letters:
        print('You already guessed this letter!!!\n')
    elif guess in word:
        print('\n')
        letters.append(guess)
        for i in range (0, len(word)):
            if word[i]==guess:
                loc[i]=word[i]
        guessword=''.join(loc)
    else:
        letters.append(guess)
        print('There is no {} in the word!\n'.format(guess))
        n=n+1
        print('You have {} guesses left'.format(6-n))
    letters.sort()
    print('Letters guessed: {}'.format(' '.join(letters)))
    if n==1:
        print('  ______\n  |    |\n  |    o\n  |\n  |\n  |\n__|__\n')
    if n==2:
        print('  ______\n  |    |\n  |    o\n  |    |\n  |\n  |\n__|__\n') 
    if n==3:
        print('  ______\n  |    |\n  |   \\o\n  |    |\n  |\n  |\n__|__\n')
    if n==4:
        print('  ______\n  |    |\n  |   \\o/\n  |    |\n  |\n  |\n__|__\n')
    if n==5:
        print('  ______\n  |    |\n  |   \\o/\n  |    |\n  |   /\n  |\n__|__\n')
    if n==6:
        print('  ______\n  |    |\n  |   \\o/\n  |    |\n  |   / \\\n  |\n__|__\n')
if n==6:
    print('YOU LOSE!!!')
    input('Press enter to see the answer.')
elif word==guessword:
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
print('The word was obviously '+word)
input('Press enter to close.')