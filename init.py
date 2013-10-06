from itertools import chain
from neuron import h
import random as rand
import numpy as np
#from nrn import *

#-------- Revamped Bush et al. 1999 Model --------#
# Implemented by Y Yamamura, 6 October 2013       #
#-------------------------------------------------#

h.xopen("pyramidal.hoc")
h.xopen("basket.hoc")
h.load_file("stdrun.hoc")

npyr = 400
nbas = 100

pyr = [h.Pyramidal() for i in xrange(npyr)]
bas = [h.Basket() for i in xrange(nbas)]

# Load weights from file
wp2p = np.loadtxt("p2p.csv", dtype='float', delimiter=',')
wp2b = np.loadtxt("p2b.csv", dtype='float', delimiter=',')
wb2p = np.loadtxt("b2p.csv", dtype='float', delimiter=',')

delay = abs(rand.gauss(1.2,0.6))
weight = abs(wp2p[i][j])
pre = pyr[i]
post = pyr[j]
# NetCon(&source_v, synapse, threshold, delay, weight)
h('pre.soma nc = new NetCon(&v(0.5), post.ampa[0],-20,delay,weight)'

print len(p2p), len(p2b), len(b2p)
	
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
