##import unittest
from collections import deque
import time

def marble_game(players,turns,show_time=False):
    if show_time:
        start=time.perf_counter_ns()
    circle=deque([0])
    player=0
    score=[0]*players
    for marble in range(1,turns+1):
        if marble%23==0:
            circle.rotate(7)
            score[marble%players]+=marble+circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    if show_time:
        end=time.perf_counter_ns()
        print('Game took {} s to simulate.'.format((end-start)/1e9))
    return max(score)

##class TestMarbleGame(unittest.TestCase):
##    def test_examples(self):
##        self.assertEqual(marble_game(9,25),32)
##        self.assertEqual(marble_game(10,1618),8317)
##        self.assertEqual(marble_game(13,7999),146373)
##        self.assertEqual(marble_game(17,1104),2764)
##        self.assertEqual(marble_game(21,6111),54718)
##        self.assertEqual(marble_game(30,5807),37305)

if __name__=='__main__':
##    unittest.main()
    print('High score, game 1: {} points'.format(marble_game(405,70953)))
    print('High score, game 2: {} points'.format(marble_game(405,7095300)))
