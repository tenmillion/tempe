import numpy as np
from matplotlib import pyplot as plt
import sys

temp=np.loadtxt(sys.argv[1],dtype='float',skiprows=1,delimiter=' ',usecols=(1,2))
data=np.transpose(temp)

plt.scatter(data[0],data[1],s=1,c='k',marker='.')
plt.show()
