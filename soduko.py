#soduko game : chaque ligne et chaque col doit avoir les nb de 1 a 9
import random 
import numpy as np

def found_val(vect, val):
    i = 0 
    while i < len(vect) and vect[i] != val:
        i+= 1
    return i==len(vect)

def existe(board, l , c , valeur):
	if found_val(board[l], valeur): 
		return False
	colonne = []
	for i in range(9):
		colonne.append(board[i][c])
	if found_val(colonne, valeur):
		return False
	else:
		return True

#generer aleatoirement une table
def new_board():
    board = np.zeros((9,9) , dtype = int)
    for i in range(30):
            l , c = random.randint(0,8) , random.randint(0,8)
            valeur = random.randint(1,9)
            while existe(board, l , c , valeur):
            	l , c = random.randint(0,8) , random.randint(0,8)
            	valeur = random.randint(1,9)
            board[l][c] = valeur
    return board

    
#obtenir si une ligne cotient les valeurs de 1 a 9 sans repetition
def ligne_correcte(ligne):
	
	t = []
	for e in ligne:
		if e not in t and e>=1 and e<=9:
			t.append(e)
	if len(t) != 9: 
		return False
	else:
		return True
	
#obtenir si une colonne cotient les valeurs de 1 a 9 sans repetition
def colonne_correcte(table , j):
	
	colonne = []
	#la colonne numero j 
	for i in range(9):
		colonne.append(table[i][j])
	return lignes_correcte(colonne)

#check if a box is correct
def box_correct(box):
	t = [ ]
	for i in range(3):
		for j in range(3):
			if not found_val(t , box[i][j]):
				t.append(box[i][j])
			else:
				return False
	return True 

#Afficher la table
def draw_table(table):
	for i in range(9):
		print(table[i])

#Obtenir si le joueur a gagne
def Won(board):
	won, i  = True , 0
	#checking for boxes
	l,c =0,0
	t = []
	while l<9 and won:
		while c < 9 and won:
			if not box_correct(board[l:l+3][c:c+2]):
				won = False
			else:
				c += 3
		l += 3

	#checking for rows and columns
	while i < 9 and won:
		if not ligne_correcte(board[i]) or not colonne_correcte(i) :
			won = False
		else:
			i += 1
	return won

#modifier une valeur de la table
def modifier_valeur(table,i,j,new_val):
	table[i][j] = new_val
	return table

#obtenir si il existe encore une case vide 
def zero_existe(table):
	i,j = 0,0
	found = False
	while i<9 and j<9 and not found:
		if table[i][j] == 0:
			found = True
		else:
		    i += 1
		    j += 1
	return found

#afficher le resultat de la partie
def afficher_resultat(board):
	if Won(board):
		print('Vous avez gagne, felicitations !')
	else:
		print("Malheureusement, vous n'avez pas reussi cette fois")

def recuperer_param(entree):
    l = int(entree[0]) -1 
    c = int(entree[2]) -1
    nv_val = int(entree[4])
    return l , c , nv_val
 
 #Create a recursive function that takes a grid and the current row and column index

 #backtracking algorithm







print("voici la table, remplacez les zeros") 

board2 = new_board()
draw_table(board2)
user_choice = input("vous pouvez taper auto pour que l'ordinateur vous resolve la partie")
if user_choice == 'auto' or user_choice == 'AUTO':
	print("Solving ...")
	solve(board2)
	print("solved")
	draw_table(board2)

else:
	while zero_existe(board2):
		param = input('Donner la ligne, la colonne et nouvelle la valeur separe par des espaces.')
		l ,c , nv_val  = recuperer_param(param)
		board2 = modifier_valeur(board2, l , c ,nv_val)
		draw_table(board2)


	print('Vous avez rempli toutes les cases')
	afficher_resultat(board2)






