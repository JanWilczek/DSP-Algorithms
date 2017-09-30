import delay_line
import feedforward_comb_filter
import feedback_comb_filter

x = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]

delay = delay_line.DelayLine(3)
print("Delay line output at the given index: ")
for i in range(len(x)):
    print("Index: ", i, " Output: ", delay.delay(x[i]))

print('\n' * 2)

feedforwardcombfilter = feedforward_comb_filter.FeedforwardCombFilter(0.1,0.5,4)
print("Feedforward comb filter output at the given index: ")
for i in range(len(x)):
    print("Index: ", i, " Output: ", feedforwardcombfilter.filter(x[i]))

print('\n' * 2)

feedbackcombfilter = feedback_comb_filter.FeedbackCombFilter(0.5, 0.9, 3)
print("Feedforward comb filter output at the given index: ")
for i in range(len(x)):
    print("Index: ", i, " Output: ", feedbackcombfilter.filter(x[i]))