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

p2p = []
p2b = []
b2p = []

for i in xrange(npyr): # excitatory connections
	for j in xrange(npyr):
		# NetCon(&source_v, synapse, threshold, delay, weight)
		p2p.append(h.NetCon(pyr[i].soma(0.5)._ref_v, pyr[j].ampa[0],-20,rand.gauss(1.2,0.6),wp2p[i][j]))
	for j in xrange(nbas):
		p2b.append(h.NetCon(pyr[i].soma(0.5)._ref_v, bas[j].ampa[0],-20,rand.gauss(1.2,0.6),wp2b[i][j]))

for i in xrange(nbas): # inhibitory connections
	for j in xrange(npyr):
		b2p.append(h.NetCon(bas[i].soma(0.5)._ref_v, pyr[j].gabaa[0],-20,rand.gauss(1.2,0.6),wb2p[i][j]))

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
