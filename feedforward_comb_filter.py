'''
FEEDFORWARD COMB FILTER IMPLEMENTATION
by Jan Wilczek
date: 30-09-2017
'''

# Filter's difference equation
# y[n] = b0 * x[n] + bM * x[n-M]

import delay_line

class FeedforwardCombFilter:
    def __init__(self, b0, bM, order):
        self.b0 = b0
        self.bM = bM
        self.delay = delay_line.DelayLine(order)

    def filter(self, x):
        return self.b0*x + self.bM * self.delay.delay(x)