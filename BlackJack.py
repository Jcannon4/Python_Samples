#BlackJack Proj
import random
import time
import sys

suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight','Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
print('Welcome to BlackJack by Jack Black.\nYour starting amount is $500.\nBlackJack pays out 3:2.')

class Card:
    
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return '{} of {}' .format(self.rank, self.suit)

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp
    
    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            j = random.randint(0, i + 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
            
    
    def draw(self):
        return self.deck.pop(0)

class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.decision = ''
        self.bust = False
    
    def hit(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def portgas_d_ace(self):
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.amount = 500
        self.bet = 0
    def win(self):
        self.amount += self.bet
    
    def lose(self):
        self.amount -= self.bet

def wager(chips):
    while True:
        try:
            chips.bet = int(input('How much would you like to wager?\n'))
        except ValueError:
            print('Enter a number!')
        else:
            if(chips.bet > chips.amount):
                print('You can\'t bet more money than you have. You have ${}' .format(chips.amount))
            elif(chips.bet < 0):
                print('Joel\'s a Hacker!!!')
            else:
                break
def hitstand(hand):
    while True:
        try:
            hand.decision = str(input('Would you like to hit, stand, or doubledown?(h/s/dd)\n'))
        except ValueError:
            print('Enter \'s\' for stand, \'h\' for hit, or \'dd\' for doubledown.')
        else:
            if (hand.decision not in ( 'h','s','dd')):
                print('Enter \'s\' for stand, \'h\' for hit, or \'dd\' for doubledown.')
            else:
                break

def ShowBoard(dealerhand, playerhand):
    
    print('Dealer\'s Hand: ')
    print('*Hidden*')
    for i in range(1, len(dealerhand.cards)):
        print(dealerhand.cards[i])
    print('\nYour Hand: ')
    for i in range(0, len(playerhand.cards)):
        print(playerhand.cards[i])
    print('Value: {}\n' .format(playerhand.value))

def ShowAll(dealerhand, playerhand):
    print('Dealer\'s Hand: ')
    for i in range(0, len(dealerhand.cards)):
        print(dealerhand.cards[i])
    print('Dealer\'s Value: {}' .format(dealerhand.value))
    print('\nYour Hand: ')
    for i in range(0, len(playerhand.cards)):
        print(playerhand.cards[i])
    print('Value: {}\n' .format(playerhand.value))
    
def Bust(hand, chips):
    if hand.value > 21:
            chips.amount -= chips.bet
            hand.bust = True
            print('Bust! You lost ${}, You have ${} left.' .format(chips.bet, chips.amount))

def BustDealer(hand, chips):
    if hand.value > 21:
        hand.bust = True
        chips.amount += chips.bet
        print('The Dealer has busted you Win! Your Total is ${}' .format(chips.amount))

player_chips = Chips()
while 1 == 1:
    #Instantiate a Deck obj and shuffle
    playing_deck = Deck()
    playing_deck.shuffle()
    
    #Create players chips object, then take wager from the player
    
    wager(player_chips)
    
    #Creating player hands
    dealer = Hand()
    player = Hand()
    
    #Dealing cards to player hands. Simulating the order, dealer, player, dealer, player
    player.hit(playing_deck.draw())
    dealer.hit(playing_deck.draw())
    player.hit(playing_deck.draw())
    dealer.hit(playing_deck.draw())
    
    ShowBoard(dealer,player)
    
    while playing:
        
        hitstand(player)
        if player.decision == 'h':
            player.hit(playing_deck.draw())
            player.portgas_d_ace()
            ShowBoard(dealer, player)
            Bust(player,player_chips)
        elif player.decision == 'dd':
            player.hit(playing_deck.draw())
            player.portgas_d_ace()
            player_chips.bet *= 2
            ShowBoard(dealer,player)
            Bust(player,player_chips)
            break
        else:
            ShowBoard(dealer,player)
            break
        if player.value > 21:
            break
    if player.bust == False:
        print('\n\nDealer\'s Turn...\n\n')
        time.sleep(3)
        ShowAll(dealer,player)
        while dealer.value < 17 :
            dealer.hit(playing_deck.draw())
            dealer.portgas_d_ace()
            ShowAll(dealer,player)
            BustDealer(dealer,player_chips)
            time.sleep(3)
    if(player.value > dealer.value and player.bust == False and dealer.bust == False):
        player_chips.amount += player_chips.bet
        print('Player has beat the dealer! Your Total is now ${}' .format(player_chips.amount))
    elif(player.value == dealer.value and player.bust == False and dealer.bust == False):
        print('Its a wash! Your total is now ${}' .format(player_chips.amount))
    elif(player.value < dealer.value and player.bust == False and dealer.bust == False):
        player_chips.amount -= player_chips.bet
        print('You Lost! Your amount is now ${}' .format(player_chips.amount))
    try:
        playagain = str(input('Would you like to keep playing? (y/n)'))
    except ValueError:
        print('Please enter \'y\' for yes or \'n\' to cash out.')
    else:
        if playagain == 'n':
            print('You have selected to cash out, here is your walk away money ${}' .format(player_chips.amount))
            sys.exit()
    continue
