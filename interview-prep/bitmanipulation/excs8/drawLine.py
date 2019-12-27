# Draw Line: A monochrome screen is stored as a single array of bytes, allowing
# eight consecutive pixels to be stored in one byte. The screen has width w,
# where w is divisible by 8 (that is, no byte will be split across rows). The
# height of the screen, of course, can be derived from the length of the array
# and the width. Implement a function that draws a horizontal line from
# (x1 , y) to (x2 , y).
#
# The method signature should look something like: drawl ine(byte[] screen,
# int width, int x1, int x2, int y)

# height = len(screen) / width
# check if height is int
# if x1 % width != x2 % (width -1?) => error, not on same line
# loop from height int(x1 / 8)
# go into array x1 % 8 and change that values in that array
# maybe make a func to speed this up (creatse 1101010 for how many)
# start and finish are done serpeartely from middle. can just wipe middle ones

# 01234567 =>
# start(3) => 00111111 : 2^(9 - x) - 1
# end(3) => 11100000 (2^(x + 1) - 1) << (9 - x)
