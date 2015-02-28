def spiral(n):
    dx,dy = 1,0            # Starting increments
    x,y = 0,0              # Starting location
    myarray = [[None]*n for i in range(n)] # Create nxn matrix with empty values
    for i in range(n**2):
        myarray[x][y] = i
        nx = x + dx
        ny = y + dy
        print i
        print "nx: {0}, ny: {1}".format(nx, ny)
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] is None:
            x = nx
            y = ny
        else:
            print "dx: {0}, dy: {1}".format(dx, dy)
            dx,dy = -dy,dx
            x = x + dx
            y = y + dy
    return myarray

def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print "{0}".format(myarray[x][y]),
        print

# printspiral(spiral(5))
spiral(5)
