from world import World
import sys
import random
class Agent():

    def __init__(self, worldKind):

        self.__diretcions=('U','R','D','L')    
        if isinstance(worldKind,World):
            self.__worldMDP=World()
        else:
            print("zzla inicjalizacja agenta, wymagany obiekt klasy World")
            # sys.exit()
        self.__p1,self.__p2,self.__p3= 0.4,0.2,0.2 
        # self.__posX, self.__posY = self.__worldMDP.GetstartPosition()
        self.__posX=0
        self.__posY=0        

        self.f,self.l,self.r,self.b=0,0,0,0
    def printse(self):
        print('forward:', self.f)
        print('left:', self.l)
        print('right:', self.r)
        print('backward:', self.b)
    def __returnDirect(self,directLetter):
        # print()
        # print(d)
        if len(directLetter)>1 or not isinstance(directLetter,str):
            print("wartosci nie ma w zbiorze 'U','R','D','L' ")
            sys.exit(1)
        ind = self.__diretcions.index(directLetter.upper())
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
        if choice=='U':
            self.__posY+=self.__posY
        elif choice=='D':
            self.__posY-=self.__posY
        elif choice=='R':
            self.__posX+=self.__posX
        elif choice=='L':
            self.__posX-=self.__posX
    def makeAction(self,choice):
        forward,left,right,backward = self.__returnDirect(choice)
        action = random.random()
        if action<self.__p1:
            self.__action(self.__diretcions[forward])
            # print('went forward')
            self.f+=1
        elif action<self.__p1+self.__p2 and action>self.__p1:
            self.__action(self.__diretcions[left])
            # print('went left')
            self.l+=1
        elif action<self.__p1+self.__p2+self.__p3 and action>self.__p1+self.__p2:
            self.__action(self.__diretcions[right])
            # print('went right')
            self.r+=1
        else:
            self.__action(self.__diretcions[backward])
            # print('went back')
            self.b+=1
            

    def proceed_MDP(self):
        return
    def proceed_RL(self):
        return
    




a=Agent(1)
diretcions=('U','R','D','L') 
for i in range(0,10000):
    a.makeAction(diretcions[i%4])

a.printse()