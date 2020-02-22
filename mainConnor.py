import pygame
from random import randint
from random import choice
import numpy as np
def main():
	rows, cols = (2, 2) 
	arr = [[0 for i in range(rows)] for j in range(cols)]
	#print(arr)
	noLeft = [0,5,9,10,11,12,14]
	allLeft = [1,2,3,4,6,7,8,13]
	noRight = [0,3,7,8,11,12,13]
	allRight = [1,2,4,5,6,9,10,14]
	noDown = [1,4,7,9,11,13,14]
	allDown = [0,2,5,6,8,10,12]
	noUp = [1,6,8,10,12,13,14]
	allUp = [0,2,3,4,5,7,9,11]

	right = {
		0 : noLeft,
		1 : allLeft,  #all left
		2 : allLeft,	
		3 : noLeft,
		4 : allLeft,
		5 : allLeft,
		6 : allLeft,
		7 : noLeft,
		8 : noLeft,
		9 : allLeft,
		10: allLeft,
		11: noLeft,
		12: noLeft,
		13: noLeft,
		14: allLeft 
	}
	left = {
		0 : noRight, #no right
		1 : allRight, #all right
		2 : allRight, #all right
		3 : allRight,
		4 : allRight,
		5 : noRight,
		6 : allRight,
		7 : allRight,
		8 : allRight,
		9 : noRight,
		10: noRight,
		11: noRight,
		12: noRight,
		13: allRight,
		14: noRight
	}
	above = {
		0 : allDown, #all down
		1 : noDown, #no down
		2 : allDown,
		3 : allDown,
		4 : allDown,
		5 : allDown,
		6 : noDown,
		7 : allDown,
		8 : noDown,
		9 : allDown,
		10: noDown,
		11: allDown,
		12: noDown,
		13: noDown,
		14: noDown
	}
	below = {
		0 : allUp, #all up
		1 : noUp, # no up
		2 : allUp,
		3 : allUp,
		4 : noUp,
		5 : allUp,
		6 : allUp,
		7 : noUp,
		8 : allUp,
		9 : noUp,
		10: allUp,
		11: noUp,
		12: allUp,
		13: noUp,
		14: noUp
	}

	shape0 = [" | ",
			  " | ",
			  " | "]
	shape1 = ["   ",
			  "---",
			  "   "]
	shape2 = 

	arr[0][0] = randint(0,14)
	for i in range(rows-1):
	 	for j in range(cols-1):
	 		arr[i+1][j] = choice(below[arr[i][j]])
	 		arr[i][j+1] = choice(right[arr[i][j]])
	arr[rows-1][cols-1] = choice(below[arr[rows-2][cols-1]])
	print(arr)
if __name__ == '__main__':
	main()

	# vertical => up, down = true 0
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
