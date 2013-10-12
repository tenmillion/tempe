# Script for generating bash script :P 
# For preliminary exploration of internal weights
# for i in range(-4,2+1):
	# f = open('bash-auto'+str(i+4+1)+'.sh', 'w')
	# for j in range(-4,2+1):
		# for k in range(-4,2+1):
			# cmd='~/nrniv -c "pp=' + str(2**i) + '" -c "pb=' + str(2**j) + '" -c "bp=' + str(2**k) + '" init.hoc\n'
			# f.write(cmd)
	# f.close()
	
#For investigating temperature effects
# f = open('batch-auto.sh', 'w')
for i in range(-2, 4+1) : # 2**-2.5 to 2**1 times original bp wts
	f = open('batch-auto'+str(i+2+1)+'.sh', 'w')
	for j in range(10/4,36/4+1) : # 10 to 36 deg c, in 2 degC steps
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.015" -c "nmda=0.05" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.015" -c "nmda=0.1" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.015" -c "nmda=0.25" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.015" -c "nmda=1.0" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.050" -c "nmda=0.05" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.050" -c "nmda=0.1" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.050" -c "nmda=0.25" init.hoc\n'
		f.write(cmd)
		cmd='~/nrniv -c "degc=' + str(j*4) + '" -c "bp=' + str(2**(i/2.0)) + '" -c "pp=0.5" -c "pb=0.5" -c "ip=0.015" -c "ib=0.050" -c "nmda=1.0" init.hoc\n'
		f.write(cmd)
	f.close()
# f.close()

#f = open('temp-auto8.sh', 'w')
#for j in range(10/2,(37+1)/2): # 10 to 37 deg c, in 2 degC steps
#	cmd='~/nrniv -c "degc=' + str(j*2) + '" -c "bp=' + str(2**(3/2.0)) + '" init.hoc\n'
#	f.write(cmd)
#f.close()
