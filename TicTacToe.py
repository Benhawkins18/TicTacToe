'''
written by: Ben Hawkins
for questions feel free to call 682-564-4902 or email ben.hawkins@ttu.edu
python 2.7

A *cell* is an integer in the interval [0,9). Cells represent squares on the tic tac toe board as pictured below:
0|1|2
3|4|5
6|7|8

A *game state* is a list of nine strings, each of whose members is either 'x', 'o', or 'e'. 
The game state S is visualized as a board configuration in which the contents of cell i is S[i] for 0<=i<9. For example, 
the game state ['x','e','e','e','o','e','e','e','x'] can be visualized as follows:

x| |
 |o|
 | |x

A *point* is a pair (x,y) of integers where 0 <= x <= 600 and 0<= y
<= 500.Points are interpreted as points in a graphics window 600 pixels wide by 500 pixels high, with (0,0) in the lower left corner, 
x increasing to the right and y increasing upward.

a *rectangle* is a an object rectanlge(x,y,w,h), where x,y,w,h are all positive integers, that refers to a rectanlge
who's lower left corner is at the point (x,y) and who's width is w and height is h

the tic tac toe game board consists of 10 rectangles. 

the cells at indeces 0,1,2, 3,4,5  6,7,8 are reprented by the following respective rectanlges: 
0: rectangle(0,333,166,166), 1: rectangle(167,333,166,166), 2: rectangle(333,333,166,166),
3: rectangle(0,167,166,166), 4: rectangle(167,167,166,166), 5: rectangle(333,167,166,166),
6: rectangle(0,0,166,166),   7: rectangle(167,0,166,166),   8: rectangle(333,0,166,166)

a play again button is represented as rectangle(500,0,100,500))

'''
import random
import graphics

class rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

     
# if rect is a rectanlge and p is a point then point_inside_rectanlge(rect,p) means point p is inside the bounds of the rectanlge and 
#is not direclty on the outside edge
def point_inside_rectanlge(rect,point):
    return (rect.x < point[0] <= rect.x + rect.width) and (rect.y < point[1] < rect.y + rect.height)

#initialState() returns the gamestate that represents an empty board with no x's or o's
def initialState():
    return ['e','e','e','e','e','e','e','e','e']


#if s is a gameState then x_or_o_has_three_in_a_row(s) means x or o has a "three in a row"

def x_or_o_has_3_in_a_row(gameState):
    list_of_winning_combos = (
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 4, 8}, {2, 4, 6})
    
    list_of_indeces_with_empty = [x for x in range(9) if gameState[x] == 'e']
    list_of_indeces_with_o = [x for x in range(9) if gameState[x] == 'o']
    list_of_indeces_with_x = [x for x in range(9) if gameState[x] == 'x']
    
    for combo in list_of_winning_combos:
        if combo.issubset(list_of_indeces_with_o):
            return True
    for combo in list_of_winning_combos:
        if combo.issubset(list_of_indeces_with_x):
            return True
    return False
        

#if p is a point then get_clicked_button_index(p) is an integer i where 0<=i=<10 representing an index of the clicked button
#indeces 0-8 inclusive refer to the respective cells on the game board, index 9 refers to the "play again" button 
#and index 10 refers to no button hit

def clicked_button_index(point): #
    
    list_of_button_rectanlges = [rectangle(0,333,166,166),rectangle(167,333,166,166),rectangle(333,333,166,166),
                                 rectangle(0,167,166,166),rectangle(167,167,166,166),rectangle(333,167,166,166),
                                 rectangle(0,0,166,166),  rectangle(167,0,166,166),  rectangle(333,0,166,166),
                                 rectangle(500,0,100,500)
                    ]
    for i in range(0,10):
        if point_inside_rectanlge(list_of_button_rectanlges[i],point):
            
            return i
    
    return 10 #if no button was hit return 10



# if s is a game state and there is at least one 'e' in the gameState then index_of_computers_move(s) is the index of the move
# that follows the logic written below. 

# 1. If the computer can win in one move, it does. Otherwise,
# 2. If the computer has to block, it does; otherwise,
# 3. The computer moves in the middle if it is empty; otherwise
# 4. The computer moves in a corner cell, selected at random from the empty corner squares, if any corners are empty; otherwise
# 5. The computer moves in a random empty cell. 
def index_of_computers_move(gameState): 
#//this function is longer then I'm normally comfortable with and coould be made more compact with a helper function but 
#//I think this way it's easier to verify it follows the logic correctly with out having to scroll up and down. //Is this an acceptable sacrifice to make?
    
    list_of_winning_combos = (
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 4, 8}, {2, 4, 6})
    
    list_of_indeces_with_empty = [x for x in range(9) if gameState[x] == 'e']
    list_of_indeces_with_o = [x for x in range(9) if gameState[x] == 'o']
    list_of_indeces_with_x = [x for x in range(9) if gameState[x] == 'x']
    
   
    
    ####### 1. if the computer can win in one move it does #######
    for i in range(len(list_of_indeces_with_empty)):
        for combo in list_of_winning_combos:
            if combo.issubset(list_of_indeces_with_o+list_of_indeces_with_empty[i:i+1]):
                return list_of_indeces_with_empty[i]
    
    ####### END: 1. if the computer can win in one move it does #######
    
    ####### 2. if player can win in one move block   #######
    for i in range(len(list_of_indeces_with_empty)):
        for combo in list_of_winning_combos:
            if combo.issubset(list_of_indeces_with_x+list_of_indeces_with_empty[i:i+1]):
                return list_of_indeces_with_empty[i]
    ####### END 2.  if player can win in one move block   #######
    
    ####### 3. move in middle of its empty #######
    if gameState[4] == 'e':
        return 4
    ####### END 3. move in the middle if its empty #####
    
    ####### 4. Computer moves in random corner cell if there is one available ######
    empty_corners = [x for x in [0,2,6,8] if gameState[x] == 'e']
    if empty_corners != []:
        return random.choice(empty_corners)
    ####### END 4. Computer moves in random corner cell if there is one available ######
    
    ###### 5. The computer moves in a random empty cell. #####
    return random.choice(list_of_indeces_with_empty)  
    ###### End 5. The computer moves in a random empty cell. #####
    


# if S is a game state and p is a point, then successor(S,p) is the game state resulting from clicking point p in game state S.
def successor(gameState,point):
    
    index_of_clicked_button = clicked_button_index(point)
    #print index_of_clicked_button
    
    
    
    if index_of_clicked_button == 9: # play again button clicked
        return initialState()
    if x_or_o_has_3_in_a_row(gameState): # game is over no more new moves can be made
        return gameState
    elif index_of_clicked_button == 10: # no button clicked
        return gameState
    elif gameState[index_of_clicked_button] != 'e': # the clicked button isn't empty
        return gameState
    elif gameState[index_of_clicked_button] == 'e': # the player clicked an empty spot
        gameState[index_of_clicked_button] = 'x'
        if x_or_o_has_3_in_a_row(gameState): #check if player has won with the move he just played
            return gameState
        if 'e' in gameState: # player didnt win and the board isnt full
            gameState[index_of_computers_move(gameState)] = 'o'
        return gameState

# if index is a cell  then images_for_x_at_index(index) returns a list of two lines that represent that x at that cell
def images_for_x_at_index(index):
    x = (index%3)
    y = 2 - (index/3)
    size = 166
    return [(x*size,y*size,x*size+size,y*size+size),(x*size,y*size+size,x*size+size,y*size)]
# if index is a cell  then images_for_x_at_index(index) returns a circle that represents an o at that cell
def image_for_o_at_index(index):
    x = (index%3)
    y = 2 - (index/3)
    size = 166
    return (x*size+size/2,y*size+size/2,size/2-1)
    
# displayImages(S) is a list of images to display on the screen in state S.    
def displayImages(state):
    
    c1 = (166,500,166,0)
    c2 = (167,500,167,0)
    c3 = (332,500,332,0)
    c4 = (333,500,333,0)
    r1 = (0,166,500,166)
    r2 = (0,167,500,167)
    r3 = (0,332,500,332)
    r4 = (0,333,500,333)
    play = (500,0,500,500)
    text = ('play again', 550,250,10)
    image_list = [c1,c2,c3,c4,r1,r2,r3,r4,play,text]
    
    for i in range(9):
        if state[i] == 'x':
            image_list.extend(images_for_x_at_index(i))
        elif state[i] == 'o':
            image_list.append(image_for_o_at_index(i))
    return image_list
    

######################################################################
######################################################################
# TPGE GAME ENGINE
#
# Student code is linked with this code to create a game.

# displaySize() is the size of the display window, (width, height)

def displaySize() : return (600,500)
from graphics import *

# If x is an image, imageKind(x) is the type of image x is:
# 'circle', 'text', or 'lineSegment'

def imageKind(x):
    if len(x)==3 : return 'circle'
    elif type(x[0])== str :return 'text'
    else : return 'lineSegment'

    
# If x is an image, convert(x) is the corresponding image in the
# graphics.py library. We turn the screen upside down so that the origin
# is in the lower left corner, so it matches what they learn in algebra
# class.

def convert(x):
    if imageKind(x)=='circle': return convertCircle(x)
    elif imageKind(x)=='lineSegment': return convertLine(x)
    elif imageKind(x)=='text' : return convertText(x)


def convertLine(x):
    (W,H) = displaySize()
    P1 = Point(x[0],H - x[1])
    P2 = Point(x[2],H - x[3])
    return Line(P1,P2)

def convertText(x):
    (W,H) = displaySize()
    center = Point(x[1],H-x[2])
    string = x[0]
    size = x[3]
    T = Text(center,string)
    T.setSize(size)
    return T

def convertCircle(x):
    (W,H) = displaySize()
    center = Point(x[0],H-x[1])
    radius = x[2]
    return Circle(center,radius)

# Create a window to play in
display = GraphWin("My game", displaySize()[0], displaySize()[1])


# The main loop
#
# Set the state, draw the display, get a mouse click, set the new state,
# and repeat until the user closes the window.

S = initialState()
images = [convert(x) for x in displayImages(S)]

while(True):
    for x in images: x.draw(display)
    c = display.getMouse()
    click = (c.getX(),displaySize()[1] - c.getY())
    S = successor(S,click)
    for I in images: I.undraw()
    images = [convert(x) for x in displayImages(S)]       

########### Testing Code ###################
def play_list_of_moves_debug_mode(list_of_moves):
    gameState = initialState()
    for point in list_of_moves:
        print "player clicked at index: " + str(clicked_button_index(point)) + "\n"
        gameState = successor(gameState,point)
        render_board(gameState)

def play():
    
            # index 6        6      3        7          2           2
    move_list1 = [(100,100),(10,1),(111,222),(222,111),(400,400),(400,400)]
            #index    2       6       8        0         1        7
    move_list2 = [(490,384),(1,2),(482,100),(11,490),(200,390),(48,200)] # this play will result in a loss or a win depending on random choice of the computer
    
    play_list_of_moves_debug_mode(move_list1)
    print "\n\n\New Game: n\n" 
    play_list_of_moves_debug_mode(move_list2)
    
def render_board(gameState):
    print gameState[0] +'|' +gameState[1] +'|' + gameState[2]
    print "______"
    print gameState[3] +'|' +gameState[4] +'|' + gameState[5]
    print "______"
    print gameState[6] +'|'+gameState[7]+  '|' + gameState[8]  + "\n"
    
def test():
    gameState = initialState()
    while 'e' in gameState:
        render_board(gameState)
        x = int(raw_input("enter x value of coordinate: "))
        y = int(raw_input("enter y value of coordinate: "))
        point = (x,y)
        gameState = successor(gameState,point)
        
    render_board(gameState)
    
play()
#test()




    
    
    