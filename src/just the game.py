import random

deck = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]}

flop = {1: [],
        2: [],
        3: [],
        4: []}

transactions: {}


def burn(deck):
    suit = deck.get(random.randint(1, 4))
    popped = []
    popped.append(suit)
    popped.appent(suit.pop(random.randint(0, len(suit) - 1)))
    if len(suit) <= 0:
        deck.pop(suit)
    return popped


def deal(deck, hand):
    temp = burn(deck)
    hand[temp[0]].append(temp[1])


def check(hand):
    for i in flop.keys():
        for v in flop[i]:
            hand[i].append(v)

    temp = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    tempsuits = {1: 0, 2: 0, 3: 0, 4: 0}
    consecutive = []
    temparr = []
    last = 0
    FH = []
    for i in hand.keys():
        for v in hand[i]:
            if not temparr:
                temparr.append(v)
            elif len(temparr) == 5:
                consecutive.append(temparr)
                temparr = []
            elif v != last + 1:
                temparr = []
            temp[v] += 1
            tempsuits[i] += 1
            last = v
    for pairs in consecutive:
        if pairs[0] == 10:
            return 10
    if consecutive:
        return 9
    elif temp.values().contains(4):
        return 8
    for i in temp.keys():
        if temp[i]>=2:
            FH.append(i)
    if len(FH>=2) and temp.values().contains(3):
        return 7
    for i in tempsuits.keys():
        if tempsuits[i]>=5:
            return 6
    last = 0
    temparr = []
    for i in temp.keys():
        if temp[i]!=0:
            if last == 0:
                last = i
                temparr.append(i)
            elif len(temparr) == 5:
                return 5
            elif i != last + 1:
                temparr=[]
                temparr.append(i)
                last=i
    if temp.values().contains(3):
        return 4
    if len(FH)>=2:
        return 3
    if temp.values().contains(2):
        return 2
    return 1

def bet(player, amount, pot):
    player.Money = player.Money-amount
    pot+=amount
    transactions[player].append(amount)

class Player():
    Money=15000
    Hand = {1:[], 2:[], 3:[], 4:[]}

def main():
    input("How much money do you want to bet?")