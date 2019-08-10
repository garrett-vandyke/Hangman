import curses
import random
import time
import os


mylines = {0:['  ______','  |    |','  |','  |','  |','  |','__|__'],
           1:['  ______','  |    |','  |    o','  |','  |','  |','__|__'],
           2:['  ______','  |    |','  |    o','  |    |','  |','  |','__|__'],
           3:['  ______','  |    |','  |   \\o','  |    |','  |','  |','__|__'],
           4:['  ______','  |    |','  |   \\o/','  |    |','  |','  |','__|__'],
           5:['  ______','  |    |','  |   \\o/','  |    |','  |   /','  |','__|__'],
           6:['  ______','  |    |','  |   \\o/','  |    |','  |   / \\','  |','__|__']}


def randword(file):
    filef = open(file, 'r')
    words = filef.readlines()
    n = random.randint(0, len(words))
    return words[n]


def winner(stdscr,yy,xx):
    winstr = 'YOU WON!!!'
    for i in range(len(winstr)):
        stdscr.addstr(yy,xx+i,winstr[i])
        stdscr.refresh()
        time.sleep(0.5)
    time.sleep(2)
    stdscr.clear()
    stdscr.addstr(0,xx,'          ¶¶ ¶¶  ¶¶ ¶¶ ')
    stdscr.addstr(1,xx,'         ¶¶ ¶¶ ¶¶ ¶¶ ¶¶¶')
    stdscr.addstr(2,xx,'     ¶¶¶¶¶            ¶¶¶¶¶¶¶')
    stdscr.addstr(3,xx,'   ¶¶¶¶¶               ¶¶¶¶¶¶¶')
    stdscr.addstr(4,xx,'  ¶¶¶¶¶                  ¶¶¶¶¶')
    stdscr.addstr(5,xx,'  ¶¶¶¶                    ¶¶¶')
    stdscr.addstr(6,xx,'   ¶¶                      ¶¶¶')
    stdscr.addstr(7,xx,'   ¶                        ¶¶¶¶') 
    stdscr.addstr(8,xx,'  ¶¶     ¶¶¶      ¶¶        ¶¶¶¶¶¶¶') 
    stdscr.addstr(9,xx,'  ¶     ¶¶¶¶     ¶¶¶¶¶      ¶¶¶¶¶¶ ¶')
    stdscr.addstr(10,xx,'  ¶    ¶¶¶¶¶    ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶  ¶')
    stdscr.addstr(11,xx,'  ¶¶  ¶¶¶¶¶      ¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶   ¶')
    stdscr.addstr(12,xx,'   ¶  ¶¶¶          ¶¶¶¶   ¶¶¶¶¶¶¶¶¶   ¶')
    stdscr.addstr(13,xx,'   ¶¶                    ¶¶¶¶¶¶¶¶¶¶   ¶¶¶') 
    stdscr.addstr(14,xx,'   ¶¶¶     ¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶')
    stdscr.addstr(15,xx,'   ¶¶¶¶¶   ¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶')
    stdscr.addstr(16,xx,'   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶')
    stdscr.addstr(17,xx,'   ¶¶¶¶¶¶¶¶  ¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(18,xx,'    ¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(19,xx,'    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(20,xx,'    ¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶')
    stdscr.addstr(21,xx,'  ¶¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶')
    stdscr.addstr(22,xx,'  ¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(23,xx,'   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(24,xx,'                   ¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(25,xx,'                   ¶¶¶¶¶¶¶¶¶¶')
    stdscr.refresh()
    time.sleep(3)


def loser(stdscr,yy,xx):
    losestr = 'YOU LOSE!!!'
    [stdscr.addstr(yy+i,xx,mylines[6][i]) for i in range(7)]
    stdscr.refresh()
    time.sleep(1)
    
    for i in range(len(losestr)):
        stdscr.addstr(yy-1,xx+i,losestr[i])
        stdscr.refresh()
        time.sleep(0.75)
    
    time.sleep(3)


def runner(stdscr):
    guess = 0
    n = 0
    word = randword('sowpods.txt').strip().upper()
    loc = [' _'] * (len(word))
    letters = []
    guessword = ''.join(loc)
    (maxy, maxx) = stdscr.getmaxyx()
    middley = int(maxy/2)
    middlex = int(maxx/2)
    while n <= 6:
        stdscr.clear()
        if n == 6:
            loser(stdscr,middley,middlex)
            break
        
        letters.sort()
        firststr = f'You have {6 - n} incorrect guesses remaining.'
        allx = middlex-int(len(firststr)/2)
        ally = middley-6
        stdscr.addstr(ally,allx,firststr)
        
        stdscr.addstr(ally+1,allx,f'Letters guessed: {" ".join(letters)}')
        [stdscr.addstr(i,allx,mylines[n][i-ally-2]) for i in range(ally+2,ally+9)]
            
        stdscr.addstr(ally+9,allx,guessword)
        stdscr.addstr(ally+11,allx,'Guess a Letter: ')
        stdscr.refresh()
        
        guess = stdscr.getstr().decode('ascii').upper()
        
        stdscr.clear()
        stdscr.refresh()
        
        if not guess.isalpha():
            errstr = 'Letters only.'
            stdscr.addstr(middley,middlex-int(len(errstr)/2),errstr)
            stdscr.refresh()
            time.sleep(1)
            n += 1
        elif len(guess) > 1:
            if guess == word:
                guessword = word
            else:
                errstr = f'{guess} is not the word.'
                stdscr.addstr(middley,middlex-int(len(errstr)/2),errstr)
                stdscr.refresh()
                time.sleep(1)
                n += 1
        elif guess in letters:
            errstr = f'You already guessed {guess}!'
            stdscr.addstr(middley,middlex-int(len(errstr)/2),errstr)
            stdscr.refresh()
            time.sleep(1)
            n += 1
        elif guess in word:
            letters.append(guess)
            for i in range (0, len(word)):
                if word[i] == guess:
                    loc[i] = word[i]
            guessword = ''.join(loc)
        else:
            letters.append(guess)
            errstr = f'There is no {guess} in the word!'
            stdscr.addstr(middley,middlex-int(len(errstr)/2),errstr)
            stdscr.refresh()
            time.sleep(1)
            n += 1
        
        stdscr.clear()
        stdscr.refresh()
        
        if guessword == word:
            winner(stdscr,middley,middlex)
            break
    return word

if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.curs_set(0)
    #curses.nocbreak()
    word = runner(stdscr)
    print('The word was obviously ' + word)