# from world import World
import sys
import random
class Agent():

    def __init__(self,x,y,start, fileName=None):

        self.__directions=('^','>','v','<')    
        self.__posX=start[0]
        self.__posY=start[1]        
        self.__sizeWx=x      
        self.__sizeWy=y
        self.f,self.l,self.r,self.b=0,0,0,0
        self.__qmatrix=[]
    def printDir(self):
        print('forward:', self.f)
        print('left:', self.l)
        print('right:', self.r)
        print('backward:', self.b)
    def __returnDirect(self,directLetter):
        # print()
        # print(d)
        if len(directLetter)>1 or not isinstance(directLetter,str):
            print("wartosci nie ma w zbiorze '^','>','v','<' ")
            sys.exit(1)
        ind = self.__directions.index(directLetter.upper())
        if ind == 0:
            left = 3
        else: 
            left=ind-1
        if ind == 3:
            right = 0
        else:
            right = ind+1
        return ind, left, right, (ind+2)%4

    def __action(self, choice):
        if choice=='^':
            self.__posY+=self.__posY
        elif choice=='v':
            self.__posY-=self.__posY
        elif choice=='>':
            self.__posX+=self.__posX
        elif choice=='<':
            self.__posX-=self.__posX
    def makeAction(self,choice):
        forward,left,right,backward = self.__returnDirect(choice)
        action = random.random()
        if action<self.__p1:
            self.__action(self.__directions[forward])
            # print('went forward')
            self.f+=1
        elif action<self.__p1+self.__p2 and action>self.__p1:
            self.__action(self.__directions[left])
            # print('went left')
            self.l+=1
        elif action<self.__p1+self.__p2+self.__p3 and action>self.__p1+self.__p2:
            self.__action(self.__directions[right])
            # print('went right')
            self.r+=1
        else:
            self.__action(self.__directions[backward])
            # print('went back')
            self.b+=1
            

    def proceed_MDP(self, iter):
        for i in range(0,30):
            a=1
    def proceed_RL(self):
        return
    




# a=Agent(1)
# directions=('^','>','v','<') 
# for i in range(0,10000):
#     a.makeAction(directions[i%4])

# a.printse()