import numpy as np
import random
import sys


class World_MDP():

    def __init__(self, sizeX, sizeY):
        self.__sizeX=sizeX
        self.__sizeY=sizeY
        self.__world = 0
        self.__testArray=[0,0,0,0,0,0,0,0,0]  # W,S,P,R,G,E,T,B,F

    
    def loadExampleWorld(self,choice=1):

        if choice==1:
            self.__world = [[ 0 , 0 ,0,'T'],
                            [ 0 ,'F',0,'T'],
                            ['S', 0, 0, 0 ]]
        
        elif choice==2:
            self.__world = [[ 0 , 0 ,'B', 0 ],
                            ['S','F','F','T'],
                            [ 0 , 0 ,'B', 0 ]]

        elif choice==3:
            self.__world = [['T', 0 ,'B', 0 ,'T'],
                            [ 0 ,'F', 0 ,'F', 0 ],
                            ['B', 0 ,'S', 0 ,'B'],
                            [ 0 ,'F', 0 ,'F', 0 ],
                            ['T', 0 ,'B', 0 ,'T']]


        else:
            self.__world = [[ 0 , 0 ,0,'T'],
                            [ 0 ,'F',0,'T'],
                            ['S', 0, 0, 0 ]]
    def loadWorldFromFile(self):
        print(len(self.__testArray))
        self.__world=np.zeros((self.__sizeY,self.__sizeX))
        for x in range(0,4):
            for y in range(0,3):
                self.__world[y][x]=random.randint(0,50)+x+y
        return
    
    def showMap(self):
        for i in range(0,len(self.__world)):
            print(self.__world[i])
        print(self.__world[1][1])

    # def 




print(sys.argv)
print()
w=World_MDP(4,3)
w.loadExampleWorld(3)
w.showMap()