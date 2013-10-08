# Script for setting up connection matrix for netconst.hoc
# Also generates corresponding delays in addition.
# Weights are in nS. Must be scaled by 0.001 to be used with default synapses which have g in uS.

import random
import numpy as np
# def shuffle(x):
    # x = list(x)
    # random.shuffle(x)
    # return x

# Todo: make so that settings(min max step for each param) can be read from file
# Todo: loop entire process over each step in each range for each param
# Todo: output params used into a local database using sqlite, for later plotting and data management
	
npyr = 400
nbas = 100
mupp = 1.0 # nS
mupb = 1.0 # nS
mubp = 4.0 # nS
mudl = 1.2 # ms
mindl = 0.5 # ms

p2p = np.zeros([npyr,npyr])
p2b = np.zeros([npyr,nbas])
b2p = np.zeros([nbas,npyr])
p2pdl = np.zeros([npyr,npyr])
p2bdl = np.zeros([npyr,nbas])
b2pdl = np.zeros([nbas,npyr])

plist = range(npyr)
blist = range(nbas)

for i in plist:
	nonzero = random.sample(plist,npyr/10)
	for j in nonzero:
		p2p[i][j] = max(0,random.gauss(mupp,mupp/2.0))
		p2pdl[i][j] = max(mindl,random.gauss(mudl,mudl/2.0))

for i in plist:
	nonzero = random.sample(blist,nbas/10)
	for j in nonzero:
		p2b[i][j] = max(0,random.gauss(mupb,mupb/2.0))
		p2bdl[i][j] = max(mindl,random.gauss(mudl,mudl/2.0))
		
for i in blist:
	nonzero = random.sample(plist,npyr/10)
	for j in nonzero:
		b2p[i][j] = max(0,random.gauss(mubp,mubp/2.0))
		b2pdl[i][j] = max(mindl,random.gauss(mudl,mudl/2.0))
		
np.savetxt("p2p.dat", p2p, fmt='%.9f', delimiter=' ', newline='\n')
np.savetxt("p2b.dat", p2b, fmt='%.9f', delimiter=' ', newline='\n')
np.savetxt("b2p.dat", b2p, fmt='%.9f', delimiter=' ', newline='\n')

np.savetxt("p2pdl.dat", p2pdl, fmt='%.4f', delimiter=' ', newline='\n')
np.savetxt("p2bdl.dat", p2bdl, fmt='%.4f', delimiter=' ', newline='\n')
np.savetxt("b2pdl.dat", b2pdl, fmt='%.4f', delimiter=' ', newline='\n')