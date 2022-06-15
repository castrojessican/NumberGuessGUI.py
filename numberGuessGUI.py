"""

Program:numberGuessGUI.py(page 269- 272)
Author: Jessica 6/7/2022

GUI-based version of the number guessing game from chapter 2.


"""

from breezypythongui import EasyFrame
import random
# other imports

class GuessingGame(EasyFrame):

# definition of the __init__ () method which is our class constructor
def __init__(self):
	# Call the EasyFrane version of the __init__
	EasyFrame.__init__(self, title = "Guessing Game")
	# initialize the instance variables for the class 
	self.MyNumber = random.randint(1,10)
	self.count = 0
	# Create and add widgets to the window
	greeting = "Guess a number between 1 and 100."
	self.hintLabel = self.addLabel(text = greeting,
									row = 0, column = 0,
									sticky = "NSEW",
									columnspan = 2)
	self.addLabel(text = "your guess", row = 1, column = 0)
	self.guessField = self.addIntegerField(0, row = 1, column = 1)
	# Buttons have no command attributes yet
	self.nextButton = self.addButton(text = "Next", row = 2
									column = 0, command = self.nextGuess)
	self.newButton = self.addButton(text = "New Game",
									row = 2, column = 1, command = self.newGame)

	# The event handling methods for the buttons
	def nextGuess(self):
		"""Process the users next guess."""
		self.count += 1
		guess = self.guessField.getNumber()
		if guess == self.myNumber:
			self.hintLabel["text"] = "You've guessed it in" + \
			    						str(self.count) + "attempts!"
			self.nextButton["state"] = "disabled"
		elif guess < self.myNumber:
			self.hintLabel["text"] = "Sorry, too small!"
		else: 
			self.hintLabel["text"] = "Sorry, too large!"


		def newGame(self):
			""" Resets the data and GUI to their original states."""
			self.myNumber = random.randint(1, 100)
			slef.count = 0
			greeting = "Guess a number between 1 and 100."
			self.hintLabel["text"] = greeting
			self.guessField.setNumber(0)
			self.nextButton["state"] = "normal"



	# definition of the main() method which will establish class objects
def main():
	#instantiate an object from the class into mainLoop()
	GuessingGame().mainLoop()

main()		