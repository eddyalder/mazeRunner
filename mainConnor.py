import pygame
from random import randint
import numpy as np
def main():
	rows, cols = (5, 5) 
	arr = [[randint(0,14) for i in range(rows)] for j in range(cols)]
	print(arr)
	dict right
	dict left
	dict above
	dict below
if __name__ == '__main__':
	main()

	# vertical => up, down = true 0
		#left 
			#none
		#right 
			#none
		#above
			#cross
			#leftT
			#rightT
			#downT
			#downLeft
			#downRight
			#down
		#below
			#cross
			#leftT
			#upT
			#rightT
			#upLeft
			#upRight
			#up
	# horizontal => left, right = true 1
	# cross => up,down,left,right = true 2
	# leftT => up, down, left = true 3
	# upT => up, left, right = true 4
	# rightT => up, down, right = true 5
	# downT => left, right, down = true 6
	# upLeft => up, left = true 7
	# downLeft => left, down = true 8 
	# upRight => up, right = true 9
	# downRight => right, down = true 10
	# up => up = true 11
	# down => down = true 12
	# left => left =true 13
	# right => right = true 14
