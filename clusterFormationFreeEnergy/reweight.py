import numpy as np
import matplotlib.pyplot as plt

def calculate_fes(cv,bias,temperature,maxCV,minCV,binSize):
    kT = 8.617333262E-5*temperature
    beta = 1/(kT)
    logweights = beta*bias
    logweights -= np.amax(logweights)
    hist, bin_edges = np.histogram(cv,weights=np.exp(logweights),range=(minCV,maxCV),bins=int((maxCV-minCV)/binSize))
    bin_centers = (bin_edges[:-1]+bin_edges[1:])/2
    fes = -kT*np.log(hist)
    fes -= np.amin(fes)
    return bin_centers, fes


COLVAR = np.genfromtxt("./COLVAR")
cv = COLVAR[:,1]
bias = COLVAR[:,4] + COLVAR[:,-2]
temperature = 373
# From reweighting
maxCV=250
minCV=1
binSize=4
bin_centers,fes = calculate_fes(cv,bias,temperature,maxCV,minCV,binSize)
plt.plot(bin_centers,fes,label='{}_reweight'.format(f))

plt.legend()
plt.xlabel("Collective variable")
plt.ylabel("Free energy (Ev)")

plt.savefig('./{}_fes.png'.format(f),dpi=600)