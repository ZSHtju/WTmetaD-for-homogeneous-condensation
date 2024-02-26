import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('./COLVAR', skiprows = 1,sep='\s+',names=['time', 'clust1.sum', 'nat', 'mt.bias', 'mt.rbias', 'mt.rct', 'uwall.bias', 'uwall.force2'])
#print(data)
plt.scatter(data['time']/1000,data['clust1.sum'],s = 5,label = 'CV Change')
plt.xlabel("Time(ns)")
plt.ylabel("CV  Change")
plt.legend()  
plt.autoscale(enable=True, axis='x' 'y')
plt.savefig("./CV_change.png",dpi = 600,bbox_inches='tight')