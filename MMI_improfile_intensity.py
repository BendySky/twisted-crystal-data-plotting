import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = ''

CB_0deg = f'{data}/CB_0deg.txt'
CB_15deg = f'{data}/CB_15deg.txt'
CB_30deg = f'{data}/CB_30deg.txt'
CB_45deg = f'{data}/CB_45deg.txt'


LB_0deg = ''
LB_15deg = ''
LB_30deg = ''
LB_45deg = ''

df0 = pd.read_csv(CB_0deg, skiprows=0, header=0, engine='python')
df15 = pd.read_csv(CB_15deg, skiprows=0, header=0, engine='python')
df30 = pd.read_csv(CB_30deg, skiprows=0, header=0, engine='python')
df45 = pd.read_csv(CB_45deg, skiprows=0, header=0, engine='python')


list = [len(df0), len(df15), len(df30), len(df45)]
xval = []
xval2= []
sublist = []
vals = []
#create list of Length of line profile
for i in range(len(list)):
    xval.append(range(list[i]))
    for j in range(len(xval[i])):
        xval2.append(j)


for i in range(len(list)):
    sublist.append(xval2[0:list[i]])

#quick fix to zero issue
sublist[1].insert(63, 63)
sublist[1].pop(64)


#ax = plt.figure().add_subplot(projection='3d')
#ax.plot(sublist[0], df0, zdir='z')
#ax.set_xlabel('Pixels')
#ax.set_ylabel('CR Magnitude')

plt.plot(sublist[0], df0)
plt.plot(sublist[1], df15)
plt.plot(sublist[2], df30)
plt.plot(sublist[3], df45)
plt.show()

