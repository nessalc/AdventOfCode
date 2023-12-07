with open('input02.txt', encoding='utf-8') as fp:
    all = fp.read()

example1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


class Game:
    def __init__(self, id: int, red: int, green: int, blue: int) -> None:
        self._id = id
        self._red = red
        self._green = green
        self._blue = blue

    def possible(self, *, red=0, green=0, blue=0):
        if red >= self._red and green >= self._green and blue >= self._blue:
            return True
        return False

    def power(self):
        return self._red*self._green*self._blue

    def __str__(self):
        return f'<Game {self._id}: {self._red=}, {self._green=}, {self._blue=}>'


def createGameFromString(sampleString: str) -> Game:
    game, samples = sampleString.split(':')
    _, id = game.split()
    id = int(id)
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for sample in samples.split(';'):
        for blocks in sample.split(','):
            number, color = blocks.split()
            number = int(number)
            match color:
                case 'red':
                    if number > maxRed:
                        maxRed = number
                case 'green':
                    if number > maxGreen:
                        maxGreen = number
                case 'blue':
                    if number > maxBlue:
                        maxBlue = number
                case _:
                    print('oops')
    return Game(id, maxRed, maxGreen, maxBlue)


if __name__ == '__main__':
    games = all
    gameList = []
    for game in games.strip().split('\n'):
        gameList.append(createGameFromString(game))
    r, g, b = 12, 13, 14
    possibleGames = list(
        filter(lambda x: x.possible(red=r, green=g, blue=b), gameList))
    gameIds = list(map(lambda x: x._id, possibleGames))
    part1 = sum(gameIds)
    part2 = sum(map(lambda x: x.power(), gameList))
    print(f'{part1=}')
    print(f'{part2=}')
