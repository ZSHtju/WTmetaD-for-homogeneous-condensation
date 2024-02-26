import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./COLVAR', skiprows=1, sep='\s+', names=['time', 'c1.lessthan', 'mt.bias', 'mt.rbias', 'mt.rct', 'uwall.bias', 'uwall.force2'])
plt.plot(data['time']/1000, data['c1.lessthan'])
plt.xlabel('Time [ns]', fontsize=12)
plt.ylabel('#Atom like gas', fontsize=12)
plt.autoscale(enable=True, axis='x''y')
plt.savefig('./CV_change.png', dpi=300, bbox_inches='tight')