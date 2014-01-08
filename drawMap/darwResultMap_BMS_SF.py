import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

width = [4,3,2,1]
BMS_Match_rate = [0.0733542319749, 0.139184952978 , 0.270219435737, 0.425078369906] 
Baseline_Match_rate = [ 0.0526645768025 ,0.0526645768025, 0.0526645768025 ,0.0526645768025]

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

plt.plot(width,BMS_Match_rate,'r--', label = 'beam search & stroke feature')
plt.plot(width, Baseline_Match_rate, 'b-', label = 'base line')

plt.legend(loc=2)

formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)

#plt.xticks([3,5,10])
plt.gca().invert_xaxis()
plt.xlabel("match rate")
plt.ylabel("noise size")
plt.savefig('BMS_SF_trand1.png')
plt.close()