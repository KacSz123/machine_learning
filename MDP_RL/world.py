import numpy as np
import random
import sys
import copy

class World():

    def __init__(self, filename = None, definedWorlds=None,r=-0.04,g=1,e=0):
        self.__world = []
        self.__policy=[]
        self.__startPosition=[]
        self.__testArray=[bool,bool,0,0,0,0,0,0,0]  # W,S,P,R,G,E,T,B,F
        self.__p1,self.__p2,self.__p3 = 0.0,0.0,0.0
        self.__r=r
        self.__G=g
        self.__E=e
        self.__directions=('^','>','v','<')    
        if filename != None:
            self.__loadWorldFromFile(filename)
        # self.showParams()
        print("------------------")
        print(len(self.__world))
        print(len(self.__world[0]))
        print(len(self.__world[0][3]))
        print("------------------")
    def getR(self):
        return self.__r
    def getG(self):
        return self.__G
    def getE(self):
        return self.__E
    def getStart(self):
        return self.__startPosition
    def getP(self):
        return self.__p1,self.__p2,self.__p3
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
                self.__startPosition=[param[0]-1,param[1]-1]
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
    def showParams(self):
        print([self.__sizeX, self.__sizeY])
        print(self.__p1)
        print(self.__p2)
        print(self.__p3)
        print(self.__r)
        print(self.__G)
    def __initWorld(self, x,y):
        xlist=[]
        xplist=[]
        for i in range(0,x):
            xlist.append(['N',0, self.__r])
            xplist.append([])
        for i in range(0,y):
            self.__world.append(copy.deepcopy(xlist))
            self.__policy.append(xplist.copy())
    def __inittmpW(self, x,y):
        xlist=[]
        tmpWorld=[]
        for i in range(0,x):
            xlist.append([])
        for i in range(0,y):
            return tmpWorld.append(copy.deepcopy(xlist))
    def __setField(self,x,y,param=None, val=None):
        # print(x,y)
        if param!=None:
            self.__world[y][x][0]=param
        if (param=='B' or param=='T') and val!=None:
            self.__world[y][x][2]=val
        if param=='T':
            self.__world[y][x][1]=val
    def __up(self):
        return self.__directions[0]
    def __right(self):
        return self.__directions[1]
    def __down(self):
        return self.__directions[2]
    def __left(self):
        return self.__directions[3]
#self.__directionsself.__directions=('^','>','v','<') 
    def ifBump(self, start, direction):
        # print(direction)
        if direction == self.__up():
            if start[0]>=self.__sizeY or self.__world[start[0]+1][start[1]][0]=='F':
                return True
        if direction == self.__left():
            if start[1]<=0 or self.__world[start[0]][start[1]-1][0]=='F':
                return True
        if direction == self.__down():
            if start[0]<=0 or self.__world[start[0]-1][start[1]][0]=='F':
                return True
        if direction == self.__right():
            if start[1]>=self.__sizeX or self.__world[start[0]][start[1]+1][0]=='F':
                return True
        return False
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
        # print(len(self.__testArray))
        self.__world=np.zeros((self.__sizeY,self.__sizeX))
        for x in range(0,self.__sizeX):
            for y in range(0,self.__sizeY):
                self.__world[y][x][1]=random.randint(0,50)+x+y
        return
    
    def showMap(self):
        for i in range(len(self.__world)-1,-1,-1):
            print(self.__world[i])


    def getPrice(self,start, direction=None):
        if direction == self.__up():
           return self.__world[start[0]+1][start[1]][2]
        if direction == self.__left():
            return self.__world[start[0]][start[1]-1][2]
        if direction == self.__down():
            return self.__world[start[0]-1][start[1]][2]
        if direction == self.__right():
            return self.__world[start[0]][start[1]+1][2]
        if direction ==None:
            return self.__world[start[0]][start[1]][2]
    def getVal(self,start, direction=None):
        
        if direction == self.__up():
        #    print(self.__world[start[0]+1][start[1]][1])
           return self.__world[start[0]+1][start[1]][1]
        if direction == self.__left():
            return self.__world[start[0]][start[1]-1][1]
        if direction == self.__down():
            return self.__world[start[0]-1][start[1]][1]
        if direction == self.__right():
            return self.__world[start[0]][start[1]+1][1]
        if direction ==None:
            return self.__world[start[0]][start[1]][1]
    def __returnDirect(self,directLetter):
        # print()
        # print(d)
        if len(directLetter)>1 or not isinstance(directLetter,str):
            print("wartosci nie ma w zbiorze '^','>','v','<' ")
            sys.exit(1)
        # print(directLetter)
        # print(type(directLetter))
        ind = self.__directions.index(directLetter)
        if ind == 0:
            left = 3
        else: 
            left=ind-1
        if ind == 3:
            right = 0
        else:
            right = ind+1
        return (ind, left, right, (ind+2)%4)
    
    def proceedMDP(self):
        tmpList=[]
        tmpWorld=copy.deepcopy(self.__world)
        p=[self.__p1,self.__p2,self.__p3,1-self.__p1-self.__p2-self.__p3]
        for x in range(0, self.__sizeX+1):
            for y in range(0,self.__sizeY+1):
                tmpList.clear()
                # print([x,y])
                for i in self.__directions:
                    dir = self.__returnDirect(i)
                    # print(dir)
                    if self.__world[y][x][0]!='T' and self.__world[y][x][0]!='F':
                        val=0
                        
                        for j in range(0, len(dir)):
                            if self.ifBump([y,x],self.__directions[dir[j]]):
                                # print(y,x)
                                val += p[j]*self.getVal([y,x])
                            else:
                                val+=p[j]*self.getVal([y,x],direction=self.__directions[dir[j]])
                                

                        tmpList.append((self.__G*val,i))
                if self.__world[y][x][0]!='T' and self.__world[y][x][0]!='F':
                    tmpWorld[y][x][1]=max(tmpList,key=lambda item:item[0])[0]+self.getPrice([y,x])
                    # self.__policy[y][x]=max(tmpList,key=lambda item:item[0])
        for x in range(0, self.__sizeX+1):
            for y in range(0,self.__sizeY+1):
                if self.__world[y][x][0]!='T' and tmpWorld[y][x][0]!='F':
                    if abs(self.__world[y][x][1]-tmpWorld[y][x][1])>0.0001:
                        #
                        break
                    else:
                        self.__world=copy.deepcopy(tmpWorld)
                        return False
                else:
                    break
        self.__world=copy.deepcopy(tmpWorld)
        return True
    def showPolicy(self):
        for x in range(0,self.__sizeX+1):
            for y in range(0,self.__sizeY+1):
                if  (self.__world[y][x][0]!='F' and self.__world[y][x][0]!='T'):    
                   self.__policy[y][x]=self.getBestPolicy([y,x])
                else:
                    self.__policy[y][x]=' '
        for y in range(self.__sizeY,-1,-1 ):                
                    print(self.__policy[y])
#####################################################################################
#######################     TEST
#####################################################################################
    def getBestPolicy(self,start):
        valList=[] # ('^','>','v','<') 
        p = (self.__p1,self.__p3,self.__p3,1-self.__p1-self.__p2-self.__p3)
        for i in self.__directions:
            tmpVal=0
            a=False 
            dir = self.__returnDirect(i)
            for d in range(0,len(dir)):
                a=self.ifBump(start, self.__directions[dir[d]])    
                if a:
                    tmpVal+=p[d]*self.getVal(start)
                else:
                    tmpVal+=p[d]*self.getVal(start,self.__directions[dir[d]])
            valList.append((tmpVal,i))
        # print(valList)
        # print()
        a=max(valList,key=lambda item:item[0])[1]
        # print(a)

        return a
        

    def showUt(self):
        for y in range(self.__sizeY,-1,-1):
            print('[',end='')
            for x in range(0,self.__sizeX+1):
                if  (self.__world[y][x][0]!='F' and self.__world[y][x][0]!='T'):
                    print(format( self.__world[y][x][1],'.4f'), end=' ')
                else:
                    print('  ', self.__world[y][x][0],' ',end=' ')
            print(']')
    def writeWorldToFile(self):
        for y in range(0,self.__sizeY):
            for x in range (0,self.__sizeX):
                a=1
print(sys.argv)
print()
w=World(filename='./worlds/w4x3-0.data')
counter=0
while    w.proceedMDP():
    # print(1)
    counter+=1



# print(counter)
# w.proceedMDP()
# w.showMap()
# print()
# print()
# w.proceedMDP()
# w.showMap()
# # print()
# # print()
# # w.proceedMDP()
w.showUt()
print()
print()
w.showPolicy()
# w.loadExampleWorld()
# w.showMap()