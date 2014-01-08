import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

width = [3,5,10,15,20,25]
BMS_Match_rate = [0.0326018808777,0.048275862069,0.0733542319749,0.0909090909091,0.114106583072, 0.139184952978] 
Baseline_Match_rate = [ 0.0219435736677,0.0294670846395  ,0.0526645768025 ,0.0689655172414,0.094670846395 ,0.116614420063]

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

plt.plot(width,BMS_Match_rate,'r--', label = 'beam search')
plt.plot(width, Baseline_Match_rate, 'b-', label = 'base line')

plt.legend(loc=2)

formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)

#plt.xticks([3,5,10])
#plt.gca().invert_xaxis()
plt.xlabel("match rate")
plt.ylabel("beam width")
plt.savefig('BMS_trand1.png')
plt.close()