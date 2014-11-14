import pylab
import math
import csv
def sig(w):
	return 1/(1+math.exp(-w))
def typeClass(i):
	if (i>=.5):
		return 1
	else:
		return 0







n=[]
error=[]

x2=[]
x1=[]

bestfit=[]
bestinput=[]
counter=0
alpha=1
matches=0
doesntmatch=0
w=[1,1,1]
x=[1,0,0]
with open('lin_sep.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		x[1]=float(row[0])
		x[2]=float(row[1])
		x1.append(x[1])
		x2.append(x[2])

		wCon=w[0]*x[0]+w[1]*x[1] +w[2]*x[2]
		n.append(counter)
		counter=counter+1
		error.append((float(row[2])-sig(wCon))**2)
		updateVal=typeClass(sig(wCon))
		for t in range(0,3):
			w[t]=w[t]+alpha*(float(row[2])-sig(wCon))*sig(wCon)*(1-sig(wCon))
		if(updateVal==float(row[2])):
			matches=matches+1
		else:
			doesntmatch=doesntmatch+1
		bestinput.append(x[1])
		bestfit.append(-(w[0]+w[1]+x[1])/w[2])
		print w
	
	print "Matches " + str(matches)
	print "Non-Mathces" + str(doesntmatch)
	pylab.plot(n,error)
	pylab.show()

	pylab.plot(bestinput,bestfit)
	pylab.plot(x1,x2)
	pylab.show()


n=[]
error=[]

x2=[]
x1=[]

bestfit=[]
bestinput=[]
counter=0
alpha=1
matches=0
doesntmatch=0
w=[1,1,1]
x=[1,0,0]
with open('non_lin_sep.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		x[1]=float(row[0])
		x[2]=float(row[1])
		x1.append(x[1])
		x2.append(x[2])

		wCon=w[0]*x[0]+w[1]*x[1] +w[2]*x[2]
		n.append(counter)
		counter=counter+1
		error.append((float(row[2])-sig(wCon))**2)
		updateVal=typeClass(sig(wCon))
		for t in range(0,3):
			w[t]=w[t]+alpha*(float(row[2])-sig(wCon))*sig(wCon)*(1-sig(wCon))
		if(updateVal==float(row[2])):
			matches=matches+1
		else:
			doesntmatch=doesntmatch+1
		bestinput.append(x[1])
		bestfit.append(-(w[0]+w[1]+x[1])/w[2])
		print w
	
	print "Matches " + str(matches)
	print "Non-Mathces" + str(doesntmatch)
	pylab.plot(n,error)
	pylab.show()

	pylab.plot(bestinput,bestfit)
	pylab.plot(x1,x2)
	pylab.show()