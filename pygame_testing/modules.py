# --------------=<Constants>=-------------- #

BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

# --------------=</Constants>=-------------- #


def chessboard(screen,surface_sz,n):
    #creates a chess board
    
    sq_sz = surface_sz // n
    colors = [WHITE,BLACK]
    

    for row in range(n):           # Draw each row of the board.
        
        c_indx = row % 2           # Change starting color on each row
        
        for col in range(n):       # Run through cols drawing squares
            
            the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
            screen.fill(colors[c_indx], the_square)
            # now flip the color index for the next square
            c_indx = (c_indx + 1) % 2