import random
'''
The progrm serves a player vs computer
format of Black-Jack game.
'''
class card():
    '''
    This class will help to generate random cards
    from deck of cards and also the value associated
    with each card.
    '''
    def __init__(self):

        self.mydeck=['A','2','3','4','5','6','7','8','9','10','J','K','Q']
        self.mycards=['Spade','Hearts','Diamonds','Clubs']
    def generate_card(self):
    
        x=random.choice(self.mycards)
        y=random.choice(self.mydeck)
        z=y+x
        return z
        
    
    
class player(card):
    '''
    This class will inherit the card class and hence
    generate the cards associated with each player.
    '''
    def __init__(self):
        card.__init__(self)
        self.player_card1=self.generate_card()
        self.player_card2=self.generate_card()
        
print('Welcome to Black-Jack')
print('                    ')
credit=int(input("Enter the Player's Credit:"))
print('                    ')
    
while True:
    if(credit<0):
        print('Insufficient Credit')
        print('                    ')
        break

    Player=player()
    print('Players cards  are:{} {}'.format(Player.player_card1,Player.player_card2))
    valP=0
    for m in [Player.player_card1,Player.player_card2]:

            if m[0] in ['J','K','Q','1']:
                valP=valP+10
            elif m[0]=='A':
                c=int(input('Treat it as 1 or 11:'))
                print('                    ')
                valP=valP+c

            else:
                valP=valP+int(m[0])
    print('Players  card sum is:{}'.format(valP))
    print('                    ')



    Dealer=player()
    print("Dealer's first card is:{}".format(Dealer.player_card1))
    print('                    ')
    valD=0
    for n in [Dealer.player_card1,Dealer.player_card2]:

            if n[0] in ['J','K','Q','1']:
                valD=valD+10
            elif n[0]=='A':
                print('                    ')
                valD=valD+11

            else:
                valD=valD+int(n[0])

    


    while True:

        bet=int(input('PLace your Bet:'))
        print('                    ')
        credit=credit-bet
        if(valP==21):
            credit=credit+(bet*2)
            print('Black-Jack!!!!!PLayer Wins {}'.format(2*bet))
            print('                    ')
            break


        else:
            while (valP<21):
                choice=input('Stand or Hit:')
                if(choice=='Stand'):
                    print("Dealer's Second card and card value is: {} {}".format(Dealer.player_card2,valD))
                    print('                    ')
                    if(valP>valD):
                        print('Player Wins!!!!!')
                        credit=credit+(bet*2)
                        break
                    elif(valP==valD):
                        print("Push!!. No one wins")
                        print('                    ')
                        credit=credit+bet
                        break
                    else:
                        print("Player Loses!!!")
                        print('                    ')
                        break
                    break
                else:
                    next_card=Player.generate_card()
                    print("The new card is {}".format(next_card))
                    print('                    ')
                    if next_card[0] in ['J','K','Q','1']:
                        valP=valP+10
                    elif next_card[0]=='A':
                        c=int(input('Treat it as 1 or 11:'))
                        print('                    ')
                        valP=valP+c

                    else:
                        valP=valP+int(next_card[0])
                    print("New :{}".format(valP))

                    if(valP==21):
                        credit=credit+(bet*2)
                        print('Black-Jack!!!!!PLayer Wins {}'.format(2*bet))
                        print('                    ')
                        break
                    elif(valP>21):
                        print("Player Busted!!!!!")
                        print('                    ')
                        break
                    else:
                        continue
                break
        break
    cho=input('Want a regame?-Y or N:')
    print('                    ')
    if(cho=='Y'):
                
        continue
    else:
        break
                                