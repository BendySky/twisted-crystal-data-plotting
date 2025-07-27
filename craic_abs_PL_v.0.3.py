import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from plot_params import incr_norm_vals as icv


import csv

main_path = '/Volumes/T7/Research/collaborations/ethan_powell_project/compound_4_oligothiophene/craic_data/20250702_angle_dep/region4_og_pitch/bl_corr-raw'

# Band 1 Absorbance Data
band1_0deg = f'{main_path}/0deg/0deg_band1.csv'
band1_15deg = f'{main_path}/15deg/15deg_band1.csv'
band1_30deg = f'{main_path}/30deg/30deg_band1.csv'
band1_45deg = f'{main_path}/45deg/45deg_band1.csv'
band1_75deg = f'{main_path}/60deg/60deg_band1.csv'
band1_60deg = f'{main_path}/75deg/75deg_band1.csv'
band1_90deg = f'{main_path}/90deg/90deg_band1.csv'

# Band 2 Absorbance data
band2_0deg = f'{main_path}/0deg/0deg_band2.csv'
band2_15deg = f'{main_path}/15deg/15deg_band2.csv'
band2_30deg = f'{main_path}/30deg/30deg_band2.csv'
band2_45deg = f'{main_path}/45deg/45deg_band2.csv'
band2_60deg = f'{main_path}/60deg/60deg_band2.csv'
band2_75deg = f'{main_path}/75deg/75deg_band2.csv'
band2_90deg = f'{main_path}/90deg/90deg_band2.csv'

col_list = [0, 1]
band1_list = [band1_0deg, band1_15deg, band1_30deg, band1_45deg, band1_60deg, band1_75deg, band1_90deg]
band2_list = [band2_0deg, band2_15deg, band2_30deg, band2_45deg, band2_60deg, band2_75deg, band2_90deg]

colors = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600']
pol_ang = ['0º', '15º', '30º', '45º', '60º', '75º', '90º']

band1_df = []
band2_df = []
# Iterively read absorbance to pandas dataframe
for i in range(len(band1_list)):
    band1_df.append(pd.read_csv(band1_list[i], skiprows=8, sep=',', header=0, engine='python', names=col_list))
    band2_df.append(pd.read_csv(band2_list[i], skiprows=8, sep=',', header=0, engine='python', names=col_list))

#for i in range(len(band1_df)):
#    plt.plot(band1_df[i][0], band1_df[i][1], label=pol_ang[i], color=colors[i])

for i in range(len(band2_df)):
    plt.plot(band2_df[i][0], band2_df[i][1], label=pol_ang[i], color=colors[i])

'''

#Artificially increase absorbance vals
#df1 = [df1[0], icv(df1[1], .25)]
#df2 = [df1[0], icv(df1[1], 1)]

plt.plot(band1_df[0], band1_df[1], label="Polarizer angle=0º", color='#003f5c')
plt.plot(band1_df[0], df2[1], label='Polarizer angle-15º', color='#374c80')
plt.plot(df3[0], df3[1], label='Polarizer Angle-30º', color='#7a5195')
plt.plot(df4[0], df4[1], label='Polarizer Angle-45º', color='#bc5090')
plt.plot(df5[0], df5[1], label='Polarizer Angle-60º', color='#ef5675')
plt.plot(df6[0], df6[1], label='Polarizer Angle-75º', color='#ff764a')
plt.plot(df7[0], df7[1], label='Polarizer Angle=90º', color='#ffa600')
'''

plt.legend(fontsize=12, loc="upper right", bbox_to_anchor=(1, 1), frameon=False)
plt.xlabel('Wavelength')
plt.ylabel('Absorbance')
plt.xlim(370, 800)
plt.ylim(0, 1.6)

#Tickmarks
plt.minorticks_on()
#xticks = np.arange(.25, 2.25, 0.25)
#yticks = np.arange(0, 4, 1)

#plt.tick_params(direction='in', right=True, top=True)
#plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)
plt.tick_params(direction='in', which='minor', length=3, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in', which='major', length=5, bottom=True, top=True, left=True, right=True)
#plt.xticks(xticks)
#plt.yticks(yticks)

plt.gcf().set_size_inches(7, 7)
plt.savefig(f'{main_path}/band_dep_abs_band2_v.0.3.png', dpi=300, bbox_inches='tight', transparent='True')
plt.show()
