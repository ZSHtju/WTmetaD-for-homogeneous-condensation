import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b):
    return a*x+b

COLVAR=np.genfromtxt("./COLVAR")
cv=COLVAR[:,1]
bias=COLVAR[:,3]
temperature=373
kT=8.617333262E-5*temperature
beta=1/(kT)
logweights = beta*bias
logweights -= np.amax(logweights)
histmin=10
histmax=30
nbins=20
histo, bin_edges = np.histogram(cv,weights=np.exp(logweights),range=(histmin,histmax),bins=nbins)
err = np.sqrt(np.histogram(cv,weights=np.power(np.exp(logweights),2), bins=nbins, range=(histmin,histmax))[0])
bin_centers=(bin_edges[:-1]+bin_edges[1:])/2
fes = -kT*np.log(histo)
offset = np.mean(np.ma.masked_invalid(fes))
fes -= offset
plt.plot(bin_centers,fes,label='373 K')
feserr = (1/beta)*err/histo
plt.fill_between(bin_centers,fes-3*feserr, fes+3*feserr,linewidth=0, alpha=0.5)
if(fes[np.isfinite(fes)].shape[0] > 0):
    popt, pcov = curve_fit(func, bin_centers[np.isfinite(fes)], fes[np.isfinite(fes)], sigma=feserr[np.isfinite(fes)])
    x=np.linspace(histmin,histmax,20)
    plt.plot(x,func(x,*popt),'--',color='black',alpha=0.5)
plt.legend(fontsize=12)
plt.xlabel("#Atom like gas",fontsize=12)
plt.ylabel("Free energy [ev]",fontsize=12)
plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks([10,15,20,25,30])

plt.savefig('./OPC_fes.png',dpi=300,bbox_inches='tight')