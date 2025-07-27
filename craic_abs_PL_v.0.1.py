import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from plot_params import incr_norm_vals as icv


import csv

main_path = ''

band1_0deg = f'{main_path}/0deg/0deg_BF2_band1.csv'
band1_15deg = f'{main_path}/15deg/15deg_BF2_band1.csv'
band1_30deg = f'{main_path}/30deg/30deg_BF2_band1.csv'
band1_45deg = f'{main_path}/45deg/45deg_BF2_band1.csv'
band1_60deg = f'{main_path}/60deg/60deg_BF2_band1.csv'
band1_75deg = f'{main_path}/75deg/75deg_BF2_band1.csv'
band1_90deg = f'{main_path}/90deg/90deg_BF2_band1.csv'


savepath = 'band1_0_deg.csv'

rename = ['Wavelength', 'Counts']
col_list = [0, 1]
header_range = (0,8)
df1 = pd.read_csv(band1_0deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df2 = pd.read_csv(band1_15deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df3 = pd.read_csv(band1_30deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df4 = pd.read_csv(band1_45deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df5 = pd.read_csv(band1_60deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df6 = pd.read_csv(band1_75deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df7 = pd.read_csv(band1_90deg, skiprows=8, sep=',', header=0, engine='python', names=col_list)

#Artificially increase absorbance vals
#df1 = [df1[0], icv(df1[1], .25)]
#df2 = [df1[0], icv(df1[1], 1)]

plt.plot(df1[0], df1[1], label="Polarizer angle=0º", color='#003f5c')
plt.plot(df2[0], df2[1], label='Polarizer angle-15º', color='#374c80')
plt.plot(df3[0], df3[1], label='Polarizer Angle-30º', color='#7a5195')
plt.plot(df4[0], df4[1], label='Polarizer Angle-45º', color='#bc5090')
plt.plot(df5[0], df5[1], label='Polarizer Angle-60º', color='#ef5675')
plt.plot(df6[0], df6[1], label='Polarizer Angle-75º', color='#ff764a')
plt.plot(df7[0], df7[1], label='Polarizer Angle=90º', color='#ffa600')


plt.legend(fontsize=12, loc="upper right", bbox_to_anchor=(1, 1), frameon=False)
plt.xlabel('Wavelength')
plt.ylabel('Counts')
plt.xlim(390, 490)
plt.ylim(0, 1)

#Tickmarks
plt.minorticks_on()
#xticks = np.arange(.25, 2.25, 0.25)
#yticks = np.arange(0, 4, 1)

#plt.tick_params(direction='in', right=True, top=True)
#plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)
#plt.tick_params(direction='in', which='minor', length=3, bottom=True, top=True, left=True, right=True)
#plt.tick_params(direction='in', which='major', length=5, bottom=True, top=True, left=True, right=True)
#plt.xticks(xticks)
#plt.yticks(yticks)

plt.gcf().set_size_inches(7, 7)
plt.savefig(f'{main_path}/band_dep_abs_band1_v.0.2.png', dpi=300, bbox_inches='tight', transparent='True')
plt.show()
