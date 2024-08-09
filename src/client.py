import pygame
import random

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
clientNumber = 0
# Deck will be a dictionary of cards, where cards are randomly chosen
# 1, 2, 3, and 4 can be spades, hearts, diamonds, and clovers in whatever order we want
# 11 = J, 12 = Q, 13 = K, 14 = A
deck = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}

def burn(deck):
    suit = deck.get(random.randint(1, 4))
    if len(suit) <= 0:
        burn(deck)
    suit.pop(random.randint(0, len(suit)-1))

def deal(deck, hand):
    suit = random.randint(1, 4)
    hand[suit].append(deck.get(suit).pop(random.randint(0, len(deck[suit]))))
# Add a card to a player's hand and pop it from the deck

# Player must have a hand and money
# When community cards are drawn, add to all players' hands

def check(hand):
    temphand = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    Samesuit5 = False
    for suit in range(hand):
        arr = hand[suit]
        if len(arr) >= 5:
            Samesuit5 = True
        for value in arr:
            temphand[value] += 1
    if 4 in temphand:
        return "4 of a Kind"
    if 3 in temphand and 2 in temphand: #This one is kind of inaccurate, update later
        return "Full House"
    if Samesuit5:
        return "Flush"
    #Straight
    if 3 in temphand:
        return "3 of a Kind"
    #2 pair
    if 2 in temphand:
        return "2 of a Kind"

    return "High Card"



class Player ():
    hand = {1: [],
            2: [],
            3: [],
            4: []}
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        val = 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= val
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += val
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= val
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += val
        self.rect = (self.x, self.y, self.width, self.height)

def redraw(win, player):
    window.fill((255, 255, 255))
    clock = pygame.time.Clock()
    clock.tick(60)
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    player = Player(50, 50, 100, 100, (0, 255, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw(window, player)

main()
                