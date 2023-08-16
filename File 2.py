from collections import Counter
from copy import deepcopy
from time import sleep
from colorama import init, Fore, Style

# Initialize colorama
init()

import numpy as np


class Soduko_solver:

    def __init__(self,grid):

        self.grid=grid
        self.n=9           #Each row or column size
        self.box_size=3    #Each box size
        self.solutions=[]
        self.num=[1,2,3,4,5,6,7,8,9]     #Numbers of grid

    #This will check for errors in input and will call actual solution
    #function
    def Solution_provider(self):

        Check=self.checking_for_errors_in_grid()
        #To check is provided input is correct according to rules
        if Check[0]==False:
            print(a[1])
        else:
            i,j=0,0
            #To get your grid
            self.Solution_provider2(i,j)

    #This function will create your grid  using backtracking
    def Solution_provider2(self,i,j):

        if j==9:
            i+=1;j=0
            self.Solution_provider2(i,j)

        if i==9:
            if self.checking_for_errors_in_grid()[0]==True:
                self.solutions.append(deepcopy(self.grid))

            return

        box=self.grid[((i//self.box_size)*self.box_size):((i//self.box_size)*self.box_size)+self.box_size,((j//self.box_size)*self.box_size):((j//self.box_size)*self.box_size)+self.box_size]

        if self.grid[i][j]==0:

            for ele in self.num:
                if ele not in self.grid[i] and ele not in self.grid[0:self.n,j] and ele not in  self.grid[((i//self.box_size)*self.box_size):((i//self.box_size)*self.box_size)+self.box_size,((j//self.box_size)*self.box_size):((j//self.box_size)*self.box_size)+self.box_size]:
                    self.grid[i][j]=ele
                    self.Solution_provider2(i,j+1)
                    if 0 not in self.grid and self.checking_for_errors_in_grid()[0]==True:
                        return
                    self.grid[i][j]=0

        elif self.grid[i][j]!=0:
            self.Solution_provider2(i,j+1)
            if 0 not in self.grid and self.checking_for_errors_in_grid()[0]==True:
                return

    #This function will look for erorrs in grid
    def checking_for_errors_in_grid(self):

        for i in range(self.n):

            count=Counter(self.grid[i])
            for key in count.keys():
                if key!=0 and count[key]>1:
                    return [False,'REPETITION FOUND IN ROW']

        for i in range(self.n):

            count=Counter(self.grid[0:self.n,i])
            for key in count.keys():
                if key!=0 and count[key]>1:
                    return [False,'REPETITION FOUND IN COLUMN']

        for i in range(0,self.n,self.box_size):
            for j in range(0,self.n,self.box_size):

                #To get box of each element
                Box=(self.grid[i:i+self.box_size,j:j+self.box_size])
                Count=Counter(Box[0])
                Count2=Counter(Box[1])
                Count3=Counter(Box[2])
                Count.update(Count2)
                Count.update(Count3)
                for key in Count.keys():

                    if key!=0 and Count[key]>1:
                        return [False,'REPETITION FOUND IN BOX']

        return [True]

    def solution(self):

        if 0 not in self.grid and self.checking_for_errors_in_grid()[0]==True:
            print('Here is your Grid , Thanks for patience')
            return self.grid

        s=("Not possile to make Soduko Table with these values as input .\n")
        s+=('In this game you cannot enter values randomly u have to respect rules .\n')
        s+=('Thankyou .')

        return s



def main():

    #Hello , here is 9*9 Grid is given with zero as default value
    #set for that game. This game works in such way that the user
    #change some values in this grid (possibly zero) and this program
    #will return u the grid having values from 1 to 9 each value will
    #not repeat more than 9 times and each column and each row contains
    #ditinct values only, Thank you.

    grid=np.array([
       [1,2,3,4,5,6,7,8,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0,0],
       [0,1,0,0,0,0,0,0,0],
       [0,0,0,0,1,0,0,0,0],
       [0,0,0,0,0,0,0,1,0],
       [0,0,1,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,1]])

    copy_grid=deepcopy(grid)
    game=Soduko_solver(grid)
    game.Solution_provider()
    grid_2=(game.solution())

    if isinstance(grid_2, str):
        print(grid_2)

    else:

        for i in range(9):
            print(' '*10,end=' ')
            for j  in range(9):

                if copy_grid[i][j]==0:
                    print(Fore.GREEN+str(grid_2[i][j]),end=' ')
                else:
                    print(Fore.RED+str(grid_2[i][j]),end=' ')

            print()

        print()

main()
