#CHECKER BOARD
def checkerboard():
    for i in range(2, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4

checkerboard()
