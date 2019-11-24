import pygame
import time
import random

pygame.init()
#===============================================================================================================
#===============================================================================================================

window_width=1400
window_height=704

# Open a window
size = (window_width, window_height)
win = pygame.display.set_mode(size)

pygame.display.set_caption("Jump Soccer")

walkRight = [pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png')]
walkLeft = [pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png'),pygame.image.load('T_Moving_Step.png'),pygame.image.load('T_Moving_Step_Back.png')]
kick = [pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png'),pygame.image.load('T_Kick.png')]

char = pygame.image.load('T_Idle.png')



clock = pygame.time.Clock()

def characterDictionary():
    # [[WALKRIGHT],[WALKLEFT],[KICK],[IDLE]
    # USERS SPRITES
    A_Walkright = [pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png')]
    A_Walkleft = [pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png'),pygame.image.load('A_Moving_Step.png'),pygame.image.load('A_Moving_Step_Back.png')]
    A_Kick = [pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png'),pygame.image.load('A_Kick.png')]
    A_Idle = [pygame.image.load('A_Idle.png')]
    
    T_Walkright =[pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha()]
    T_Walkleft =[pygame.image.load('T_Moving_Step_Back.png').convert_alpha().convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha(),pygame.image.load('T_Moving_Step.png').convert_alpha(),pygame.image.load('T_Moving_Step_Back.png').convert_alpha()]
    T_Kick =[pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha(),pygame.image.load('T_Kick.png').convert_alpha()]
    T_Idle = [pygame.image.load('T_Idle.png').convert_alpha()]
    
    N_Walkright = [pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png')]
    N_Walkleft = [pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png'),pygame.image.load('N_Moving_Step.png'),pygame.image.load('N_Moving_Step_Back.png')]
    N_Kick = [pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png'),pygame.image.load('N_Kick.png')]
    N_Idle = [pygame.image.load('N_Idle.png')]
    
    Y_Walkright = [pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png')]
    Y_Walkleft = [pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png'),pygame.image.load('Y_Moving_Step.png'),pygame.image.load('Y_Moving_Step_Back.png')]
    Y_Kick =[pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png'),pygame.image.load('Y_Kick.png')]
    Y_Idle = [pygame.image.load('Y_Idle.png')]
    
    Yu_Walkright = [pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png')]
    Yu_Walkleft = [pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png'),pygame.image.load('Yu_Moving_Step.png'),pygame.image.load('Yu_Moving_Step_Back.png')]
    Yu_Kick = [pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png'),pygame.image.load('Yu_Kick.png')]
    Yu_Idle = [pygame.image.load('Yu_Idle.png')]
    
    K_Walkright = [pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png')]
    K_Walkleft = [pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png'),pygame.image.load('K_Moving_Step.png'),pygame.image.load('K_Moving_Step_Back.png')]
    K_Kick = [pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png'),pygame.image.load('K_Kick.png')]
    K_Idle = [pygame.image.load('K_Idle.png')]
    
    characterSprites = {}
    
    characterSprites['Akame'] = [A_Walkright,A_Walkleft,A_Kick,A_Idle]
    characterSprites['Tanjiro'] = [T_Walkright,T_Walkleft,T_Kick,T_Idle]
    characterSprites['Nezuko'] = [N_Walkright,N_Walkleft,N_Kick,N_Idle]
    characterSprites['Yato'] = [Y_Walkright,Y_Walkleft,Y_Kick,Y_Idle]
    characterSprites['Yukino'] = [Yu_Walkright,Yu_Walkleft,Yu_Kick,Yu_Idle]
    characterSprites['Korosensei'] = [K_Walkright,K_Walkleft,K_Kick,K_Idle]
    
    
    # [[WALKRIGHT],[WALKLEFT],[Kick_O],[IDLE_O]
    # OPPONENTS SPRITE
    A_Walkright_O = [pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png')]
    A_Walkleft_O = [pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png'),pygame.image.load('A_Moving_Step_O.png'),pygame.image.load('A_Moving_Step_Back_O.png')]
    A_Kick_O = [pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png'),pygame.image.load('A_Kick_O.png')]
    A_Idle_O = [pygame.image.load('A_Idle_O.png')]
    
    T_Walkright_O =[pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png')]
    T_Walkleft_O =[pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png'),pygame.image.load('T_Moving_Step_O.png'),pygame.image.load('T_Moving_Step_Back_O.png')]
    T_Kick_O =[pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png'),pygame.image.load('T_Kick_O.png')]
    T_Idle_O = [pygame.image.load('T_Idle_O.png')]
    
    N_Walkright_O = [pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png')]
    N_Walkleft_O = [pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png'),pygame.image.load('N_Moving_Step_O.png'),pygame.image.load('N_Moving_Step_Back_O.png')]
    N_Kick_O = [pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png'),pygame.image.load('N_Kick_O.png')]
    N_Idle_O = [pygame.image.load('N_Idle_O.png')]
    
    Y_Walkright_O = [pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png')]
    Y_Walkleft_O = [pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png'),pygame.image.load('Y_Moving_Step_O.png'),pygame.image.load('Y_Moving_Step_Back_O.png')]
    Y_Kick_O =[pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png'),pygame.image.load('Y_Kick_O.png')]
    Y_Idle_O = [pygame.image.load('Y_Idle_O.png')]
    
    Yu_Walkright_O = [pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png')]
    Yu_Walkleft_O = [pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png'),pygame.image.load('Yu_Moving_Step_O.png'),pygame.image.load('Yu_Moving_Step_Back_O.png')]
    Yu_Kick_O = [pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png'),pygame.image.load('Yu_Kick_O.png')]
    Yu_Idle_O = [pygame.image.load('Yu_Idle_O.png')]
    
    K_Walkright_O = [pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png')]
    K_Walkleft_O = [pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png'),pygame.image.load('K_Moving_Step_O.png'),pygame.image.load('K_Moving_Step_Back_O.png')]
    K_Kick_O = [pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png'),pygame.image.load('K_Kick_O.png')]
    K_Idle_O = [pygame.image.load('K_Idle_O.png')]
    
    characterSpritesOpponent = {}
    
    characterSpritesOpponent['Akame'] = [A_Walkright_O,A_Walkleft_O,A_Kick_O,A_Idle_O]
    characterSpritesOpponent['Tanjiro'] = [T_Walkright_O,T_Walkleft_O,T_Kick_O,T_Idle_O]
    characterSpritesOpponent['Nezuko'] = [N_Walkright_O,N_Walkleft_O,N_Kick_O,N_Idle_O]
    characterSpritesOpponent['Yato'] = [Y_Walkright_O,Y_Walkleft_O,Y_Kick_O,Y_Idle_O]
    characterSpritesOpponent['Yukino'] = [Yu_Walkright_O,Yu_Walkleft_O,Yu_Kick_O,Yu_Idle_O]
    characterSpritesOpponent['Korosensei'] = [K_Walkright_O,K_Walkleft_O,K_Kick_O,K_Idle_O]

    return [characterSprites,characterSpritesOpponent]

allCharactersSprites = characterDictionary()


class player(object):
    def __init__(self,x,y,width,height,Opponent):
        
        self.x = x
        self.y = y
        self.width = width
        
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.kick = False
        self.right = False
        self.isOpponent = Opponent
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win,character,isOpponent):
        if (not isOpponent):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[0][character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[0][character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[0][character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False 
                
            else:
                win.blit(allCharactersSprites[0][character][3][0], (self.x,self.y))
        else:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[1][character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[1][character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[1][character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                
            else:
                win.blit(allCharactersSprites[1][character][3][0], (self.x,self.y))
            


###################################################    CHARACTER SELECTION PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################
 
def fixedCharacterSetUp(value):
        
    
    redSquare = [pygame.image.load('AKAME.png'),pygame.image.load('YATO.png'),pygame.image.load('TANJIRO.png'),pygame.image.load('NEZUKO.png'),pygame.image.load('KOROSENSEI.png'),pygame.image.load('YUKINO.png')]
    platform  = pygame.image.load('platform.png')
    kickoff = pygame.image.load('KickOff.png')
    bg = [pygame.image.load('player1.jpg'),pygame.image.load('player2.jpg'),pygame.image.load('AiOpponent.jpg')]


    win.blit(bg[value], (0,0))
    win.blit(platform ,  (300,420))

    win.blit(redSquare[0] ,  ( 700,200)) # paint to screen
    win.blit(redSquare[1] ,  ( 700,270))
    win.blit(redSquare[2] ,  ( 700,340))
    win.blit(redSquare[3] ,  ( 700,410))
    win.blit(redSquare[4] ,  ( 700,480))
    win.blit(redSquare[5] ,  ( 700,550))

    win.blit(kickoff ,  ( 500,630))

    pygame.display.update()


def characters(index,value):
    fixedCharacterSetUp(value)
    sprite = [pygame.image.load('A_Idle.png'),pygame.image.load('Ya_Idle.png'),pygame.image.load('T_Idle.png'),pygame.image.load('N_Idle.png'),pygame.image.load('K_Idle.png'),pygame.image.load('Yu_Idle.png')]
    if index == 2 or index ==3 or index ==4 :
        win.blit(sprite[index] ,  ( 325,310))
    elif index == 0 or index == 1:
        win.blit(sprite[index] ,  ( 325,325))
    elif index == 5:
        win.blit(sprite[index] ,  ( 340,318))
        
def chooseCharacter(value):
    running = True
    default = True
    character = 'Akame'
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                
                if ( x > 700 and x <1030 and y > 200 and y < 250):
                    characters(0,value)
                    character = 'Akame'
                    default = False
                    
                if ( x > 700 and x <1030 and y > 270 and y < 320 ):
                    characters(1,value)
                    character = 'Yato'
                    default = False
                     
                    
                if ( x > 700 and x <1030 and y > 340 and y < 390 ):
                    characters(2,value)
                    character = 'Tanjiro'
                    default = False
                    
                    
                if ( x > 700 and x <1030 and y > 410 and y < 460 ):
                    characters(3,value)
                    character = 'Nezuko'
                    default = False
                    
                    
                if ( x > 700 and x <1030 and y > 480 and y < 530 ):
                    characters(4,value)
                    character = 'Korosensei'
                    default = False
                    
                    
                if ( x > 700 and x <1030 and y > 550 and y < 600 ):
                    characters(5,value)
                    character = 'Yukino'
                    default = False
                

                if ( x > 500 and x <830 and y > 630 and y < 680 ):
                    return (character)   
                    
        pygame.display.update()

    #loop over, quit pygame
    #pygame.quit()




###################################################    STADIUM SELECTION PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################



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


def stadiums(index):
    fixedStaduimSetUp()
    
    sprite = [pygame.image.load('zcn.jpg'),pygame.image.load('cnn.jpg'), pygame.image.load('shn.jpg') ]

    if index == 0 :
        win.blit(sprite[index] ,  ( 255,310))
    elif index == 1:
        win.blit(sprite[index] ,  ( 255,310))  
    elif index == 2:
        win.blit(sprite[index] ,  ( 255,310))
        
        
def chooseStaduim():
    fixedStaduimSetUp()
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if ( x > 700 and x <1030 and y > 300 and y < 350):
                    stadiums(0)
                    stadium = 0
                    
                if ( x > 700 and x <1030 and y > 400 and y < 450 ):
                    stadiums(1)
                    stadium = 1
                    
                if ( x > 700 and x <1030 and y > 500 and y < 550 ):
                    stadiums(2)
                    stadium = 2
                    
                if ( x > 500 and x <830 and y > 600 and y < 650 ):
                    return stadium
                    
        pygame.display.update()

    #pygame.quit()

###################################################    LOADING SCREEN PART OF CODE #################################################################
#===================================================================================================================================
###################################################################################################################################################

def loadingbar():
    bg = pygame.image.load('bg.jpg')

    green = [0,255,0]
    black = [0,0,0]
    white = [255,255,255]

    smallfont = pygame.font.SysFont('Impact',30)


    progress = 0
    
    def loading(progress):
        if progress < 100:
            text = smallfont.render('Loading ' + str(int(progress)) + '%',True, green)
            
        else:
            text = smallfont.render('Loading ' + str(100) + '%',True, green)
            
        win.blit( text, (600,555))


    while ((progress//5) < 100):
        
        
        increase = random.randint(1,20)
        progress += increase
        win.blit(bg, (0,0))
        
        pygame.draw.rect(win,green,(448,498,508,54))
        

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                print(x,y)
            
        if (progress/5) > 100:
            pygame.draw.rect(win,black,(452,502,500,46))
            
        else:
            pygame.draw.rect(win,black,(452,502,progress,46))
           
        loading(progress//5)

        pygame.display.flip()

        time.sleep(0.05)
    return

 
###################################################    START OF ARCADE PART OF CODE #################################################################
###################################################################################################################################################
'''
def arcade(character,stadium):

    #mainloop
    man = player(200, 345, 64,64,False)
    run = True
    indexcount = 0
    while run:
        #clock.tick(270)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            
        elif keys[pygame.K_RIGHT] and man.x < window_width - man.width - man.vel-130:
            man.x += man.vel
            man.right = True
            man.left = False
            
        elif keys[pygame.K_SPACE]:
            man.right = False
            man.left = False
            man.kick = True
            
        else:
            man.right = False
            man.left = False
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
                
                
        else:
            if man.jumpCount >= -10:
                neg = 1
                
                if man.jumpCount < 0:
                    neg = -1
                    
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
                
            else:
                man.isJump = False
                man.jumpCount = 10
                
        isOpponent = False
        redrawGameWindow(man,character,isOpponent,stadium)
        
        
    pygame.quit()

def redrawGameWindow(man,character,isOpponent,stadium):
    stadiums = [pygame.image.load('ZombieCourt.jpg'),pygame.image.load('CampNou.jpg'),pygame.image.load('SlytherinHall.jpg')]
    bg = pygame.image.load('ArcadeBg.jpg')
    win.blit(stadiums[stadium], (0,0))
    man.draw(win,character,isOpponent)
    pygame.display.update()
'''

class singleplayer(object):
    def __init__(self,x,y,width,height,isOpponent):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.kick = False
        self.right = False
        self.isOpponent = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win,character,isOpponent):
        if (not isOpponent):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[0][character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[0][character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[0][character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False 
                
            else:
                win.blit(allCharactersSprites[0][character][3][0], (self.x,self.y))
        else:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[1][character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[1][character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[1][character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                
            else:
                win.blit(allCharactersSprites[1][character][3][0], (self.x,self.y))
            



def redrawGameWindowSingle(man,character1,player2,character2,stadium):
    notOpponent= False
    Opponent = True
    stadiums = [pygame.image.load('ZombieCourt.jpg'),pygame.image.load('CampNou.jpg'),pygame.image.load('SlytherinHall.jpg')]
    bg = pygame.image.load('ArcadeBg.jpg')
    win.blit(stadiums[stadium], (0,0))
    man.draw(win,character1,notOpponent)
    player2.draw(win,character2,Opponent)
    pygame.display.update()


#mainloop
def singlePlayerGame(character1,character2,stadiumChosen):
    notOpponent= False
    Opponent = True
    man = singleplayer(200, 345, 64,64,notOpponent)
    player2 = singleplayer(1000,345,64,64,Opponent)
    run = True
    indexcount = 0
    while run:
        clock.tick(27)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            
        elif keys[pygame.K_RIGHT] and man.x < window_width - man.width - man.vel-130:
            man.x += man.vel
            man.right = True
            man.left = False
            
        elif keys[pygame.K_SPACE]:
            man.right = False
            man.left = False
            man.kick = True
            
        else:
            man.right = False
            man.left = False
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
                
                
        else:
            if man.jumpCount >= -10:
                neg = 1
                
                if man.jumpCount < 0:
                    neg = -1
                    
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
                
            else:
                man.isJump = False
                man.jumpCount = 10

        ####################################################
        

        redrawGameWindowSingle(man,character1,player2,character2,stadiumChosen)
        
        
    pygame.quit()
###################################################    END OF ARCADE PART OF CODE #################################################################
###################################################################################################################################################

###################################################    FRIENDS OF ARCADE PART OF CODE #################################################################
###################################################################################################################################################

class multiplayer(object):
    def __init__(self,x,y,width,height,isOpponent):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.kick = False
        self.right = False
        self.isOpponent = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win,character,isOpponent):
        if (not isOpponent):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[0][character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[0][character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[0][character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False 
                
            else:
                win.blit(allCharactersSprites[0][character][3][0], (self.x,self.y))
        else:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(allCharactersSprites[1][character][0][self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(allCharactersSprites[1][character][1][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.kick:
                win.blit(allCharactersSprites[1][character][2][self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.kick = False
                
            else:
                win.blit(allCharactersSprites[1][character][3][0], (self.x,self.y))
            



def redrawGameWindow(man,character1,player2,character2,stadium):
    notOpponent= False
    Opponent = True
    stadiums = [pygame.image.load('ZombieCourt.jpg'),pygame.image.load('CampNou.jpg'),pygame.image.load('SlytherinHall.jpg')]
    bg = pygame.image.load('ArcadeBg.jpg')
    win.blit(stadiums[stadium], (0,0))
    man.draw(win,character1,notOpponent)
    player2.draw(win,character2,Opponent)
    pygame.display.update()


#mainloop
def multiplayerGame(character1,character2,stadiumChosen):
    notOpponent= False
    Opponent = True
    man = multiplayer(200, 345, 64,64,notOpponent)
    player2 = multiplayer(1000,345,64,64,Opponent)
    run = True
    indexcount = 0
    while run:
        clock.tick(27)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            
        elif keys[pygame.K_RIGHT] and man.x < window_width - man.width - man.vel-130:
            man.x += man.vel
            man.right = True
            man.left = False
            
        elif keys[pygame.K_SPACE]:
            man.right = False
            man.left = False
            man.kick = True
            
        else:
            man.right = False
            man.left = False
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
                
                
        else:
            if man.jumpCount >= -10:
                neg = 1
                
                if man.jumpCount < 0:
                    neg = -1
                    
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
                
            else:
                man.isJump = False
                man.jumpCount = 10

        ####################################################
        if keys[pygame.K_a] and player2.x > player2.vel:
            player2.x -= player2.vel
            player2.left = True
            player2.right = False
            
        elif keys[pygame.K_d] and player2.x < window_width - player2.width - player2.vel-130:
            player2.x += player2.vel
            player2.right = True
            player2.left = False
            
        elif keys[pygame.K_q]:
            player2.right = False
            player2.left = False
            player2.kick = True
            
        else:
            player2.right = False
            player2.left = False
            player2.walkCount = 0
            
        if not(player2.isJump):
            if keys[pygame.K_w]:
                player2.isJump = True
                player2.right = False
                player2.left = False
                player2.walkCount = 0
                
                
        else:
            if player2.jumpCount >= -10:
                neg = 1
                
                if player2.jumpCount < 0:
                    neg = -1
                    
                player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
                player2.jumpCount -= 1
                
            else:
                player2.isJump = False
                player2.jumpCount = 10

        redrawGameWindow(man,character1,player2,character2,stadiumChosen)
        
        
    pygame.quit()
###################################################    INTRO PART OF CODE #################################################################
###################################################################################################################################################



def intro():
    redSquare = [pygame.image.load("ARCADE.png").convert(),pygame.image.load("FRIENDS.png").convert(),pygame.image.load("SETTINGS.png").convert(),pygame.image.load("QUIT.png").convert()]

    bg = pygame.image.load('background.jpg')
    win.blit(bg, (0,0))

    win.blit(redSquare[0] ,  ( 160,320)) # paint to screen
    win.blit(redSquare[1] ,  ( 160,400))
    win.blit(redSquare[2] ,  ( 160,480))
    win.blit(redSquare[3] ,  ( 160,560))

    pygame.display.flip() # paint screen one time
    

    #loop over, quite pygame
    running = True
    while (running):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                running = False
                
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                
                if ( x > 160 and x <490 and y > 320 and y < 370 ):
                    
                    fixedCharacterSetUp(0)
                    character1 = chooseCharacter(0)
                    
                    fixedCharacterSetUp(2)
                    character2 = chooseCharacter(2)
                    
                    stadiumChosen = chooseStaduim()
                    
                    loadingbar()
                    
                    singlePlayerGame(character1,character2,stadiumChosen)
                    
                    running = False
                    
                if ( x > 160 and x <490 and y > 400 and y < 450 ):
                    
                    fixedCharacterSetUp(0)
                    character1 = chooseCharacter(0)
                    
                    fixedCharacterSetUp(1)
                    character2 = chooseCharacter(1)
                    
                    stadiumChosen = chooseStaduim()
                    
                    loadingbar()
                    
                    multiplayerGame(character1,character2,stadiumChosen)
                    
                    running = False

                    
                if ( x > 160 and x <490 and y > 480 and y < 530 ):
                    
                    print('settings')#running = False
                    
                if ( x > 160 and x <490 and y > 560 and y < 610 ):
                    
                    print('quit')
                    
                    pygame.quit()
                    quit()

               

intro()
