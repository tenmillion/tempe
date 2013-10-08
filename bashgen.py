# Script for generating bash script :P
for i in range(-4,2+1):
	f = open('bash-auto'+str(i+4+1)+'.sh', 'w')
	for j in range(-4,2+1):
		for k in range(-4,2+1):
			cmd='~/nrniv -c "pp=' + str(2**i) + '" -c "pb=' + str(2**j) + '" -c "bp=' + str(2**k) + '" init.hoc\n'
			f.write(cmd)
	f.close()