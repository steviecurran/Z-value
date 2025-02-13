#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 
import sys
from scipy import stats
from scipy.stats import norm
import matplotlib.patches as patches

print("\nIf naumbers are low and inf is returned, use the C version [~/C/stats/Z-value]")

p = float(input("\nEnter p-value [e.g. 0.05 for 95% significance: "))
ot = str(input("\nOne [o] or two-sided [any other]: "))

if ot == "o":
    p = p
else:
    p = p/2
    
Z = norm.ppf(1-p,loc=0,scale=1) 

print("For p = %1.3g (%1.3e, %1.8f%% confidence, Z = %1.3f sigma)" % (p,p,100*(1-p), Z))

