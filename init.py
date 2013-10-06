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

h("""
npyr = 400
nbas = 100

objectvar pyr[npyr]
for i = 0, npyr-1 {
    pyr[i] = new Pyramidal()
}
objectvar bas[nbas]
for i = 0, nbas-1 {
    bas[i] = new Basket()
}

objref p2pfile, p2bfile, b2pfile, r
r = new Random()
r.normal(1.2, 0.6)
p2pfile = new File()
p2bfile = new File()
p2pfile.ropen("p2p.dat")
p2bfile.ropen("p2b.dat")
for i = 0, npyr-1 {
    for j = 0, npyr-1 { // Set pyramidal -> pyramidal weights
        p2pwt = p2pfile.scanvar()
        if p2pwt > 0 {
            dl = abs(r.repick())
            pyr[i].soma pyr[j].nclist.append(new NetCon(&v(0.5), pyr[j].ampa[0],-20, dl, p2pwt))
        }
    for j = 0, nbas-1 { // Set pyramidal -> basket weights
        p2bwt = p2bfile.scanvar()
        if p2bwt > 0 {
            dl = abs(r.repick())
            pyr[i].soma bas[j].nclist.append(new NetCon(&v(0.5), bas[j].ampa[0],-20, dl, p2bwt))
        }
    }
}
p2pfile.close()
p2bfile.close()
b2pfile = new File()
b2pfile.ropen("b2p.dat")
for i = 0, nbas-1 {
    for j = 0, npyr-1 { // Set basket -> pyramidal weights
        b2pwt = b2pfile.scanvar()
        if b2pwt > 0 {
            dl = abs(r.repick())
            bas[i].soma pyr[j].nclist.append(new NetCon(&v(0.5), pyr[j].ampa[0],-20, dl, b2pwt))
        }
    }
}
b2pfile.close()

""")

print len(h.pyr[1].nclist), len(h.bas[1].nclist)
	
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
