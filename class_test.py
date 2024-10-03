import random

class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__(self):
    return f"{self.rank} of {self.suit}"

class Deck:
  def __init__(self):
    self.cards   
 = []
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds",   
 "Clubs", "Spades"]

    for rank in ranks:
      for suit in suits:
        self.cards.append(Card(rank, suit))

  def shuffle(self):
    random.shuffle(self.cards)

  def deal_card(self):
    return self.cards.pop()

class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []

  def add_card(self, card):
    self.hand.append(card)

  def   
 hand_value(self):
    value = 0
    num_aces = 0

    for card in self.hand:
      if card.rank   
 == "Ace":
        num_aces += 1
        value += 11
      elif card.rank in ["Jack", "Queen", "King"]:
        value += 10
      else:
        value += int(card.rank)

    while value > 21 and num_aces > 0:
      value -= 10
      num_aces -= 1

    return value   


class Blackjack:
  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.player = Player("Player")
    self.dealer = Player("Dealer")

  def deal_initial_cards(self):
    self.player.add_card(self.deck.deal_card())
    self.dealer.add_card(self.deck.deal_card())
    self.player.add_card(self.deck.deal_card())   


  def player_turn(self):
    while self.player.hand_value() < 21:
      print(f"{self.player.name}'s hand: {self.player.hand}")
      print(f"{self.player.name}'s hand value: {self.player.hand_value()}")
      choice = input("Hit or stand? (h/s): ")

      if choice == "h":
        self.player.add_card(self.deck.deal_card())
      elif choice == "s":
        break
      else:
        print("Invalid choice. Please enter 'h' or 's'.")

  def dealer_turn(self):
    while self.dealer.hand_value() < 17:
      self.dealer.add_card(self.deck.deal_card())

  def determine_winner(self):
    player_value = self.player.hand_value()
    dealer_value = self.dealer.hand_value()

    if player_value > 21:
      print("Player busts! Dealer wins.")
    elif dealer_value > 21:
      print("Dealer busts! Player wins.")
    elif player_value > dealer_value:
      print("Player wins!")
    elif   
 dealer_value > player_value:
      print("Dealer wins!")
    else:
      print("It's a   
 tie!")

  def play(self):
    self.deal_initial_cards()

    print(f"{self.player.name}'s hand: {self.player.hand}")
    print(f"{self.player.name}'s hand value: {self.player.hand_value()}")
    print(f"Dealer's hand: {self.dealer.hand[0]}")

    self.player_turn()

    if self.player.hand_value() <= 21:
      self.dealer_turn()

    self.determine_winner()

if __name__ == "__main__":
  game = Blackjack()
  game.play()
