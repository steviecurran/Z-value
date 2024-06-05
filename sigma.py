#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 
import sys
import matplotlib.patches as patches

print("\nOnly accurate to p >~ 1e-5 [Z < 4.1], otherwise use (the much faster) C version [~/C/stats/Z-value]")
p = float(input("\nEnter p-value [e.g. 0.05 for 95% significance: "))
ot = str(input("\nOne [o] or two-sided [any other]: "))

if ot == "o":
    q = 0.5-p
    ot_text = "one-sided"
else:
    q = 0.5-(p/2)
    ot_text = "two-sided"

pi = np.pi;
norm = 1/((2*pi)**0.5)

npts = 100000 # struggles if this is too high

xi = 0 # inital x
xf = 10  # max sigma to start
yi = 0  # yalue

dx = (xf-xi)/npts           
x = [xi] # initialise with inital value
y = [yi]
y_sum = y
sum = 0
area = 0

j =0

plt.rcParams.update({'font.size': 14})
ax = plt.gca()
ax.set_xlim([-.2, xf])
ax.set_ylim([-0.02, 0.42])

for i in range(npts):
    x = i*dx
    y = norm*np.exp(-0.5*(x**2))
    ax.plot(x,y,'o', markersize=1, c = 'k')
    
    while(sum < q):
        y_sum = norm*np.exp(-0.5*((j*dx)**2))
        area =y_sum*dx

        sum = sum + area
        j = j+1

        rect = patches.Rectangle((dx*j,0), dx, y_sum, linewidth=1, edgecolor='r', facecolor='none') #x,y,width, height
        ax.add_patch(rect)

print("For p = %1.3f (%1.3e, %1.8f%% confidence, Z = %1.3f sigma)" % (p,p,100*(1-p), dx*j))
print("\nFor p = %1.3f (%1.3e), %1.8f%% confidence %s, Z = %1.3f sigma)" % (p,p,200*q,ot_text, dx*j))


'''
## PLOT
xlabel = xf - (xf-xi)/2.2; ylabel = 0.38;
text = "p = %1.3e $\Rightarrow$ Z = %1.2f$\sigma$" % (p,dx*j)
ax.text(xlabel,ylabel,text,fontsize = 12, horizontalalignment='left',verticalalignment='top') 
plt.xlabel('Z-value [$\sigma$]'); plt.ylabel('y')
png = "sigma_plot-p=%1.3e.png" % (p) #eps = "convert %s %s.eps" % (png, plot)
plt.savefig(png);  #os.system(eps);
#plt.show();print("Plot written to", png)
#plt.clf(); plt.cla(); plt.close()
'''
