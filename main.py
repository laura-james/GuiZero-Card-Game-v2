#download card images from here https://code.google.com/archive/p/vector-playing-cards/downloads
#help on guizero from here https://lawsie.github.io/guizero/
#stuff we did in lessons of guizero can be found here : https://kesbath.fireflycloud.net/computing--ict/programming-ideas/python (scroll to bottom part where ppts live)


from guizero import App, Text, TextBox, PushButton ,Picture
import random
from classes import Card, Deck
myDeck = Deck()
myDeck.displayDeck()
            
def do_something(): 
   if tbox.value == "Bob":
      message.value = "Welcome Bob"
      app.bg = "green"
      tbox.bg = "white"
   else:
      message.value = "You're not Bob!"
      app.bg = "red"
      tbox.bg = "white"
      
def deal():
  #random picks ones of the suits and shows the 2 or that suit
  mylist=["clubs","diamonds","hearts","spades"]
  choice = random.choice(mylist)
  card1.image = "2_of_"+choice+".png"
  
  

app = App(title="Welcome - only if you're called Bob",layout="grid") 
message = Text(app, text="Enter your name!",grid=[0,50])
tbox = TextBox(app, grid=[10,50])
tbox.bg = "white"

button = PushButton(app, text="Press me", command=do_something, grid=[50,50])
dealbutton = PushButton(app, text="Deal", command=deal, grid=[50,100])



card1 = Picture(app, image="red_joker.png", grid=[100,130], width=150, height=219) 


app.display() # this must be last
