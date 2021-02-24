# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

import curses
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT
from random import randint

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    
score = 0

 # Initial snake position / Initial food position / Food visualisation
snake = [[4,10], [4,9], [4,8]]                                 
food = [15,30]                                                     
win.addch(food[0], food[1], 'o')                                   

#ESC is not pressed / increase snakes speed and lenght
while key != 27:                                                   
    win.border(0)
    win.addstr(0, 2, 'Current score : ' + str(score) + ' ')    
    win.timeout(150 - (len(snake)//5 + len(snake)//10)%120)         
    
    prevKey = key                                                  
    event = win.getch()
    key = key if event == -1 else event 

    # Spacebar - PAUSE/RESUME game
    if key == ord(' '):                                            
        key = -1                                                   
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, 27]:     
        key = prevKey

    # Calculates the new coordinates of the head of the snake.
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # Quit if snake hit border
    if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

    # If snake hit himself
    if snake[0] in snake[1:]: break

    #food consumption, new food location
    if snake[0] == food:                                            
        food = []
        score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 58)]                 
            if food in snake: food = []
        win.addch(food[0], food[1], 'o')
    else:    
        last = snake.pop()                                          
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '0')
    
curses.endwin()
print("\nScore - " + str(score))