import numpy as np
import random
import sys
import copy

class World():

    def __init__(self, filename = None, definedWorlds=None):
        self.__world = []
        self.__startPosition=0
        self.__testArray=[bool,bool,0,0,0,0,0,0,0]  # W,S,P,R,G,E,T,B,F
        self.__p1,self.__p2,self.__p3 = 0.0,0.0,0.0
        self.__r=1
        self.__G=1
        self.__E=1
        if filename != None:
            self.__loadWorldFromFile(filename)

    def __loadWorldFromFile(self,filename):
        file=open(filename,'r')
        lines=list(file.readlines())
        for line in lines:
            label=line[0]
            if line[1]==' ':
                newline=line[2:]
            if label=='W':
                param=[int(i) for  i in newline.split(' ')]
                self.__sizeX=param[0]-1
                self.__sizeY=param[1]-1
                print(param)
                self.__initWorld(param[0],param[1])
            elif label=='S':
                param=[int(i) for  i in newline.split(' ')]
                self.__setField((param[0]-1),(param[1]-1),'S')
            elif label=='P':
                param=[float(i) for  i in newline.split(' ')]
                self.__p1,self.__p2,self.__p3 = param[0],param[1],param[2]
            elif label=='R':
                param=[float(i) for  i in newline.split(' ')]
                self.__r = param[0]
            elif label=='G':
                param=[float(i) for  i in newline.split(' ')]
                self.__G = param[0]
            elif label=='E':
                param=[float(i) for  i in newline.split(' ')]
                self.__E = param[0]
            elif label=='T':
                param=[float(i) for  i in newline.split(' ')]
                self.__setField((int(param[0])-1),(int(param[1])-1), param='T',val=param[2])
            elif label=='B':
                param=[float(i) for  i in newline.split(' ')]
                self.__setField((int(param[0])-1),(int(param[1])-1), param='B',val=param[2])
            elif label=='F':
                param=[float(i) for  i in newline.split(' ')]
                self.__setField((int(param[0])-1),(int(param[1])-1), param='F',val=0)

            else:
                a=1
        self.showMap()
    def __initWorld(self, x,y):
        xlist=[]
        for i in range(0,x):
            xlist.append(['N',0])
        for i in range(0,y):
            self.__world.append(copy.deepcopy(xlist))
    def __setField(self,x,y,param=None, val=None):
        print(x,y)
        if param!=None:
            self.__world[y][x][0]=param
    
    
    def GetstartPosition(self): 
        return 1,1
    def loadExampleWorld(self,choice=1):

        if choice==1:
            self.__world = [[ ['N',0] , ['N',0] ,['N',0],['T',1]],
                            [ ['N',0] ,['F','-'],['N',0],['T',1]],
                            [['S','+'], ['N',0],['N',0], ['N',0] ]]
        
        elif choice==2:
            self.__world = [[['N',0],['N',0],['B',0],['N',0]],
                            [['S','+'],['F','-'],['F','-'],['T',1]],
                            [['N',0],['N',0],['B',0],['N',0]]]

        elif choice==3:
            self.__world = [[['T',1],['N',0],['B',0],['N',0],['T',1]],
                            [['N',0],['F','-'],['N',0],['F','-'],['N',0]],
                            [['B',0],['N',0],['S','+'],['N',0],['B',0]],
                            [['N',0],['F','-'],['N',0],['F','-'],['N',0]],
                            [['T',1],['N',0],['B',0],['N',0],['T',1]]]


        else:
            self.__world = [[['N',0],['N',0]  , 0,['T',1]],
                            [['N',0],['F','-'], 0,['T',1]],
                            [['S','+']    , 0       , 0,['N',0]]]
    def loadWorldFromFile(self):
        print(len(self.__testArray))
        self.__world=np.zeros((self.__sizeY,self.__sizeX))
        for x in range(0,4):
            for y in range(0,3):
                self.__world[y][x][1]=random.randint(0,50)+x+y
        return
    
    def showMap(self):
        for i in range(len(self.__world)-1,-1,-1):
            print(self.__world[i])
        # print(self.__world[1][1])

    # def 


#####################################################################################
#######################     TEST
#####################################################################################


print(sys.argv)
print()
w=World(filename='./worlds/w4x3-0.data')
# w.loadExampleWorld()
# w.showMap()