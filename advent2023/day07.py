import logging
from functools import total_ordering
from dataclasses import dataclass
from typing import Self
from enum import IntEnum, unique, auto
from collections import Counter
from pprint import pprint

logging.basicConfig(filename='day07.log',
                    format='[%(asctime)s] %(message)s', level=logging.INFO)

with open('input07.txt', encoding='utf-8') as fp:
    all = fp.read()

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

card_ranks = "AKQJT98765432"
card_ranks_joker = "AKQT98765432J"


@unique
class HandType(IntEnum):
    FIVE_OF_A_KIND = auto()
    FOUR_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    THREE_OF_A_KIND = auto()
    TWO_PAIR = auto()
    ONE_PAIR = auto()
    HIGH_CARD = auto()


camel_cards = all


@total_ordering
@dataclass
class CamelCards:
    cards: str
    bid: int
    type: HandType

    def __init__(self, cards, bid, *, joker_rule=False):
        self.cards = cards
        self.bid = bid
        self.type = self.find_type(joker_rule)
        if not joker_rule:
            self.card_ranks = card_ranks
        else:
            self.card_ranks = card_ranks_joker

    def find_type(self, joker_rule) -> HandType:
        ctr = Counter(self.cards)
        if joker_rule:
            ctr_no_jack = ctr-Counter('J'*ctr['J'])
            try:
                ctr = ctr_no_jack + \
                    Counter(ctr_no_jack.most_common(1)[0][0]*ctr['J'])
            except IndexError:
                pass
        c = ctr.most_common()
        _, counts = zip(*c)
        if counts[0] == 5:
            type = HandType.FIVE_OF_A_KIND
        elif counts[0] == 4:
            type = HandType.FOUR_OF_A_KIND
        elif counts[0] == 3 and counts[1] == 2:
            type = HandType.FULL_HOUSE
        elif counts[0] == 3:
            type = HandType.THREE_OF_A_KIND
        elif counts[0] == 2 and counts[1] == 2:
            type = HandType.TWO_PAIR
        elif counts[0] == 2:
            type = HandType.ONE_PAIR
        else:
            type = HandType.HIGH_CARD
        return type

    def __lt__(self, other: Self):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        else:
            for a, b in zip(self.cards, other.cards):
                if a == b:
                    continue
                if self.card_ranks.find(a) < self.card_ranks.find(b):
                    return True
                return False

    def __eq__(self, other: Self):
        return self.cards == other.cards


hands1 = [CamelCards(hand, int(bid), joker_rule=False) for hand, bid in [
    cards.split() for cards in camel_cards.strip().split('\n')]]
hands2 = [CamelCards(hand, int(bid), joker_rule=True) for hand, bid in [
    cards.split() for cards in camel_cards.strip().split('\n')]]

part1 = 0
for rank, hand in enumerate(sorted(hands1, reverse=True), start=1):
    part1 += rank*hand.bid
print(f'{part1=}')
logging.info(f'{part1=}')

part2 = 0
for rank, hand in enumerate(sorted(hands2, reverse=True), start=1):
    part2 += rank*hand.bid
print(f'{part2=}')
logging.info(f'{part2=}')
