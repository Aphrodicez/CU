order = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
suits = ["club", "diamond", "heart", "spade"]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(" + self.value + " " + self.suit + ")"

    def next1(self):
        if self.suit == "spade":
            return Card(order[(order.index(self.value) + 1) % len(order)], "club")
        return Card(self.value, suits[suits.index(self.suit) + 1])

    def next2(self):
        ret = self.next1()
        self.value, self.suit = ret.value, ret.suit

n = int(input())
cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())

print("----------")

for i in range(n):
    print(cards[i])

print("----------")

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])