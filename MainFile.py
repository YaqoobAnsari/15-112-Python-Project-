#===============================================================================================================
#===============================================================================================================
# Done By : Yaqoob Ansari
# AndrewID : yansari@andrew.cmu.edu

import pygame
import random
import time
import math

pygame.init()
#===============================================================================================================
#===============================================================================================================

window_width=1400
window_height=704

# Open a window
size = (window_width, window_height)
win = pygame.display.set_mode(size)

# Labeling the game window with a title.
pygame.display.set_caption("Jump Soccer")

# General declaration of variables.
clock = pygame.time.Clock()
drag = 1
elasticity = 0.75
gravity,bd = math.pi, 0.2

music = pygame.mixer.Sound('Intro.wav')
fans = pygame.mixer.Sound('Music.wav')
whistle = pygame.mixer.Sound('gamewhistle.wav')
goal = pygame.mixer.Sound('goal.wav')

# Creating a function that loads in the spirte images of all the characters.
# The sprites are of two types: User and Opponent.
# User sprites are the sprites the the user or player1 uses.
# The sprites are divided into categories of their movements.
def characterDictionary():
    # [[WALKRIGHT],[WALKLEFT],[KICK],[IDLE]
    # USERS SPRITES
    # Loading in the sprites of different characters.
    # Akame user sprites.
    A_Walkright = [pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png')]
    A_Walkleft = [pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png')]
    A_Kick = [pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png')]
    A_Idle = [pygame.image.load('A_Idle.png')]

    # Tanjiro user sprites.
    T_Walkright =[pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha()]
    T_Walkleft =[pygame.image.load('T_Moving_Step_Back.png').convert_alpha().convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha()]
    T_Kick =[pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha()]
    T_Idle = [pygame.image.load('T_Idle.png').convert_alpha()]

    # Nezuko user sprites.
    N_Walkright = [pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png')]
    N_Walkleft = [pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png')]
    N_Kick = [pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png')]
    N_Idle = [pygame.image.load('N_Idle.png')]

    # Yato user sprites.
    Y_Walkright = [pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png')]
    Y_Walkleft = [pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png')]
    Y_Kick =[pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png')]
    Y_Idle = [pygame.image.load('Y_Idle.png')]

    # Yukino user sprites.
    Yu_Walkright = [pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png')]
    Yu_Walkleft = [pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png')]
    Yu_Kick = [pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png')]
    Yu_Idle = [pygame.image.load('Yu_Idle.png')]

    # Korosensie user sprites.
    K_Walkright = [pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png')]
    K_Walkleft = [pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png')]
    K_Kick = [pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png')]
    K_Idle = [pygame.image.load('K_Idle.png')]
    
    # Declaring an empty dictionary to store all the sprites with character names as key.
    characterSprites = {}

    # Loading the sprites in the dictionary.
    characterSprites['Akame'] = [A_Walkright,A_Walkleft,A_Kick,A_Idle]
    characterSprites['Tanjiro'] = [T_Walkright,T_Walkleft,T_Kick,T_Idle]
    characterSprites['Nezuko'] = [N_Walkright,N_Walkleft,N_Kick,N_Idle]
    characterSprites['Yato'] = [Y_Walkright,Y_Walkleft,Y_Kick,Y_Idle]
    characterSprites['Yukino'] = [Yu_Walkright,Yu_Walkleft,Yu_Kick,Yu_Idle]
    characterSprites['Korosensei'] = [K_Walkright,K_Walkleft,K_Kick,K_Idle]
    
    
    # [[WALKRIGHT],[WALKLEFT],[Kick_O],[IDLE_O]
    # OPPONENTS SPRITE
    # Loading in the sprites of different characters.
    # Akame opponent sprites.
    A_Walkright_O = [pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png')]
    A_Walkleft_O = [pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png')]
    A_Kick_O = [pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png')]
    A_Idle_O = [pygame.image.load('A_Idle_O.png')]

    # Tanjiro opponent sprites.    
    T_Walkright_O =[pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png')]
    T_Walkleft_O =[pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png')]
    T_Kick_O =[pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png')]
    T_Idle_O = [pygame.image.load('T_Idle_O.png')]

    # Nezuko opponent sprites.
    N_Walkright_O = [pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png')]
    N_Walkleft_O = [pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png')]
    N_Kick_O = [pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png')]
    N_Idle_O = [pygame.image.load('N_Idle_O.png')]

    # Yato opponent sprites.
    Y_Walkright_O = [pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png')]
    Y_Walkleft_O = [pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png')]
    Y_Kick_O =[pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png')]
    Y_Idle_O = [pygame.image.load('Y_Idle_O.png')]

    # Yukino opponent sprites.
    Yu_Walkright_O = [pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png')]
    Yu_Walkleft_O = [pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png')]
    Yu_Kick_O = [pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png')]
    Yu_Idle_O = [pygame.image.load('Yu_Idle_O.png')]

    # Korosensei opponent sprites.
    K_Walkright_O = [pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png')]
    K_Walkleft_O = [pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png')]
    K_Kick_O = [pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png')]
    K_Idle_O = [pygame.image.load('K_Idle_O.png')]

    # Declaring a dictionary to store the opponent sprites.
    characterSpritesOpponent = {}

    # Loading the sprites into the dictionary.
    characterSpritesOpponent['Akame'] = [A_Walkright_O,A_Walkleft_O,A_Kick_O,A_Idle_O]
    characterSpritesOpponent['Tanjiro'] = [T_Walkright_O,T_Walkleft_O,T_Kick_O,T_Idle_O]
    characterSpritesOpponent['Nezuko'] = [N_Walkright_O,N_Walkleft_O,N_Kick_O,N_Idle_O]
    characterSpritesOpponent['Yato'] = [Y_Walkright_O,Y_Walkleft_O,Y_Kick_O,Y_Idle_O]
    characterSpritesOpponent['Yukino'] = [Yu_Walkright_O,Yu_Walkleft_O,Yu_Kick_O,Yu_Idle_O]
    characterSpritesOpponent['Korosensei'] = [K_Walkright_O,K_Walkleft_O,K_Kick_O,K_Idle_O]

    # Returining the both dictionaries as a list 
    return [characterSprites,characterSpritesOpponent]

allCharactersSprites = characterDictionary()


# Creating a class that creates the game ball.
# This class also handles all types of physics related events with the ball.
# Events like collision of Player-Ball, Ball-Ball,Ball-Wall,Goals are done here.
class BallProjectile(object):

    # Creating a constructor function that initializes general variables.
    # Like ball's coordinates, its speed, a hitbox around it and the image.
    def __init__(self, ballX, ballY, ballSize,ball):
        
            self.ballcorX = ballX
            self.ballcorY = ballY
            self.sizeOfBall = ballSize
            self.angleCreated = 0
            self.ballvelocity = 20
            self.ball = ball
            self.hitboxB = (self.ballcorX,self.ballcorY,self.sizeOfBall,self.sizeOfBall)


    # Creating a functions that computes collisons of the Ball and the goal post.
    # The left goal post.
    def LeftGoalpostColl(self,leftgoalposthitbox):

            # Creatinng a hitbox around the ball.
            ballHitBox = pygame.draw.rect(win,(255,0,0),(self.ballcorX,self.ballcorY,self.sizeOfBall-15,self.sizeOfBall-15),2)

            # Checking if the hitboxes collide, return True if yes.
            if leftgoalposthitbox.colliderect(ballHitBox):
                    return True

    # Creating a functions that computes collisons of the Ball and the goal post.
    # The Right goal post.
    def RightGoalpostColl(self,rightgoalposthitbox):

            # Creatinng a hitbox around the ball.
            ballHitBox = pygame.draw.rect(win,(255,0,0),(self.ballcorX,self.ballcorY,self.sizeOfBall-15,self.sizeOfBall-15),2)

            # Checking if the hitboxes collide, return True if yes.
            if rightgoalposthitbox.colliderect(ballHitBox):
                
                    return True
                

    # Creating a function that checks if a goal is scored.
    # In the left goal.
    def LeftGoalScored(self,LeftGoalXcor,LeftGoalYcor):

            # Checking if the ball is inside the goal by checking coordinates.
            if self.ballcorX <= 110:
                if self.ballcorY > LeftGoalYcor and self.ballcorY + self.sizeOfBall > LeftGoalYcor:

                    # Resetting the ball's coordinates to initial game setup
                    # Putting the ball back at the center.
                    self.ballcorX = 658
                    self.ballcorY = 200
                    self.angleCreated = 0
                    self.ballvelocity = 20
                    
                    return True

    # Creating a function that checks if a goal is scored.
    # In the right goal.
    def RightGoalScored(self,RightGoalXcor,RightGoalYcor):

            # Checking if the ball is inside the goal by checking coordinates.
            if self.ballcorX + self.sizeOfBall > RightGoalXcor and self.ballcorX < RightGoalXcor:
                    if self.ballcorY > RightGoalYcor and self.ballcorY + self.sizeOfBall > RightGoalYcor:

                            # Resetting the ball's coordinates to initial game setup
                            # Putting the ball back at the center.
                            self.ballcorX = 658
                            self.ballcorY = 200
                            self.angleCreated = 0
                            self.ballvelocity = 20
                            
                            return True

    # Creating a function that checks and deals with collision between ball and goal posts.
    def BallAndGoalColl(self,GoalBoxLeft,GoalBoxRight,WidthOfGoal,HeigthOfGoal):

            # Creatinng a hitbox around the ball.
            ballRect = pygame.draw.rect(win,(255,0,0),(self.ballcorX,self.ballcorY,self.sizeOfBall-15,self.sizeOfBall-15),2)

            # Creating hitboxes around the goal posts.
            # Checking if the hitboxes of the ball and the posts cross.
            # For left goal post.
            if GoalBoxLeft.colliderect(ballRect):  
                if self.ballcorY > HeigthOfGoal:
                    
                    self.ballcorX = 2*self.sizeOfBall - self.ballcorX
                    self.angleCreated = - self.angleCreated
                    self.ballvelocity *= elasticity

                if self.ballcorY <= HeigthOfGoal:
                    
                    self.ballcorY = 2*(HeigthOfGoal - self.sizeOfBall) - self.ballcorY
                    self.angleCreated = math.pi - self.angleCreated
                    self.ballvelocity *= elasticity

            # Creating hitboxes around the goal posts.
            # Checking if the hitboxes of the ball and the posts cross.
            # For right goal post.
            if GoalBoxRight.colliderect(ballRect):
                    if self.ballcorY > HeigthOfGoal:
                        
                            self.ballcorX = 2*((window_width-WidthOfGoal) - self.sizeOfBall) - self.ballcorX
                            self.angleCreated = - self.angleCreated
                            self.ballvelocity *= elasticity

                    if self.ballcorY <= HeigthOfGoal:
                        
                            self.ballcorY = 2*(HeigthOfGoal - self.sizeOfBall) - self.ballcorY
                            self.angleCreated = math.pi - self.angleCreated
                            self.ballvelocity *= elasticity

    
    # Creating a function that deals with Ball and Wall collisions.
    def BallAndWallColl(self):

            # Right wall collisions are handled here.
            if self.ballcorX > 1500 - self.sizeOfBall:
                
                    self.ballcorX = 2*(1200 - self.sizeOfBall) - self.ballcorX
                    self.angleCreated = - self.angleCreated
                    self.ballvelocity *= elasticity

            # Left wall collisions are handled here.
            elif self.ballcorX < self.sizeOfBall:
                
                    self.ballcorX = 2*self.sizeOfBall - self.ballcorX
                    self.angleCreated = - self.angleCreated
                    self.ballvelocity *= elasticity

            # Bottom wall collisions are handled here.
            if self.ballcorY > 550 - self.sizeOfBall:
                
                    self.ballcorY = 2*(550 - self.sizeOfBall) - self.ballcorY
                    self.angleCreated = math.pi - self.angleCreated
                    self.ballvelocity *= elasticity

            # Top wall collisions are handled here.
            elif self.ballcorY < self.sizeOfBall:
                
                    self.ballcorY = 2*self.sizeOfBall - self.ballcorY
                    self.angleCreated = math.pi - self.angleCreated
                    self.ballvelocity *= elasticity
                

    # Creating a function that checks for Ball and Player Collisions.
    # For Left Player.
    def PlayerOneBallColl(self,PlayerXcor,PlayerYcor,playerVel):
        
            dx = PlayerXcor - self.ballcorX
            dy = PlayerYcor - self.ballcorY
            
            tangent = math.atan2(dy,dx)
            self.angleCreated = 0.5 * math.pi + tangent
            angle1 = 2 * tangent - self.angleCreated
            angle2 = 2 * tangent - self.angleCreated
            
            speed1 = playerVel + self.ballvelocity
            speed2 = playerVel + self.ballvelocity
            
            (self.angleCreated, self.ballvelocity) = (angle1, speed1)
            (self.angleCreated, self.ballvelocity) = (angle2, speed2)
            self.ballcorX += math.sin(self.angleCreated)
            self.ballcorY -= math.cos(self.angleCreated)

    # Creating a function that checks for ball and player Collisions.
    # For Right Player.
    def PlayerTwoBallColl(self,PlayerXcor,PlayerYcor,playerVel):
        
            dx = PlayerXcor - self.ballcorX
            dy = PlayerYcor - self.ballcorY
            
            tangent = math.atan2(dy,dx)
            self.angleCreated = 0.5 * math.pi + tangent
            angle1 = 2 * tangent - self.angleCreated
            angle2 = 2 * tangent - self.angleCreated
            
            speed1 = playerVel + self.ballvelocity
            speed2 = playerVel + self.ballvelocity
            
            (self.angleCreated, self.ballvelocity) = (angle1, speed1)
            (self.angleCreated, self.ballvelocity) = (angle2, speed2)
            self.ballcorX += math.sin(self.angleCreated)
            self.ballcorY -= math.cos(self.angleCreated)


    # Creating a function that displays the ball on the screen.
    def blitBall(self):

            # Blitting the ball on the screen at the ball's coordinates.           
            win.blit(self.ball,[self.ballcorX,self.ballcorY])

    # Creating a function that deals with   ball movement. 
    def calcBallMovements(self):
        
            (self.angleCreated, self.ballvelocity) = BallAngleAndVeloctiyCalc(self.angleCreated, self.ballvelocity, gravity,bd)
            
            self.ballcorX += math.sin(self.angleCreated) * self.ballvelocity
            self.ballcorY -= math.cos(self.angleCreated) * self.ballvelocity

            # This functions adds the air resistance to help form the projectile motion.
            self.ballvelocity *= drag
            

# Creating a function that deals with calculation of all the angles and resistances.
def BallAngleAndVeloctiyCalc(angle1, length1, angle2, length2):
    
	x = math.sin(angle1) * length1 + math.sin(angle2) * length2
	y = math.cos(angle1) * length1 + math.cos(angle2) * length2
	
	angle = 0.5 * math.pi - math.atan2(y, x)
	length  = math.hypot(x, y)
	
	return (angle, length)
    
###################################################    START OF ARCADE PART OF CODE #################################################################
###################################################################################################################################################

# Creating a class that creates a player for the SinglePlayer part of the game.
class singlePlayer(object):
    def __init__(self,x,y,width,height,opponent,ch,bg):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.kick = False
        self.right = False
        self.Opponent = opponent
        self.walkCount = 0
        self.character = ch
        self.std = bg
        self.hitbox = (self.x,self.y+25,185,190)
        self.jumpCount = 10

    # Defining a function that redraws the player every looprun at the updated coordinates of the player.
    def draw(self, win):
        # Checking if the player is the user or the Computer(Opponent).
        # This is done to blit appropriate sprites (user sprites) from the dictionaries.
        if self.Opponent == 0:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
                
            # If user had pressed Left Arrow Key:
            if self.left:
                win.blit(allCharactersSprites[0][self.character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1

            # If user had pressed Right Arrow Key:    
            elif self.right:
                win.blit(allCharactersSprites[0][self.character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            # If user had pressed Space Key:
            elif self.kick:
                win.blit(allCharactersSprites[0][self.character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                

            # If user had pressed no key, blitting the same position up:
            else:
                win.blit(allCharactersSprites[0][self.character][3][0], (self.x,self.y))

            self.hitbox = (self.x,self.y+25,185,190)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            
        # Checking if the player is the user or the Computer(Opponent).
        # This is done to blit appropriate sprites (user sprites) from the dictionaries.
        if self.Opponent == 1:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[1][self.character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[1][self.character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[1][self.character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                 
                
            else:
                win.blit(allCharactersSprites[1][self.character][3][0], (self.x,self.y))
            self.hitbox = (self.x,self.y+25,185,190)

    # Declaring a function that blits the stadium image of the game.         
    def drawstadium(self,win):
        win.blit(self.std, (0,0))

# Declaring a timer counter.
def timedisplay(count):
    white = [255,255,255]
    smallfont = pygame.font.SysFont('Courier',50)
    
    

############################################
######################################
##########################################
##############################
# Declaring a funtion that redraws component of the game screen.
def redrawGameWindow(man,player2,count,PlayerOneGoals,PlayerTwoGoals,ballobj):
    
    white = [255,255,255]
    
    # Loading the ball.
    ballimage = pygame.image.load('balln.png')

    # Drawing hitboxes around goalposts.
    GoalBoxLeft = pygame.draw.rect(win,(255,0,0),(0,170,170,25),2)
    GoalBoxRight = pygame.draw.rect(win,(255,0,0),(1320,170,170,25),2)

    # Drawing hitboxes around the players.
    rect1 = pygame.draw.rect(win,(255,0,0),man.hitbox,2)
    rect2 = pygame.draw.rect(win,(255,0,0),player2.hitbox,2)

    # Loading the 'Vs' image.
    vs = pygame.image.load('vs.png')

    # Loading in the fonts.
    smallfont = pygame.font.SysFont('Courier',30)
    smallfont = pygame.font.SysFont('comsicsaans',50)

    # Rendering in texts to display.
    Player1 = smallfont.render(man.character,True,white)
    Player2 = smallfont.render(player2.character,True,white)
    time = smallfont.render(str(int(count//16)),True,white)
    player1score= smallfont.render(str(PlayerOneGoals),True,white)
    colon = smallfont.render(':',True,white)
    player2score= smallfont.render(str(PlayerTwoGoals),True,white)

    # here we apply the collision function and call the collide function 
    # accordingly
    isCollided = ballobj.LeftGoalpostColl(rect1)
    if isCollided:
            ballobj.PlayerOneBallColl(man.x,man.y,man.vel)
            #BallProjectile.PlayerTwoBallColl(leadX1,leadY1,leadXChange1)

    isCollided2 = ballobj.RightGoalpostColl(rect2)
    if isCollided2:
            ballobj.PlayerOneBallColl(player2.x,player2.y,player2.vel)
            #BallProjectile.PlayerTwoBallColl(leadX2,leadY2,leadXChange2)

    # Function that checks for collison between goalposts and ball.
    ballobj.BallAndGoalColl(GoalBoxLeft,GoalBoxRight,170,400)

    # Calling function that redraws stadium.
    man.drawstadium(win)

    # Blitting player images,all the other images and the texts.
    win.blit(Player1,(330,10))
    win.blit(Player2,(800,10))   
    win.blit(vs,(600,-10))
    win.blit(time,(655,88))
    win.blit(player1score,(640,153))
    win.blit(colon,(665,150))
    win.blit(player2score,(685,153))

    # Calling function to draw the players.
    man.draw(win)
    player2.draw(win)

    # Calling functions that blits the ball.
    ballobj.blitBall()
    ballobj.calcBallMovements()#width,height
    
    ballobj.BallAndWallColl()
    pygame.display.update()


#Mainloop for the SinglePlayerGame.
def singlePlayerGame(bg,c1,c2,gameround,difficulty):
        
   
    count = 0
    
    PlayerOneGoals=0
    PlayerTwoGoals=0

    aicount = 1
    
    # Starting the game music.
    #whistlesound.play()
    whistle.play()
    fans.play()
    #pygame.mixer.music.play(-1)
    

    # Creating two players as objects of SinglePlayer Class.
    man = multiplayer(200,345, 64,64,0,c1,bg)
    player2 = multiplayer(1000,345,64,64,1,c2,bg)

    # Creating the object of Ball class.
    ballimage = pygame.image.load('finalball.png')
    ballobj = BallProjectile(658,200,100,ballimage)

    
    run = True
    # Running the main game loop for 120 game seconds.
    while run and count < 16*120:

        
        clock.tick(27)
        count += 1

        # Check if an event has occured.
        for event in pygame.event.get():

            # Quits the game if the cross button is pressed.
            if event.type == pygame.QUIT:
                run = False

        # Finding if any keyboard key is pressed.
        keys = pygame.key.get_pressed()

        # If the Left Key is pressed.
        # Updating the player coordinates accordingly.
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            
        # If the Right Key is pressed.
        # Updating the player coordinates accordingly.   
        elif keys[pygame.K_RIGHT] and man.x < window_width - man.width - man.vel-130 and man.hitbox[0]+185 < player2.hitbox[0]:
            man.x += man.vel
            man.right = True
            man.left = False
            
        # If the Space Key is pressed.
        # Updating the player coordinates accordingly.    
        elif keys[pygame.K_SPACE]:
            man.right = False
            man.left = False
            man.kick = True

        # No key is pressed.
        else:
            man.right = False
            man.left = False
            man.walkCount = 0

        # If Space Key is pressed.
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
                
        # Using a polynomial equation to plot the graph of the jump.
        else:
            if man.jumpCount >= -10:
                neg = 1
                
                if man.jumpCount < 0:
                    neg = -1

                # The polynomial equation.
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
                
            else:
                man.isJump = False
                man.jumpCount = 10

        ####################################################
                
        #Checking if the computer is in the range of 950 and 1200
        #Making a randomly increasing variable that when is divisible by 3
        #initiates the player to jump..making the jump random during its
        #patrol like movements.

        if difficulty == "Hard":
            #print('hard')
            # Checking if a number divisible by 3 is found.
            if  (ballobj.ballcorX > 1000 and ballobj.ballcorY < 1200 and ballobj.ballcorY < player2.y):

                    # Making the player jump.
                    player2.isJump = True
                    player2.left = False
                    player2.right = False
                    #pygame.time.delay(100)

                    #if not(player2.isJump):
                        

            # If not, then the  player keeps on patrolling.         
            else:
                player2.x -= player2.vel
            
                aicount += 1
                if player2.x == 950:
                        player2.vel *= -1
                        player2.left = True
                        player2.right = False
                        player2.isJump = False

                        # Increaisng the number randomly.
                        aicount += random.randint(2,5)
                        
                if player2.x == 1200:
                        
                        player2.vel *= -1
                        player2.left = False
                        player2.right = True
                        player2.isJump = False

        
        if difficulty == "Easy" or difficulty == 'Normal':
            #print('Easy Normal')
            player2.x -= player2.vel
        
            aicount += 1
            if player2.x == 950:
                    player2.vel *= -1
                    player2.left = True
                    player2.right = False
                    player2.isJump = False

                    # Increaisng the number randomly.
                    aicount += random.randint(2,5)
                    
            if player2.x == 1200:
                    
                    player2.vel *= -1
                    player2.left = False
                    player2.right = True
                    player2.isJump = False

      
        if player2.isJump:
            if player2.jumpCount >= -10:
                neg = 1
                
                if player2.jumpCount < 0:
                    neg = -1

                # The polynomial equation.    
                player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
                player2.jumpCount -= 1
                
            else:
                player2.isJump = False
                player2.jumpCount = 10
                        
                        
        
        
                
        # Checking if a goal is scored.
        # If the left goal is scored.
        if(ballobj.LeftGoalScored(0,170)):

            # Relocating the player to th.e initial positions.
            whistle.play()
            goal.play()
            PlayerTwoGoals += 1
            
            man.x = 200
            man.y = 345
            player2.x = 1000
            player2.y = 345

            

        # Checking if a goal is scored.
        # If the Right goal is scored.    
        if(ballobj.RightGoalScored(1320,170)):
                

            # Relocating the player to the initial positions.
            whistle.play()
            goal.play()
            PlayerOneGoals += 1
            
            man.x = 200
            man.y = 345
            player2.x = 1000
            player2.y = 345
            
        if  not man.isJump:
            man.y = 345
            
        if not player2.isJump:
            player2.y = 345

        #Calling the function to redraw the game window.
        redrawGameWindow(man,player2,count,PlayerOneGoals,PlayerTwoGoals,ballobj)

    # End of one set whistle.
    whistle.play()

    # Display the Gameover screen if the gameround is 2.
    if gameround%2 == 0:
        winnercalculator(PlayerOneGoals,PlayerTwoGoals)


    



###################################################    END OF ARCADE PART OF CODE #################################################################
###################################################################################################################################################

###################################################    FRIENDS OF ARCADE PART OF CODE #################################################################
###################################################################################################################################################

# Creating a class that creates a player for the MultiPlayer part of the game.
class multiplayer(object):
    def __init__(self,x,y,width,height,opponent,ch,bg):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.kick = False
        self.right = False
        self.Opponent = opponent
        self.walkCount = 0
        self.character = ch
        self.std = bg
        self.jumpCount = 10
        self.hitbox = (self.x,self.y+25,185,190)

    def draw(self, win):
        if self.Opponent == 0:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[0][self.character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[0][self.character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[0][self.character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                pygame.time.delay(100)
                
            else:
                win.blit(allCharactersSprites[0][self.character][3][0], (self.x,self.y))

            self.hitbox = (self.x,self.y+25,185,190)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        if self.Opponent == 1:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[1][self.character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[1][self.character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[1][self.character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                
            else:
                win.blit(allCharactersSprites[1][self.character][3][0], (self.x,self.y))

            self.hitbox = (self.x,self.y+25,185,190)
            #spygame.draw.rect(win,(255,0,0),self.hitbox,2)
    def drawstadium(self,win):
        win.blit(self.std, (0,0))

############################################
######################################
##########################################
###############################

# Declaring a timer counter.
def timedisplay(count):
    white = [255,255,255]
    smallfont = pygame.font.SysFont('Courier',50)
    

############################################
######################################
##########################################
###############################

# Declaring a funtion that redraws component of the game screen.
def redrawGameWindow(man,player2,count,PlayerOneGoals,PlayerTwoGoals,ballobj):
    
    white = [255,255,255]
    
    # Loading the ball.
    ballimage = pygame.image.load('balln.png')

    # Drawing hitboxes around goalposts.
    GoalBoxLeft = pygame.draw.rect(win,(255,0,0),(0,170,170,25),2)
    GoalBoxRight = pygame.draw.rect(win,(255,0,0),(1320,170,170,25),2)

    # Drawing hitboxes around the players.
    rect1 = pygame.draw.rect(win,(255,0,0),man.hitbox,2)
    rect2 = pygame.draw.rect(win,(255,0,0),player2.hitbox,2)

    # Loading the 'Vs' image.
    vs = pygame.image.load('vs.png')

    # Loading in the fonts.
    smallfont = pygame.font.SysFont('Courier',30)
    smallfont = pygame.font.SysFont('comsicsaans',50)

    # Rendering in texts to display.
    Player1 = smallfont.render(man.character,True,white)
    Player2 = smallfont.render(player2.character,True,white)
    time = smallfont.render(str(int(count//16)),True,white)
    player1score= smallfont.render(str(PlayerOneGoals),True,white)
    colon = smallfont.render(':',True,white)
    player2score= smallfont.render(str(PlayerTwoGoals),True,white)

    # here we apply the collision function and call the collide function 
    # accordingly
    isCollided = ballobj.LeftGoalpostColl(rect1)
    if isCollided:
            ballobj.PlayerOneBallColl(man.x,man.y,man.vel)
            #BallProjectile.PlayerTwoBallColl(leadX1,leadY1,leadXChange1)

    isCollided2 = ballobj.RightGoalpostColl(rect2)
    if isCollided2:
            ballobj.PlayerOneBallColl(player2.x,player2.y,player2.vel)
            #BallProjectile.PlayerTwoBallColl(leadX2,leadY2,leadXChange2)

    # Function that checks for collison between goalposts and ball.
    ballobj.BallAndGoalColl(GoalBoxLeft,GoalBoxRight,170,400)

    # Calling function that redraws stadium.
    man.drawstadium(win)

    # Blitting player images,all the other images and the texts.
    win.blit(Player1,(330,10))
    win.blit(Player2,(800,10))   
    win.blit(vs,(600,-10))
    win.blit(time,(655,88))
    win.blit(player1score,(640,153))
    win.blit(colon,(665,150))
    win.blit(player2score,(685,153))

    # Calling function to draw the players.
    man.draw(win)
    player2.draw(win)

    # Calling functions that blits the ball.
    ballobj.blitBall()
    ballobj.calcBallMovements()#width,height
    
    ballobj.BallAndWallColl()
    pygame.display.update()

# Mainloop for the MultiPlayerGame.
def multiplayerGame(bg,c1,c2,gameround):

   
    count = 0
    PlayerOneGoals=0
    PlayerTwoGoals=0

    # Starting the game music.
    #whistlesound.play()
    whistle.play()
    fans.play()
    #pygame.mixer.music.play(-1)
    
    man = multiplayer(200,345, 64,64,0,c1,bg)
    player2 = multiplayer(1000,345,64,64,1,c2,bg)
    
    ballimage = pygame.image.load('finalball.png')
    ballobj = BallProjectile(658,200,100,ballimage)

    
    run = True
    # Running the main game loop for 120 game seconds.
    while run and count < 16*120:

        
        clock.tick(27)
        count += 1

        # Check if an event has occured.
        for event in pygame.event.get():

            # Quits the game if the cross button is pressed.
            if event.type == pygame.QUIT:
                run = False

        # Finding if any keyboard key is pressed.
        keys = pygame.key.get_pressed()

        # If the Left Key is pressed.
        # Updating the player coordinates accordingly.
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            
        # If the Right Key is pressed.
        # Updating the player coordinates accordingly.   
        elif keys[pygame.K_RIGHT] and man.x < window_width - man.width - man.vel-130 and man.hitbox[0]+185 < player2.hitbox[0]:
            man.x += man.vel
            man.right = True
            man.left = False
            
        # If the Space Key is pressed.
        # Updating the player coordinates accordingly.    
        elif keys[pygame.K_SPACE]:
            man.right = False
            man.left = False
            man.kick = True

        # No key is pressed.
        else:
            man.right = False
            man.left = False
            man.walkCount = 0

        # If Space Key is pressed.
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
                
        # Using a polynomial equation to plot the graph of the jump.
        else:
            if man.jumpCount >= -10:
                neg = 1
                
                if man.jumpCount < 0:
                    neg = -1

                # The polynomial equation.
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
                
            else:
                man.isJump = False
                man.jumpCount = 10



        ####################################################
        # If the Left Key is pressed.
        # Updating the player coordinates accordingly.

        # If the 'A' Key is pressed.
        # Updating the player coordinates accordingly.
        if keys[pygame.K_a] and player2.x > player2.vel and player2.hitbox[0] > man.hitbox[0] + 185:
            player2.x -= player2.vel
            player2.left = True
            player2.right = False

        # If the 'D' Key is pressed.
        # Updating the player coordinates accordingly.    
        elif keys[pygame.K_d] and player2.x < window_width - player2.width - player2.vel-130 :
            player2.x += player2.vel
            player2.right = True
            player2.left = False
            
        # If the 'Q' Key is pressed.
        # Updating the player coordinates accordingly.    
        elif keys[pygame.K_q]:
            player2.right = False
            player2.left = False
            player2.kick = True

        # No key is pressed.    
        else:
            player2.right = False
            player2.left = False
            player2.walkCount = 0
            
        if not(player2.isJump):
            # If Space Key is pressed.
            if keys[pygame.K_w]:
                player2.isJump = True
                player2.right = False
                player2.left = False
                player2.walkCount = 0
                
        # Using a polynomial equation to plot the graph of the jump.        
        else:
            if player2.jumpCount >= -10:
                neg = 1
                
                if player2.jumpCount < 0:
                    neg = -1

                # The polynomial equation.    
                player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
                player2.jumpCount -= 1
                
            else:
                player2.isJump = False
                player2.jumpCount = 10
        
        # Checking if a goal is scored.
        # If the left goal is scored.
        if(ballobj.LeftGoalScored(0,170)):

            # Relocating the player to the initial positions.
            whistle.play()
            goal.play()
            PlayerTwoGoals += 1
            
            man.x = 200
            man.y = 345
            player2.x = 1000
            player2.y = 345

        # Checking if a goal is scored.
        # If the Right goal is scored.    
        if(ballobj.RightGoalScored(1320,170)):

            # Relocating the player to the initial positions.
            whistle.play()
            goal.play()
            PlayerOneGoals += 1
            
            man.x = 200
            man.y = 345
            player2.x = 1000
            player2.y = 345

        if  not man.isJump:
            man.y = 345
            
        if not player2.isJump:
            player2.y = 345
        
        #Calling the function to redraw the game window.
        redrawGameWindow(man,player2,count,PlayerOneGoals,PlayerTwoGoals,ballobj)

    # End of match whistle.
    whistle.play()

    # Display the Gameover screen if the gameround is 2
    if gameround%2 == 0:
        winnercalculator(PlayerOneGoals,PlayerTwoGoals)

        


###################################################    LOADING SCREEN PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################

# Defining a fucntion that calculates the progress of the loading bar.
def loading(progress):

    # Declaring the colors to be later used.    
    green = [0,255,0]
    black = [0,0,0]
    white = [255,255,255]

    # Declaring the font.    
    smallfont = pygame.font.SysFont('Impact',30)

    # Rendering the text.
    if progress < 100:
        text = smallfont.render('Loading ' + str(int(progress)) + '%',True, green)
        
    else:
        text = smallfont.render('Loading ' + str(100) + '%',True, green)

    # Blitting the text on screen.    
    win.blit( text, (600,555))

# Making the main function that draws the loading screen.
# The function loads in a different background every game set.
def loadingbar(setnumber):

    # Loading the background pic for each half of the match.    
    bg = [pygame.image.load('bg1.jpg'),pygame.image.load('bg2.jpg')]

    # Declaring the colors to be later used. 
    green = [0,255,0]
    black = [0,0,0]
    white = [255,255,255]

    # Declaring the font. 
    smallfont = pygame.font.SysFont('Impact',30)

    progress = 0
   
    # A loop that fills the loading bar.
    # Goes 5 times over the lenght of the bars.
    while ((progress//5) < 100):
        
        # Radomly increase the percentage loaded.
        increase = random.randint(1,20)

        # Increment the progress.
        progress += increase

        # Blit the progress value on the screen.
        win.blit(bg[setnumber], (0,0))

        # Drawing the loading bar as a rectangle.
        pygame.draw.rect(win,green,(448,498,508,54))

        # Filling the bar.    
        if (progress/5) > 100:
            pygame.draw.rect(win,black,(452,502,500,46))
            
        else:
            pygame.draw.rect(win,black,(452,502,progress,46))
           
        loading(progress//5)
        pygame.display.flip()

        # Delaying the loop by some milliseconds.
        time.sleep(0.05)
    return
    

###################################################    DIFFICULTY SELECTION PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################

# Making a function that allows the user to choose the difficulty of the game.
# Creating a fixed display screen with all the buttons and options.
def fixedDifficultySetUp():

    # Loading in the buttons images.
    redSquare = [pygame.image.load('easy.png'),pygame.image.load('normal.png'),pygame.image.load('hard.png')]

    # Loading in the background image.
    bg = pygame.image.load('difbackground.jpg')

    # Blitting the background 
    win.blit(bg, (0,0))
    
    # Blitting the buttons on the screen.
    win.blit(redSquare[0] ,  ( 530,270)) # paint to screen
    win.blit(redSquare[1] ,  ( 530,370))
    win.blit(redSquare[2] ,  ( 530,470))

    # Updating the screen with the new displays.
    pygame.display.update()

# Defining the function that allows user to choose difficulty.
def chooseDifficulty(character1,character2,bg):

    # Displaying all the buttons and choices.
    fixedDifficultySetUp()

    running = True
    default = True
    difficulty = ''

    # The loop that allows user to choose the option.
    while (running):

        # Checking for an event occurace.
        for event in pygame.event.get():

            # Quitting the screen when the cross button is pressed.
            if event.type == pygame.QUIT:
                running = False

            # Checking if Mouse is pressed.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos

                # Checking if 'EASY' button is pressed.
                if ( x > 530 and x <860 and y > 270 and y < 320):
                    
                    # call your easy thing here
                    loadingbar(0)
                    singlePlayerGame(bg,character1,character2,1,'Easy')
                    loadingbar(1)
                    singlePlayerGame(bg,character1,character2,2,'Easy')

                # Checking if 'NORMAL' button is pressed.    
                if ( x > 530 and x <860 and y > 370 and y < 420 ):
                    
                    # call your normal thing here
                    loadingbar(0)
                    singlePlayerGame(bg,character1,character2,1,'Normal')
                    loadingbar(1)
                    singlePlayerGame(bg,character1,character2,2,'Normal')

                # Checking if 'HARD' button is pressed.    
                if ( x > 530 and x <860 and y > 470 and y < 520 ):
                    
                    # call your hard thing here
                    loadingbar(0)
                    singlePlayerGame(bg,character1,character2,1,'Hard')
                    loadingbar(1)
                    singlePlayerGame(bg,character1,character2,2,'Hard')
                    
        pygame.display.update()

    #loop over, quit pygame
    pygame.quit()


###################################################    CHARACTER SELECTION PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################

# Making a function that allows the user to choose the Character of the game.
# Creating a fixed display screen with all the buttons and options.  
def fixedCharacterSetUp(value):
        
    # Loading in the buttons images.
    redSquare = [pygame.image.load('AKAME.png'),pygame.image.load('YATO.png'),pygame.image.load('TANJIRO.png'),pygame.image.load('NEZUKO.png'),pygame.image.load('KOROSENSEI.png'),pygame.image.load('YUKINO.png')]

    # Loading in the platform image.
    platform  = pygame.image.load('platform.png')

    # Loading the KickOff Button image.
    kickoff = pygame.image.load('KickOff.png')

    #  Loading all the background images as per the need.
    bg = [pygame.image.load('player1.jpg'),pygame.image.load('player2.jpg'),pygame.image.load('AiOpponent.jpg')]

    # Blitting all the images and buttons on the screen,
    win.blit(bg[value], (0,0))
    win.blit(platform ,  (300,420))

    win.blit(redSquare[0] ,  ( 700,200)) # paint to screen
    win.blit(redSquare[1] ,  ( 700,270))
    win.blit(redSquare[2] ,  ( 700,340))
    win.blit(redSquare[3] ,  ( 700,410))
    win.blit(redSquare[4] ,  ( 700,480))
    win.blit(redSquare[5] ,  ( 700,550))

    win.blit(kickoff ,  ( 500,630))
    
    # Updating the screen with the new displays.
    pygame.display.update()

# Function that displays character sprites on the platform.
def characters(index,value):

    # Dispalying all the options.    
    fixedCharacterSetUp(value)

    # Loading all the idle sprites.
    sprite = [pygame.image.load('A_Idle.png'),pygame.image.load('Ya_Idle.png'),pygame.image.load('T_Idle.png'),pygame.image.load('N_Idle.png'),pygame.image.load('K_Idle.png'),pygame.image.load('Yu_Idle.png')]

    # Displaying the appropriate idle sprite on the platform.    
    if index == 2 or index ==3 or index ==4 :
        win.blit(sprite[index] ,  ( 325,310))
    elif index == 0 or index == 1:
        win.blit(sprite[index] ,  ( 325,325))
    elif index == 5:
        win.blit(sprite[index] ,  ( 340,318))

# Making a function that allows the user to choose the Character of the game.        
def chooseCharacter(value):

    # Declaring default characters.    
    running = True
    default = True
    character = 'Tanjiro'

    # Creating a loop that allows user to select the player.
    while (running):
            
        # Checking for an event occurace.    
        for event in pygame.event.get():

            # Quitting the screen when the cross button is pressed.    
            if event.type == pygame.QUIT:
                running = False

            # Checking if Mouse is pressed.    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                
                # Checking if 'Akame' button is pressed.
                if ( x > 700 and x <1030 and y > 200 and y < 250):
                    characters(0,value)
                    character = 'Akame'
                    default = False

                # Checking if 'Yato' button is pressed.    
                if ( x > 700 and x <1030 and y > 270 and y < 320 ):
                    characters(1,value)
                    character = 'Yato'
                    default = False

                # Checking if 'Tanjiro' button is pressed.    
                if ( x > 700 and x <1030 and y > 340 and y < 390 ):
                    characters(2,value)
                    character = 'Tanjiro'
                    default = False
                    
                # Checking if 'Nezuko' button is pressed.    
                if ( x > 700 and x <1030 and y > 410 and y < 460 ):
                    characters(3,value)
                    character = 'Nezuko'
                    default = False
                    
                # Checking if 'Korosensie' button is pressed.    
                if ( x > 700 and x <1030 and y > 480 and y < 530 ):
                    characters(4,value)
                    character = 'Korosensei'
                    default = False
                    
                # Checking if 'Yukino' button is pressed.    
                if ( x > 700 and x <1030 and y > 550 and y < 600 ):
                    characters(5,value)
                    character = 'Yukino'
                    default = False
                
                # Checking if 'Kickoff' button is pressed.
                if ( x > 500 and x <830 and y > 630 and y < 680 ):
                    return (character)   
                    
        pygame.display.update()

    #loop over, quit pygame
    #pygame.quit()



###################################################    STADIUM SELECTION PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################

# Making a function that allows the user to choose the Stadium of the game.
# Creating a fixed display screen with all the buttons and options.  
def fixedStaduimSetUp():
    bg = pygame.image.load('background1.jpg')
    platform = pygame.image.load('platform.png')
    kickoff = pygame.image.load('KickOff.png')
    buttons = [pygame.image.load('ZLbutton.png'),pygame.image.load('CNbutton.png'),pygame.image.load('SHbutton.png'),pygame.image.load('KickOff.png')]

    win.blit(bg, (0,0))
    win.blit(platform ,  (300,420))

    win.blit(buttons[0] ,  ( 700,300)) # paint to screen
    win.blit(buttons[1] ,  ( 700,400))
    win.blit(buttons[2] ,  ( 700,500))
    
    win.blit(kickoff ,  ( 500,600))

    pygame.display.update()

# Function that displays stadium sprites on the platform.
def stadiums(index):

    # Dispalying all the options.     
    fixedStaduimSetUp()

    # Loading the pics for the stadium. 
    sprite = [pygame.image.load('zcn.jpg'),pygame.image.load('cnn.jpg'), pygame.image.load('shn.jpg') ]

    # Displaying the appropriate stadium pics on the platform.    
    if index == 0 :
        win.blit(sprite[index] ,  ( 255,310))
    elif index == 1:
        win.blit(sprite[index] ,  ( 255,310))  
    elif index == 2:
        win.blit(sprite[index] ,  ( 255,310))

# Making a function that allows the user to choose the Stadium of the game.          
def chooseStaduim():

    # Displaying the with fixed buttons and images.    
    fixedStaduimSetUp()

    # Declaring default characters.
    running = True
    stadium = 0

    # Creating a loop that allows user to select the Stadium.
    while (running):

        # Checking for an event occurace.     
        for event in pygame.event.get():

            # Quitting the screen when the cross button is pressed.    
            if event.type == pygame.QUIT:
                running = False

            # Checking if Mouse is pressed.     
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos

                # Checking if 'Zombie Court' button is pressed.
                if ( x > 700 and x <1030 and y > 300 and y < 350):
                    stadiums(0)
                    stadium = 0

                # Checking if 'Camp Nou' button is pressed.    
                if ( x > 700 and x <1030 and y > 400 and y < 450 ):
                    stadiums(1)
                    stadium = 1

                # Checking if 'Slytherin Hall' button is pressed.    
                if ( x > 700 and x <1030 and y > 500 and y < 550 ):
                    stadiums(2)
                    stadium = 2

                # Checking if 'Kickoff' button is pressed.    
                if ( x > 500 and x <830 and y > 600 and y < 650 ):
                    return stadium
                    
        pygame.display.update()
#==================================================================================================================
#==================================================================================================================
#==================================================================================================================

# Making a function that allows the user to see the settings page of the game.        
def displaysettings():
    run = True

    # Loading the pictures for the background.
    bg = pygame.image.load('setbg.jpg')

    # Loading the button for 'Back'.
    back = pygame.image.load('back.png')

    # Blitting the background and button on the screen.
    win.blit(bg,(-30,-65))
    win.blit(back,(5,15))
    
    pygame.display.flip()

    # A loop that allows the user to access the settings screen and to use the 'Back' button.
    while run:

        # Checking for an event occurace.     
        for event in pygame.event.get():

            # Quitting the screen when the cross button is pressed.
            if event.type == pygame.QUIT:
                
                running = False
                
                run = False

            # Checking if Mouse is pressed.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                win.blit(back,(0,0))

                # Checking if 'Back' button is pressed.
                if( x > 5 and x < 155 and y>15 and y<50):

                    # Calling back the intro function.    
                    intro()
            

#==================================================================================================================
#==================================================================================================================
# Defining a function that gives the user the option to play on another game.
# This function also displays the winner of the previous game.
def winnercalculator( score1, score2 ):

    # A variable to determine the number of time the game is being played. 
    click = 1
    
    # Blitting the images as per the scores.
    # Loading the background images.
    bg = [pygame.image.load('playeronewins.jpg'),pygame.image.load('playerzerowins.jpg'),pygame.image.load('playertwowins.jpg')]
    # Player1 wins!
    if score1 > score2:
        win.blit(bg[0],(0,0))
        
    # Its a Draw! 
    elif score1 == score2:
        win.blit(bg[1],(0,0))
        
    # Player2 wins!
    else:
        win.blit(bg[2],(0,0))

    running = True
    # A loop that allows the user to choose the option.
    while (running):
        
        # Checking for an event occurace.
        for event in pygame.event.get():

            # Quitting the screen when the cross button is pressed.
            if event.type == pygame.QUIT:
                
                running = False
                
                run = False

            # Checking if Mouse is pressed.    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos

                # Checking if 'YES' button is pressed.
                if ( x > 400 and x < 530 and y > 540 and y < 640 ):

                    # Calling back the intro function that restarts the game.
                    click += 1
                    intro(click)

                # Checking if 'NO ' button is pressed.    
                if ( x > 830 and x < 960 and y > 540 and y < 640 ):
                    
                    # Exiting the game.
                    pygame.quit()
                    quit()
        pygame.display.flip()
#==================================================================================================================
#==================================================================================================================

# Making the intro function that allows the user to choose the mode of game or access the settings or exit .
def intro(gameplayed):
    
    #pygame.mixer.music.play(-1)
    if gameplayed == 0:
        music.play(-1)    
    
    # Loading in the images for buttons and backgrounds.    
    stadiums = [pygame.image.load('ZombieCourt.jpg'),pygame.image.load('CampNou.jpg'),pygame.image.load('SlytherinHall.jpg')]
    redSquare = [pygame.image.load("ARCADE.png").convert(),pygame.image.load("FRIENDS.png").convert(),pygame.image.load("controls.png").convert(),pygame.image.load("QUIT.png").convert()]

    # Loading in the background.
    bg = pygame.image.load('background.jpg')

    # Blitting the images on the screen.
    win.blit(bg, (0,0))

    win.blit(redSquare[0] ,  ( 160,320)) # paint to screen
    win.blit(redSquare[1] ,  ( 160,400))
    win.blit(redSquare[2] ,  ( 160,480))
    win.blit(redSquare[3] ,  ( 160,560))

    pygame.display.flip() # paint screen one time
    

    #loop over, quite pygame
    running = True

    # A loop that allows the user to choose the game mode.
    while (running):
        
        # Checking for an event occurace.
        for event in pygame.event.get():

            # Quitting the screen when the cross button is pressed.
            if event.type == pygame.QUIT:
                
                running = False
                
                run = False

            # Checking if Mouse is pressed.    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos

                # Checking if 'ARCADE' button is pressed.
                if ( x > 160 and x <490 and y > 320 and y < 370 ):

                    # Calling in the function to select the user's character.
                    fixedCharacterSetUp(0)
                    character1 = chooseCharacter(0)

                    # Calling in the function to select the Computer's character.
                    fixedCharacterSetUp(2)
                    character2 = chooseCharacter(2)

                    # Calling the function to select the stadium.
                    stadium = chooseStaduim()
                    bg = stadiums[stadium]
                    
                    chooseDifficulty(character1,character2,bg)
                    
                    
                    running = False

                # Checking if 'FRIENDS ' button is pressed.    
                if ( x > 160 and x <490 and y > 400 and y < 450 ):

                    # Calling in the function to select the user1's character.    
                    fixedCharacterSetUp(0)
                    character1 = chooseCharacter(0)

                    # Calling in the function to select the user2's character.
                    fixedCharacterSetUp(1)
                    character2 = chooseCharacter(1)

                    # Calling the function to select the stadium.
                    stadium = chooseStaduim()
                    bg = stadiums[stadium]

                    # Calling in the loading bar for the first half.
                    loadingbar(0)
                    # Calling the function that starts the Multiplayer Game.
                    multiplayerGame(bg,character1,character2,1)

                    # Calling in the loading bar for the first half.
                    loadingbar(1)
                    # Calling the function that starts the Multiplayer Game.
                    multiplayerGame(bg,character1,character2,2)
                    
                    running = False

                # Checking if 'SETTINGS' button is pressed.    
                if ( x > 160 and x <490 and y > 480 and y < 530 ):

                    # Calling the function that displays the settings page.
                    displaysettings()

                # Checking if 'QUIT' button is pressed.    
                if ( x > 160 and x <490 and y > 560 and y < 610 ):
                    
                    pygame.quit()
                    quit()

intro(0)

