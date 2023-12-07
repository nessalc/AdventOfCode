from dataclasses import dataclass

with open('input04.txt', encoding='utf-8') as fp:
    all = fp.read()

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

cards = all


class Match:
    match_count: int

    def __init__(self, winners: list, scratches: list):
        self.match_count = len(set(winners).intersection(set(scratches)))

    def points(self) -> int:
        return int(2**(self.match_count-1))

    def __repr__(self):
        return f'<Match ({self.match_count})>'


@dataclass
class CardSet:
    match: Match
    count: int = 1


cardset_list = []
for card in cards.strip().split('\n'):
    _, numbers = card.split(':')
    winners, scratches = numbers.split('|')
    cardset_list.append(CardSet(Match(winners.split(), scratches.split())))
for idx, cardset in enumerate(cardset_list):
    for nc in range(idx+1, idx+cardset.match.match_count+1):
        cardset_list[nc].count += 1*cardset.count

part1 = sum(map(lambda x: x.match.points(), cardset_list))
part2 = sum(map(lambda x: x.count, cardset_list))

print(f'{part1=}')
print(f'{part2=}')
