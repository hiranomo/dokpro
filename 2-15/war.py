from random import shuffle

class Card:
    values = [None,None,2,3,4,5,6,7,8,9,10,'jack','queen','king','ase']
    suits = ['spead','hart','diamond','crab']
    def __init__(self,v,s):
        self.value = v
        self.suit = s
    def __lt__(self,c2):
        if self.value == c2.value:
            return self.suit < c2.suit
        return self.value < c2.value
    def __ge__(self,c2):
        if self.value == c2.value:
            return self.suit > c2.suit
        return self.value > c2.value
    def __repr__(self):
        return '{} of {}'.format(self.values[self.value],self.suits[self.suit])

class Deck:
    cards = []
    def __init__(self):
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def draw(self):
        if 0 == self.cards:
            return
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1 = input('Player1の名前を入力 >')
        name2 = input('Player2の名前を入力 >')
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()
    def raund_winner(self,p1,p2):
        if self.p1.card > self.p2.card:
            winner = self.p1.name
            self.p1.wins += 1
        else:
            winner = self.p2.name
            self.p2.wins += 1
        print('このラウンドは{}の勝ち！'.format(winner))
    def game_winner(self,p1,p2):
        w = 'ゲーム終了、{}対{}で{}の勝ち！'
        if self.p1.wins == self.p2.wins:
            print('ゲーム終了、引き分け！')
        elif self.p1.wins > self.p2.wins:
            winner = self.p1.name
            print(w.format(self.p1.wins,self.p2.wins,winner))
        else:
            winner = self.p2.name
            print(w.format(self.p2.wins,self.p1.wins,winner))
    def play_game(self):
        cards = self.deck.cards
        m = ''
        print('ゲームを開始します。')
        while len(cards) > 0:
            if m == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            print('{}は{}、{}は{}を引きました。'.format(self.p1.name,self.p1.card,
                                                    self.p2.name,self.p2.card))
            self.raund_winner(self.p2,self.p1)
            m = input('qキーで終了、それ以外のキーでplay >')
        self.game_winner(self.p1,self.p2)

game = Game()
game.play_game()
