# Name: Min Seok Gang
# Assignment 3
# gang3@wisc.edu
# 9074016560

import copy
import numpy as np
import sys
import random

# Getting Neighboring States
def succ(state, static_x, static_y):
    succ = []
    if state[static_x] != static_y: # checking if there is a queen at the static position
        return succ
    
    for i in range(len(state)):
        
        if i == static_x: # do not modify the static position
            continue
        
        if state[i] - 1 >= 0: # move up the queen by 1
            copy = state.copy()
            copy[i] = state[i] - 1
            succ.append(copy)
            
        if state[i] + 1 <= (len(state)-1): #move down the queen by 1    
            copy = state.copy()
            copy[i] = state[i] + 1
            succ.append(copy)
    
    
    return sorted(succ)

# Getting f score of the given state
def f(state):
    if state == None:
        sys.exit("Missing Queen on Static Position")
        
    size = len(state)
    chess = np.zeros((size, size), dtype = int)
    diagonal = []
    f = 0
    
    # Creating a chessboard with fixed size based on the given state
    # 1 for where the queens are located and 0 for the rest
    for i in range(size):
        chess[state[i]][i] = 1
    
    # Check horizontally, if conflicintg queens occur switch 1 to 2
    for col in range(size):
        count1 = 0
        track = []
        for row in range(size):
            if chess[col][row] == 1:
                track.append(row)
                count1 += 1
            if row == size-1 and count1 > 1:
                f += count1
                for i in track:
                    chess[col][i] += 1

    # Getting all the diagonals present on the chessboard
    for j in range(size-1):
        diagonal.append(chess.diagonal(j))
    
    # Flipping the board by leftmost y-axis
    horizontal = np.fliplr(chess)
    for k in range(size-1):        
        diagonal.append(horizontal.diagonal(k))   
    
    # Flipping the board by bottom-most x-axis
    vertical = np.flipud(chess)                 
    for l in range(1, size-1):
        diagonal.append(vertical.diagonal(l))
    
    # Flipping the board by bottom-most x-axis of the horizontally flipped one
    vertical = np.flipud(horizontal) 
    for m in range(1, size-1):
        diagonal.append(vertical.diagonal(m))
    
    # Checking for the conflicting queens in all diagonals
    # Counting for only queens that are not counted in the horizontal checking section, only 1s are considered
    for i in range(len(diagonal)):
        diagonal[i].setflags(write = 1)
        count2 = 0
        count3 = 0
        track = []
        for j in range(len(diagonal[i])):
            if diagonal[i][j] == 1:
                count2 += 1
                track.append(j)
            if diagonal[i][j] == 2:
                count3 += 1
            if j == len(diagonal[i])-1 and count2 + count3 > 1:
                f += count2
                for k in track:
                    diagonal[i][k] += 1
                
    return f

# Choosing the next state
def choose_next(curr, static_x, static_y):
    succ_state = succ(curr, static_x, static_y)
    neighbor = []
    f_score = f(curr)
    
    neighbor.append((f_score, curr))
    
    if succ_state == []:
        return None
    
    for i in succ_state: 
        f_succ = f(i)
        if f_succ <= f_score:
            neighbor.append((f_succ, i))
    
    if len(neighbor) == 1:
        return neighbor[0][1]
    
    neighbor = sorted(neighbor, key=lambda x: x[0]) # Sorting based on f value
    
    temp = []
    for i in neighbor:
        if neighbor[0][0] == i[0]:
            temp.append(i)
            
    temp = sorted(temp, key=lambda y: y[1]) # Sorting based on ascending state
    
    return temp[0][1]
    
# Getting the convergence of the given initial state by using choosing next function
def n_queens(initial_state, static_x, static_y):
    #local minimum = encountering two states with the same f value in the consecutive two steps
    before = initial_state
    while True:
        print(before, " - f=", f(before), sep='')
        f1 = f(before)
        after = choose_next(before, static_x, static_y)
        f2 = f(after)
        before = after
        
        if f1 == 0:
            return after
        
        if f1 == f2:
            print(after, " - f=", f(after), sep='')
            return after
        
# Hill climbing algorithm with k random restarts
def n_queens_restart(n, k, static_x, static_y):
    random.seed(1)
    mystery = rand_state(n, static_x, static_y)
    track = []
    while k != 0:
        result = convergence(mystery, static_x, static_y)
        if f(result) != 0: # when there is converging state with f score not equal to 0
            track.append((result, f(result)))
            mystery = rand_state(n, static_x, static_y)
            k -= 1
        else: # when a state with f score 0 is found
            print(result, " - f=", f(result), sep='')
            return
                         
    track = sorted(track, key=lambda x: x[1]) # Sorting based on f value
    temp = []
    for i in track:
        if track[0][1] == i[1]:
            temp.append(i)
            
    temp = sorted(temp, key=lambda y: y[0]) # Sorting based on ascending state 
                         
    for i in temp:
        print(i[0], " - f=", i[1], sep='') # Printing out the best states with its f value
            
# Function to generate the converging state of the given state
def convergence(initial_state, static_x, static_y):
    before = initial_state
    while True:
        f1 = f(before) 
        after = choose_next(before, static_x, static_y)
        f2 = f(after)
        before = after # before = current state / after = next state to consider
        if f1 == f2 or f1 == 0:
            break
        
    return after

# Random state generator
def rand_state(n, static_x, static_y):
    initial_state = []
    count = n
    while count != 0:
        rand_int = random.randint(0,n-1)
        initial_state.append(rand_int)
        count -= 1
        
    initial_state[static_x] = static_y
    
    return initial_state