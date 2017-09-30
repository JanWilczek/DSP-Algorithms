'''
DELAY LINE IMPLEMENTATION
by Jan Wilczek
date: 30-09-2017

from: https://www.dsprelated.com/freebooks/pasp/Delay_Lines.html
'''
class DelayLine:
    # Constructor
    def __init__(self, order):
        self.M = order
        self.index = 0
        self.buffer = []
        for i in range(self.M):
            self.buffer.append(0)

    def delay(self, x):
        y = self.buffer[self.index]
        self.buffer[self.index] = x
        self.index += 1
        #if (self.index >= self.M): self.index -= self.M
        self.index %= self.M
        return y