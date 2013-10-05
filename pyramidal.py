from itertools import chain
from neuron import h
Section = h.Section
load_mechanisms('.')

#-------- Model of mammalian cortical layer V pyramidal neuron --------#
# Based on PC Bush & TJ Sejnowski 1991's reduced model
# Original measurements from C Koch et al. 1990's cat V1 cortical neuron
# Implemented by Y Yamamura, 5 October 2013
#----------------------------------------------------------------------#

# Topology
soma	= Section()			# Create soma, apical, basilar
apical	= Section()
basilar	= Section()

apical.connect(soma, 1, 0)	# Connect apical(0) to soma(0)
basilar.connect(soma, 0, 0)	# Connect basilar(0) to soma(0)

# Geometry
soma.L		= 30	#
soma.nseg	= 1		#
soma.diam	= 30	#

apical.L	= 600
apical.nseg	= 23
apical.diam	= 1

basilar.L		= 200
basilar.nseg	= 5
basilar.diam	= 2

# Biophysics
for sec in h.allsec():
	sec.Ra	= 100	# ohm*cm
	sec.cm	= 1		# uF/cm2

soma.insert('na')
soma.insert('kdr')

for seg in chain(soma, apical, basilar):
	seg.insert('leak')
	seg.leak.el = -65	# mV
	
# Synaptic input
syn = h.AlphaSynapse(0.5, sec=soma)
syn.onset = 0.5
syn.gmax = 0.05
syn.e = 0

# Simulation control
h.dt = 0.025
h.tstop = 5
h.v_init = -65
h.celsius = 37

def initialize():
	h.finitialize(v_init)
	h.fcurrent()

def setup_record():
	vec['v'].record(soma(0.5)._ref_v)
	vec['t'].record(h._ref_t)

initialize()
setup_record()	
h.run()

# Plot voltage trace
import matplotlib as plt
plt.plot(vec['t'], vec['v'])
