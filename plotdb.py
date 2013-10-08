import sqlite3 as sql
import os
import matplotlib.pyplot as plt
import numpy as np

# Read file names and param values from DB
if not os.path.isfile('output.db'):
	print 'No output.db found.'
	exit()
	
conn = sql.connect('output.db')
c = conn.cursor()

# DB structure:
# output (filename text PRIMARY KEY,
# temp real, inp real, inb real, pp real, pb real, bp real )

# Plot by any two dimensions of the parameter space
# Todo: specify params from command line

dim1 = 'inp'
dim2 = 'inb'
temp = 37
pp = 1
pb = 1
bp = 1

print 'Creating 2D supspace...'
c.execute('DROP VIEW t1')
c.execute('DROP VIEW t2')
c.execute('DROP VIEW t3')
c.execute('DROP VIEW subspace')
c.execute('CREATE VIEW t1 AS SELECT * FROM output WHERE temp='+str(temp))
c.execute('CREATE VIEW t2 AS SELECT * FROM t1 WHERE pp='+str(pp))
c.execute('CREATE VIEW t3 AS SELECT * FROM t2 WHERE pb='+str(pb))
c.execute('CREATE VIEW subspace AS SELECT * FROM t3 WHERE bp='+str(bp))

ndim1=c.execute('SELECT DISTINCT COUNT('+dim1+') FROM subspace').fetchone()[0]
ndim2=c.execute('SELECT DISTINCT COUNT('+dim2+') FROM subspace').fetchone()[0]
print 'Will generate', ndim1, 'by', ndim2, 'matrix of scatter plots.'
print '( dim1 =', dim1, ', dim2=', dim2, ')'

print 'Reading file names...'
flist = []
tlist = []
for distinctd1 in c.execute('SELECT DISTINCT '+dim1+' FROM subspace'):
	ftemp = []
	ttemp = []
	for entry in c.execute('SELECT filename, '+dim1+', '+dim2+' FROM subspace WHERE '+dim1+'=? ORDER BY '+dim2+' DESC', distinctd1):
		ftemp.append(entry[0])
		ttemp.append(dim1+'='+str(entry[1])+', '+dim2+'='+str(entry[2]))
		print entry[0]
	flist.append(ftemp)
	tlist.append(ttemp)

# Read from files and plot

fig = plt.figure() 
for i in range(ndim1):
	for j in range(ndim2):
		spikes = np.transpose(np.loadtxt(str(flist[i][j]),dtype='float',skiprows=1,delimiter=' ',usecols=(1,2)))
		ax = fig.add_subplot(ndim2,ndim1,i*ndim2+j+1)
		ax.scatter(spikes[0],spikes[1],s=1,c='k',marker='.')
		ax.set_title(tlist[i][j],size='6')
		print j
		print i
plt.show()
	
# conn.commit()
# conn.close()