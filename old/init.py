from itertools import chain
from neuron import h
import random as rand
import numpy as np
#from nrn import *

#-------- Revamped Bush et al. 1999 Model --------#
# Implemented by Y Yamamura, 6 October 2013       #
#-------------------------------------------------#

#h.xopen("pyramidal.hoc")
#h.xopen("basket.hoc")
#h.xopen("netconst.hoc")

print len(h.pyr[1].nclist), len(h.bas[1].nclist)
	
h.load_file("stdrun.hoc")
# Simulation control
# h('celsius = 23')
# dt = 0.025
# h.v_init = -65
# h.tstop = 5
# h.init()
#	finitialize(v_init)
#	fcurrent()

# vec = {} # Needs to be outside a function
# for var in 'v','t':
	# vec[var] = h.Vector()

# vec['v'].record(soma(0.5)._ref_v)
# vec['t'].record(h._ref_t)

# initialize()
# h.run()

# Plot voltage trace
# import matplotlib.pyplot as plt
# plt.figure(1, figsize=(6,6))
# plt.plot(vec['t'], vec['v'])
# plt.show()
