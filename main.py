from tkinter import *
from PIL import Image, ImageTk
from functools import partial

window = Tk()
window.title("Tic Tac Toe")
window.config(bg="white")

currentUser = "X"
clicksCount = 0
gameBoard = ["white", "white", "white", "white", "white", "white", "white", "white", "white"]
playGame = True

loadO = Image.open("tic tac toeO_sized.png")
renderO = ImageTk.PhotoImage(loadO)

loadX = Image.open("tic tac toeX_sized.png")
renderX = ImageTk.PhotoImage(loadX)

loadWhite = Image.open("whiteSquare_sized.jpg")
renderWhite = ImageTk.PhotoImage(loadWhite)


titleLabel = Label(window, text="Tic Tac Toe", font=("Comic Sans Ms", 40), bg="white", fg="navy")
titleLabel.grid(row=1, column=1, columnspan=3)

def squarePressed(squareNumber):
  global currentUser
  global clicksCount
  global gameBoard
  global playGame
  print(squareNumber)
  if playGame == True:
    if currentUser == "X" and gameBoard[(squareNumber-1)] == "white":
      buttonsList[(squareNumber-1)].config(image=renderX)
      gameBoard[(squareNumber-1)] = "X"
      currentUser = "O"
      clicksCount += 1
      checkWin()
    elif currentUser == "O" and gameBoard[(squareNumber-1)] == "white":
      buttonsList[(squareNumber-1)].config(image=renderO)
      gameBoard[(squareNumber-1)] = "O"
      checkWin
      currentUser = "X"
      clicksCount += 1
      checkWin()
  if clicksCount == 9:
    print("All squares pressed")
    checkWin()

def checkWin():
  global playGame
  print("lets check if someone is winning")
  print(gameBoard)
  #check all straight lines for both x's and o's
  if gameBoard[0] == "X" and gameBoard[1] == "X" and gameBoard[2] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[0] == "O" and gameBoard[1] == "O" and gameBoard[2] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  elif gameBoard[0] == "X" and gameBoard[3] == "X" and gameBoard[6] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[0] == "O" and gameBoard[3] == "O" and gameBoard[6] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  elif gameBoard[6] == "X" and gameBoard[7] == "X" and gameBoard[8] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[6] == "O" and gameBoard[7] == "O" and gameBoard[8] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  elif gameBoard[2] == "X" and gameBoard[5] == "X" and gameBoard[8] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[2] == "O" and gameBoard[5] == "O" and gameBoard[8] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  elif gameBoard[1] == "X" and gameBoard[4] == "X" and gameBoard[7] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[1] == "O" and gameBoard[4] == "O" and gameBoard[7] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  elif gameBoard[3] == "X" and gameBoard[4] == "X" and gameBoard[5] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[3] == "O" and gameBoard[4] == "O" and gameBoard[5] == "O":
    titleLabel.config(text="O won!")
    playGame = False

  #checking diagonals
  elif gameBoard[0] == "X" and gameBoard[4] == "X" and gameBoard[8] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[0] == "O" and gameBoard[4] == "O" and gameBoard[8] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  elif gameBoard[2] == "X" and gameBoard[4] == "X" and gameBoard[6] == "X":
    titleLabel.config(text="X won!")
    playGame = False
  elif gameBoard[2] == "O" and gameBoard[4] == "O" and gameBoard[6] == "O":
    titleLabel.config(text="O won!")
    playGame = False
  
  #check whether its end of game and no one won 
  if clicksCount == 9 and playGame == True:
    titleLabel.config(text="No one won!")
    playGame = False

def restartGame():
  global currentUser
  global clicksCount
  global gameBoard
  global playGame
  for i in range(9):
    buttonsList[i].config(image=renderWhite)
  currentUser = "X"
  clicksCount = 0
  gameBoard = ["white", "white", "white", "white", "white", "white", "white", "white", "white"]
  playGame = True
  titleLabel.config(text="Tic Tac Toe")
  

button1 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 1))
button2 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 2))
button3 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 3))
button4 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 4))
button5 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 5))
button6 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 6))
button7 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 7))
button8 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 8))
button9 = Button(window, image=renderWhite, bg="white", command=partial(squarePressed, 9))

restartButton = Button(window, text="Restart Game", bg="white", command=restartGame)

button1.grid(row=2, column=1)
button2.grid(row=2, column=2)
button3.grid(row=2, column=3)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button7.grid(row=4, column=1)
button8.grid(row=4, column=2)
button9.grid(row=4, column=3)
restartButton.grid(row=5, column=1, columnspan=3)

buttonsList = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

window.mainloop()