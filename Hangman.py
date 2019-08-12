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


def winner(stdscr,my,mx):
    winstr = 'YOU WON!!!'
    
    for i in range(len(winstr)):
        stdscr.addstr(my,mx-int(len(winstr)/2)+i,winstr[i])
        stdscr.refresh()
        time.sleep(0.5)
    time.sleep(2)
    stdscr.clear()
    stdscr.refresh()
    
    topy = my - 13
    topx = mx - 22

    stdscr.addstr(topy  , topx,'          ¶¶ ¶¶  ¶¶ ¶¶ ')
    stdscr.addstr(topy+1, topx,'         ¶¶ ¶¶ ¶¶ ¶¶ ¶¶¶')
    stdscr.addstr(topy+2, topx,'     ¶¶¶¶¶            ¶¶¶¶¶¶¶')
    stdscr.addstr(topy+3, topx,'   ¶¶¶¶¶               ¶¶¶¶¶¶¶')
    stdscr.addstr(topy+4, topx,'  ¶¶¶¶¶                  ¶¶¶¶¶')
    stdscr.addstr(topy+5, topx,'  ¶¶¶¶                    ¶¶¶')
    stdscr.addstr(topy+6, topx,'   ¶¶                      ¶¶¶')
    stdscr.addstr(topy+7, topx,'   ¶                        ¶¶¶¶') 
    stdscr.addstr(topy+8, topx,'  ¶¶     ¶¶¶      ¶¶        ¶¶¶¶¶¶¶') 
    stdscr.addstr(topy+9, topx,'  ¶     ¶¶¶¶     ¶¶¶¶¶      ¶¶¶¶¶¶ ¶')
    stdscr.addstr(topy+10,topx,'  ¶    ¶¶¶¶¶    ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶  ¶')
    stdscr.addstr(topy+11,topx,'  ¶¶  ¶¶¶¶¶      ¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶   ¶')
    stdscr.addstr(topy+12,topx,'   ¶  ¶¶¶          ¶¶¶¶   ¶¶¶¶¶¶¶¶¶   ¶')
    stdscr.addstr(topy+13,topx,'   ¶¶                    ¶¶¶¶¶¶¶¶¶¶   ¶¶¶') 
    stdscr.addstr(topy+14,topx,'   ¶¶¶     ¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶¶¶   ¶¶¶¶')
    stdscr.addstr(topy+15,topx,'   ¶¶¶¶¶   ¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶')
    stdscr.addstr(topy+16,topx,'   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+17,topx,'   ¶¶¶¶¶¶¶¶  ¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+18,topx,'    ¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+19,topx,'    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+20,topx,'    ¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+21,topx,'  ¶¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶')
    stdscr.addstr(topy+22,topx,'  ¶¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+23,topx,'   ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+24,topx,'                   ¶¶¶¶¶¶¶¶¶¶¶')
    stdscr.addstr(topy+25,topx,'                   ¶¶¶¶¶¶¶¶¶¶')
    stdscr.refresh()
    time.sleep(3)


def loser(stdscr,yy,xx):
    losestr = 'YOU LOSE!!!'
    [stdscr.addstr(yy-2+i,xx-int(len(losestr)/2),mylines[6][i]) for i in range(7)]
    stdscr.refresh()
    time.sleep(.75)
    
    for i in range(len(losestr)):
        stdscr.addstr(yy-4,xx-int(len(losestr)/2)+i,losestr[i])
        stdscr.refresh()
        time.sleep(0.5)
    
    time.sleep(3)


def runner(stdscr, yy, xx):
    guess = 0
    n = 0
    word = randword('sowpods.txt').strip().upper()
    loc = ['_'] * (len(word))
    letters = []
    guessword = ' '.join(loc)
    
    middley = int(yy/2)
    middlex = int(xx/2)
        
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
            for i in range (len(word)):
                if word[i] == guess:
                    loc[i] = guess
            guessword = ' '.join(loc)
        else:
            letters.append(guess)
            errstr = f'There is no {guess} in the word!'
            stdscr.addstr(middley,middlex-int(len(errstr)/2),errstr)
            stdscr.refresh()
            time.sleep(1)
            n += 1
        
        stdscr.clear()
        stdscr.refresh()
        
        if guessword.replace(' ','') == word:
            winner(stdscr,middley,middlex)
            break
    return word

if __name__ == '__main__':
    stdscr = curses.initscr()
    (maxy, maxx) = stdscr.getmaxyx()
    
    errw = True if maxx < 44 else False
    errh = True if maxy < 26 else False
    
    if errw or errh:
        curses.endwin()
        print('Increase terminal height to play.') if errh else None 
        print('Increase terminal width to play.') if errw else None
    else:
        curses.curs_set(0)
        word = runner(stdscr,maxy,maxx)
        curses.endwin()
        print('The word was obviously ' + word)