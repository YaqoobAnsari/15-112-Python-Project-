# 15-112-Python-Project-
The project is a simple python game, called Jump Soccer, which is a 1 vs 1 football game.

######## INSTRUCTIONS FOR USE #####################################################################
###################################################################################################
1)	Pre-requisite:
    •	Install Pygame: 
      o	Open command Prompt
      o	Type: pip3 install pygame
2)	Game Information:
      a.	Arcade Mode: Its Single player Mode against AI having three difficulty modes
      b.	Friends Mode: Its Multi player Mode; its PvP mode. 
3)	Download all the files uploaded (The audio and image files).
4)	Store them the same folder.
5)	Run the file Mainfile.py

######## INSTRUCTIONS FOR USE #####################################################################
###################################################################################################

Computer project: Jump Soccer 2:
The project that I am working is a game called Jump Soccer, it is based on an existing game called Head Soccer. The game is basically a 1 vs 1 football game. The players aim is to get the ball into the opponent’s goal. The game would have the following features:
Game Guidelines:
1)	A match of the game would have 2 sets.
2)	Match time of each set will be 90 seconds in total.
3)	The game would have 3 difficulty levels which will determine the level of the AI’s responses:
        a.	Easy: The opponent would block simple attempts to score by jumping only and moving (minimum movements).
        b.	Normal: The opponent would have a fixed area where it will defend by jumping and kicking and additionally, dash to clear the            ball from his side of the court.
        c.	Hard: The opponent would have a fixed area to defend by jumping, kicking, and dashing. Additionally, it will follow the ball            back and attempt to score if possible. 
4)	The game will have 6 characters.
5)	The game can be played in 2 modes:
        a.	Arcade (Single player Mode):
            i.	This will be against a simple AI (whose main aim would be to just jump and stop the ball).
        b.	Friends (Multi player Mode):
            i.	This would allow two players to play the game at the same time on the same machine.
6)	The game would begin with the ball being dropped from a height (bounce from a height) at the center of the field.
7)	 The goal of the game is to get the ball into the opponent’s goal area either any legal means.
Key Bindings:
a.	Repeated >  / < (two times) == Dash in particular direction.
b.	Classic movement keys ,  for moving left and right.
c.	Up arrow key for jump:
        i.	Jump will be parabolic or of any other polynomial curve.
        ii.	Mid-Jump movements of left or right are allowed.
        iii.	A single jump is only allowed i.e. only when a jump is full performed then only can the player jump again.
        iv.	Jump would allow a player to essentially climb on the other player ( possible bug).
d.	Space bar to kick:
        i.	 Kicks the ball.
        ii.	The ball’s projectile would follow a projectile motion or any other polynomial curve.
Character Information:
a.	These characters would have the following names:
    •	Yato
    •	Yukino
    •	Akame
    •	Korosensei 
    •	Tanjiro
    •	Nezuko
b.	Each character would have a special/unique move.
iii.	This move can only be used when a Skill Meter would be full.
        1.	This meter would slowly fill up on its own at a fixed rate (depends on difficulty selected).
        2.	The meter can be filled faster if the player/opponents scores a goal (increase by a fixed percentage).
iv.	The use of the special move depletes the Skill meter completely.

Libraries to be used:
    •	Pygame
    •	Tkinter
    •	Time
    •	PIL

	The game would begin with a home/main screen showing the options of play, settings, credit and exit. 
	Selecting Play would take user to the screen to choose the mode of game i.e. Arcade or Multiplayer. Then the user would proceed to        choose the character/player of choice and then to choose the stadium of choice (4 choice of stadiums will be provided) and then the      game would begin in the mode selected. At all points in after selecting Play, the user would have the option to return to the            previous screen through a Back button or  shaped button.
	Selecting on Settings would take the user to a screen that would give the user the options to change key configurations of the            controls and to disable/enable sounds. Upon any change the user will prompted to confirm his changes to the setting or revert back      to the default settings. This would be done through a message box window. At all points in after selecting Settings, the user would      have the option to return to the previous screen through a Back button or  shaped button.
	Selecting on Credits would show the user the acknowledgement and citations to the creators of the game. At all points in after            selecting Credits, the user would have the option to return to the previous screen through a Back button or  shaped button.
	Selecting Quit, would exit the game and close the game window.   

