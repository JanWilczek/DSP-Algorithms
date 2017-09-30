'''
FEEDBACK COMB FILTER
by Jan Wilczek
date: 30-09-2017
'''


# Filter's difference equation
# y[n] = b0 * x[n] - aM * y[n-M]

import delay_line

class FeedbackCombFilter:
    def __init__(self, b0, aM, order):
        self.b0 = b0
        self.aM = aM
        self.delay = delay_line.DelayLine(order - 1)    #-1 is necessary for the filter to work correctly
        self.y = 0

    def filter(self, x):
        self.y = self.b0 * x - self.aM * self.delay.delay(self.y)
        return self.y
