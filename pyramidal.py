from itertools import chain
from neuron import *
from nrn import *
#h.nrn_load_dll('./i686/.libs/libnrnmech.so')

#-------- Model of mammalian cortical layer V pyramidal neuron --------#
# Based on PC Bush & TJ Sejnowski 1991's reduced model
# Original measurements from C Koch et al. 1990's cat V1 cortical neuron
# Implemented by Y Yamamura, 5 October 2013
#----------------------------------------------------------------------#

# Topology
soma	= h.Section()		# Create soma, apical, basilar
apical	= h.Section()
basilar	= h.Section()

apical.connect(soma, 1, 0)	# Connect apical(0) to soma(0)
basilar.connect(soma, 0, 0)	# Connect basilar(0) to soma(0)

# Geometry
soma.L		= 30	# umeter?
soma.nseg	= 1	#
soma.diam	= 30	#

apical.L	= 600
apical.nseg	= 23
apical.diam	= 1

basilar.L	= 200
basilar.nseg	= 5
basilar.diam	= 2

# Biophysics
for sec in h.allsec():
	sec.Ra	= 100	# ohm*cm
	sec.cm	= 1   	# uF/cm2

soma.insert('traub')
#soma.insert('kdr')
#soma(0.5).na.gnabar = 3000.0
#soma(0.5).kdr.gkbar = 2500.0

#soma.insert('leak')
#apical.insert('leak')
#basilar.insert('leak')

#for seg in chain(soma, apical, basilar):
#	seg.leak.el = -65  # mV

#soma.insert('hh')
#soma.insert('pas')
#apical.insert('pas')
#basilar.insert('pas')

#for seg in chain(soma, apical, basilar):
#	seg.pas.e = -65  # mV
	
# Synaptic input
syn = h.AlphaSynapse(0.5, sec=soma)
syn.onset = 0.5
syn.gmax = 0.05
syn.e = 0

# Simulation control
celsius = 37

def initialize():
	h.load_file("stdrun.hoc")
	dt = 0.025
	h.v_init = -65
	h.tstop = 5
	h.init()
#	finitialize(v_init)
#	fcurrent()

vec = {} # Needs to be outside a function
for var in 'v','t':
	vec[var] = h.Vector()
vec['v'].record(soma(0.5)._ref_v)
vec['t'].record(h._ref_t)

initialize()
h.run()

# Plot voltage trace
import matplotlib.pyplot as plt
plt.figure(1, figsize=(6,6))
plt.plot(vec['t'], vec['v'])
plt.show()
