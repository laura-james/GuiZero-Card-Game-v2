
class Card:
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        self.image = str(number)+"_of_"+suit+".png"
    def display(self):
        print(self.suit,self.number)

class Deck:
    def __init__(self):
        self.cards = []
        #just creates clubs

        for i in range(1,13):
            if i == 10:
                self.cards.append(Card("clubs","J"))
            elif i == 11:
                self.cards.append(Card("clubs","Q"))
            elif i == 12:
                self.cards.append(Card("clubs","K"))
            else:
                self.cards.append(Card("clubs",i))
    def displayDeck(self):
        for c in self.cards:
            c.display()