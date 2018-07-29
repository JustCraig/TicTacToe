def printTable(two_d_array):
	print " "
	print " "
	newXOTable = [ [0 for j in range(3)] for i in range(3)]

	for x in range (3):
		for y in range (3):
			if two_d_array[x][y] == -1:
				newXOTable[x][y] = 'O'
			elif two_d_array[x][y] == 1:
				newXOTable[x][y] = 'X'
			else:
				newXOTable[x][y] = '-'				
	print " "
	print newXOTable[0][0] + " | " + newXOTable[0][1] + " | " + newXOTable[0][2] 
	print "----------"
	print newXOTable[1][0] + " | " + newXOTable[1][1] + " | " + newXOTable[1][2] 
	print "----------"
	print newXOTable[2][0] + " | " + newXOTable[2][1] + " | " + newXOTable[2][2]	
	

##########################################################################################
#In getUSerOneMove and getUserTwoMove, need to add checking to ensure the spot isn't taken
##########################################################################################
def getUserOneMove(two_d_array):

	goodJob=False
	inRange=False
	
	while goodJob == False:
	
		row = input ("X, enter row [0, 1, or 2]:")
		col = input ("X, enter column [0, 1 or 2]:")	

		if row >= 0 and row <=2 and col >= 0 and col <= 2:
			inRange=True
			if two_d_array[row][col]==0:
				two_d_array[row][col]=1
				goodJob=True
			else:
				print("That space is taken, please try again")
				goodJob=False	

	printTable(two_d_array)

def getUserTwoMove(two_d_array):

	goodJob=False
	inRange=False
	
	while goodJob == False:
	
		row = input ("O, enter row [0, 1, or 2]:")
		col = input ("O, enter column [0, 1 or 2]:")	

		if row >= 0 and row <=2 and col >= 0 and col <= 2:
			inRange=True
			if two_d_array[row][col]==0:
				two_d_array[row][col]=-1
				goodJob=True
			else:
				print("That space is taken, please try again")
				goodJob=False	
	printTable(two_d_array)        

#############################################################################
# checkIsWinner          
# Add the value in the rows.  If they equal 3 X wins, if they equal -3 O wins.
# Create an array for rows, cols, diag.
#############################################################################
def checkIsWinner(two_d_array):
	#	Scan Rows for winner
#two_d_array = [ [0 for j in range(cols_count)] for i in range(rows_count)]
	rowOnly = [ 0 for j in range(3)]
	colOnly = [ 0 for j in range (3)]
	diag = [0 for j in range (2)]	
	
	rowOnly[0] = [ two_d_array[0][0], two_d_array[0][1], two_d_array[0][2] ]
	rowOnly[1] = [ two_d_array[1][0], two_d_array[1][1], two_d_array[1][2] ]
	rowOnly[2] = [ two_d_array[2][0], two_d_array[2][1], two_d_array[2][2] ]

	colOnly[0] = [ two_d_array[0][0], two_d_array[1][0], two_d_array[2][0] ]
	colOnly[1] = [ two_d_array[0][1], two_d_array[1][1], two_d_array[2][1] ]
	colOnly[2] = [ two_d_array[0][2], two_d_array[1][2], two_d_array[2][2] ]

	diag[0] = [ two_d_array[0][0], two_d_array[1][1], two_d_array[2][2] ]
	diag[1] = [ two_d_array[2][0], two_d_array[1][1], two_d_array[0][2] ]

	for i, val in enumerate(rowOnly):
		if sum(rowOnly[i]) == 3:
			print ("X wins!")
			return True
		if sum(rowOnly[i]) == -3:
			print ("O wins!")
			return True
	for i, val in enumerate(colOnly):
		if sum(colOnly[i])== 3:
			print ("X wins")
			return True
		if sum(colOnly[i])==-3:
			print ("O wins")
			return True
	for i, val in enumerate(diag):
		if sum(diag[i])==3:
			print ("X wins!")
			return True
		if sum(diag[i]) == -3:
			print ("O wins!")
			return True
	return False

#############################################################################
# initializeBoard        
#  Display welcome message
#  initialize two_d_array to all 0
#  call printTable
#############################################################################
	
def initializeBoard(two_d_array):
	print " "
	print "***********************"
	print "Welcome to tick tac to"
	print "***********************"
	print " "
	print "X goes first."
	
# Initialize the array to all 0's

	two_d_array[0][0] = 0
	two_d_array[0][1] = 0
	two_d_array[0][2] = 0
	two_d_array[1][0] = 0
	two_d_array[1][1] = 0
	two_d_array[1][2] = 0
	two_d_array[2][0] = 0
	two_d_array[2][1] = 0
	two_d_array[2][2] = 0

#print the table
	printTable(two_d_array)

##############################################
#             Start the game                 #
##############################################
# 3 rows, 3 cols
rows_count = 3
cols_count = 3
winner = False   #Loops through the game until winner == True
# Create 2D array/ matrix, intialize to 0, that's what the first 0 does (?)
two_d_array = [ [0 for j in range(cols_count)] for i in range(rows_count)]

initializeBoard(two_d_array)

while (winner == False):

	getUserOneMove(two_d_array)
	winner = checkIsWinner(two_d_array)
	if winner == True:
		exit()
	
	getUserTwoMove(two_d_array)
	winner = checkIsWinner(two_d_array)
	if winner == True:
		exit()


