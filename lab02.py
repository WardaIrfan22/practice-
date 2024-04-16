
import time
from tkinter import *
from pynput.keyboard import Key, Listener
from playsound import playsound
#-----------------------------------    

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

#-----------------------------------    

class GameObject:    
    def __init__(self, pos, vel):
        self.position=Vector(pos[0],pos[1])
        self.velocity=Vector(vel[0],vel[1])
    
    def isCollidingWith(self, otherGameObject):  # Checks collosion between itself
        #############################            #   and another game object. Returns
        rect1_left=self.position.x 
        rect1_right=self.position.x
        rect1_bottom=self.position.y
        rect1_top=self.position.y
        rect2_left=otherGameObject.position.x 
        rect2_right=otherGameObject.position.x
        rect2_bottom=otherGameObject.position.y
        rect2_top=otherGameObject.position.y
        if rect1_right>=rect2_left and rect1_left<=rect2_right and rect1_bottom>=rect2_top and rect1_top<=rect2_bottom:
            return True
        else:
            return False
                  #   True if they are colliding,                               #   False otherwise.
        #############################
    
    def Draw(self):                    # This function MUST be overidden by all 
        raise NotImplemented           #   sub-classes !!!
    
    def Update(self):                  # This function MUST be overidden by all 
        raise NotImplemented           #   sub-classes !!!

#-----------------------------------

class Background(GameObject):
    def __init__(self):
        #############################
        self.img=PhotoImage(file='assets/bg.gif')
        #############################
    
    def Draw(self):
        #############################
        Game.canvas.create_image(320,240,image=self.img)
        #############################
        
    def Update(self):
        return None
        

#-----------------------------------
    
class Brick(GameObject):
    def __init__(self, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        GameObject.__init__(self, pos, vel)
        #############################


class NormalBrick(Brick):
    def __init__(self, pos, vel):
        #############################
        Brick.__init__(self,pos,vel)
        self.img=PhotoImage(file="assets/normalbrick.gif")
        #############################
    
    def Draw(self):
        #############################
        Game.canvas.create_image(self.position.x,self.position.y,image=self.img)
        #############################
        
    def Update(self):
        return None
    
class MetalBrick(Brick):
    def __init__(self, pos, vel):
        #############################
        Brick.__init__(self,pos,vel)
        self.img=PhotoImage(file="assets/metalbrick.gif")
        #############################
    
    def Draw(self):
        #############################
        Game.canvas.create_image(self.position.x,self.position.y,image=self.img)
        #############################
        
    def Update(self):
        return None
    #############################
    #   INSERT YOUR CODE HERE
    #############################

    
class ExplodingBrick(Brick):
    #############################
    def __init__(self, pos, vel):
        #############################
        Brick.__init__(self,pos,vel)
        self.img=PhotoImage(file="assets/explodingbrick.gif")
        #############################
    
    def Draw(self):
        #############################
        Game.canvas.create_image(self.position.x,self.position.y,image=self.img)
        #############################
        
    def Update(self):
        return None
    #   INSERT YOUR CODE HERE
    #############################


#-----------------------------------
    
class Ball(GameObject):
    MAX_VX = 4
    MAX_VY = 4
    def __init__(self, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        # Call the super class constructor
        GameObject.__init__(self,pos,vel)
        self.img=PhotoImage(file="assets/ballBlue.png")
        #############################


    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        Game.canvas.create_image(self.position.x,self.position.y)
        #############################

    def Update(self):
        #############################
        self.position.x+=self.velocity.x
        self.position.y+=self.velocity.y
        if (self.position.x>=640):
            self.position.x=640
            self.velocity.x=-Ball.MAX_VX
        if (self.position.x<0):
            self.position.x=0
            self.velocity.x=Ball.MAX_VX
        if self.position.y>=480:
            self.position.y=480
            self.velocity.y=-self.velocity.y
        elif self.position.y<=0:
            self.position.y=0
            self.velocity.y=-self.velocity.y


        #############################


    
#-----------------------------------

class Powerup(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
class Life(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################

    
class FastPaddle(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################


class CrazyBall(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    pass
    #############################


#-----------------------------------

class Player(GameObject):
    MAX_VX = 10
    def __init__(self, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        # Call the super class constructor
        super().__init__(pos,vel)
        self.img=PhotoImage(file="assets/paddleBlue.gif")
        pass
        #############################


    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        Game.canvas.create_image(self.position.x,self.position.y,image=self.img)
        #############################

    def Update(self):
        #############################
        #   INSERT YOUR CODE HERE
        self.position.x+=self.velocity.x
        self.position.y+=self.velocity.y
        if (self.position.x+self.img.width()/2>=640):
            self.position.x=640-self.img.width()/2
        if self.position.x-self.img.width()/2<=0:
            self.position.x=self.
    
        #############################
    
#-----------------------------------

class Game:
    canvas = None
    def __init__(self, canvas):
        Game.canvas = canvas           # Save canvas for future use
        self.gameObjects = [] 
        self.background=Background()  
        self.ball=Ball((320,420),(Ball.MAX_VX,-Ball.MAX_VY)) 
        self.gameObjects.append(self.background)
        self.player=Player((320,450),(0,0))
        self.gameObjects.append(self.player)
        self.gameObjects.append(self.ball) 
        for i in range(5):
            for j in range(10):
                bricks=NormalBrick((50*j,20*i),(0,0))
                self.gameObjects.append(bricks)
        for i in range(5):
            for j in range(10):
                bricks1=MetalBrick((50*j,20*i),(0,0))
                self.gameObjects.append(bricks1)
        for i in range(5):
            for j in range(10):
                bricks2=ExplodingBrick((50*j,20*i),(0,0))
                self.gameObjects.append(bricks2)
        #############################
        #   INSERT YOUR CODE HERE
        #############################

                
    def Draw(self):                    # This function draws ALL of the things
        Game.canvas.delete(ALL)        # First clear the screen
        for obj in self.gameObjects:   # Now the objects draw THEMSELVES one by one
            obj.Draw()            
       
    def Update(self):
        for obj in self.gameObjects:
            obj.Update()            

            
    def LeftKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        self.player.velocity.x=-Player.MAX_VX

        #############################

    
    def RightKeyPressed(self):        
        #############################
        self.player.velocity.x=Player.MAX_VX
        pass
        #############################

    def LeftKeyReleased(self):
        #############################
        #   INSERT YOUR CODE HERE
        self.player.velocity.x=0

        #############################

    
    def RightKeyReleased(self):        
        #############################
        #   INSERT YOUR CODE HERE
        self.player.velocity.x=0
        #############################
        
            
#-----------------------------------


class GameWindow:
    def __init__(self):
        self.listener = Listener(on_press=self.KeyPressed, on_release=self.KeyReleased)
        self.listener.start()
        
        self.root = Tk()
        self.root.title("DSA:Lab 2 -- Breakout Game")
        self.root.geometry('640x480')

        self.canvas = Canvas(self.root, wi
    def KeyPressed(self, key):
        if key.name == 'left':
            self.game.LeftKeyPressed
            self.root.destroy()
            time.sleep(3)
            raise SystemExit(0)
            
    
    def KeyReleased(self, key):
        if key.name == 'left':
            self.game.LeftKeyReleased()
        if key.name == 'right':
            self.game.RightKeyReleased()
        
    
    def GameLoop(self):
        self.game.Update()
        self.game.Draw()
        self.root.after(1000//60, self.GameLoop)
#-----------------------------------

#"my name is warda and this is subbranch code"
#whats the diff
```python  
def subtract(a,b):
    return a-b
```
1. first item 
    1. first item 
    2. second item 
2. second item 
    1. first item 
    2. second item 
    #nsme warda 
    