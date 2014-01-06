import matplotlib
import matplotlib.pyplot as plt
xs = [3,5,10]
ys = [49,71,109]
plt.plot(xs,ys)
plt.xticks([3,5,10])
#plt.gca().invert_xaxis()
plt.xlabel("beam width")
plt.ylabel("nDCG higher")
plt.savefig('BMS1.png')
plt.close()