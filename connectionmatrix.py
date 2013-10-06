import random
import numpy as np
# def shuffle(x):
    # x = list(x)
    # random.shuffle(x)
    # return x

npyr = 400
nbas = 100
p2p = np.zeros([npyr,npyr])
p2b = np.zeros([npyr,nbas])
b2p = np.zeros([nbas,npyr])

plist = range(npyr)
blist = range(nbas)

for i in plist:
	nonzero = random.sample(plist,npyr/10)
	for j in nonzero:
		p2p[i][j] = random.gauss(1.0,0.5)

for i in plist:
	nonzero = random.sample(blist,nbas/10)
	for j in nonzero:
		p2b[i][j] = random.gauss(1.0,0.5)
		
for i in blist:
	nonzero = random.sample(plist,npyr/10)
	for j in nonzero:
		b2p[i][j] = random.gauss(4.0,2.0)
		
np.savetxt("p2p.csv", p2p, fmt='%0.9e', delimiter=',', newline='\n')
np.savetxt("p2b.csv", p2b, fmt='%0.9e', delimiter=',', newline='\n')
np.savetxt("b2p.csv", b2p, fmt='%0.9e', delimiter=',', newline='\n')