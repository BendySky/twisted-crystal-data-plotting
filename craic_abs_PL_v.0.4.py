import os
from fnmatch import fnmatch
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


path = '/Volumes/T7/Research/collaborations/ethan_powell_project/compound_4_oligothiophene/craic_data/' \
       '20250702_angle_dep/region1/bl_corr-raw'


def bands(filepath, band_no=1, bl_corr='true'):

    '''
    :param filepath: base filepath containing all of polarization data
    :param band_no: decide whether to view band 1 or band 2 from polarization-dependent measurement
    :param bl_corr: 'true' is baseline correction was used. 'false' if not. only works if file has a "_bl" at end
    :return:
    '''

    data_name = []

    if band_no == 1 and bl_corr == 'false':
        mime = '*band1.csv'

    elif band_no == 2 and bl_corr == 'false':
        mime = '*band2.csv'

    elif band_no == 1 and bl_corr == 'true':
        mime = '*band1_bl.csv'

    elif band_no == 2 and bl_corr == 'true':
        mime = '*band2_bl.csv'

    for path, subdirs, files in os.walk(filepath):
        for name in files:
            if fnmatch(name, mime):
                data_name.append(os.path.join(path, name))

    return data_name

#
band2_bl = bands(path, band_no=2, bl_corr='true')
band1_bl = bands(path, band_no=1, bl_corr='true')

band2 = bands(path, band_no=2, bl_corr='false')
band1 = bands(path, band_no=1, bl_corr='false')


if 'band1_bl' and 'band2_bl' in globals():
    print('Baseline Correction Used\n')
    band1_bl_df = []
    band2_bl_df = []
    for i in range(len(band1_bl)):
        band1_bl_df.append(pd.read_csv(band1_bl[i], skiprows=9, delimiter=',', header=None, engine='python'))
        band2_bl_df.append(pd.read_csv(band2_bl[i], skiprows=9, delimiter=',', header=None, engine='python'))


band1_df = []
band2_df = []
for i in range(len(band1)):
    band1_df.append(pd.read_csv(band1[i], skiprows=9, delimiter=',', header=None, engine='python'))
    band2_df.append(pd.read_csv(band2[i], skiprows=9, delimiter=',', header=None, engine='python'))


fig1, ax1 = plt.subplots(figsize=(7,7))
fig2, ax2 = plt.subplots(figsize=(7,7))
fig3, ax3 = plt.subplots(figsize=(7,7))
fig4, ax4 = plt.subplots(figsize=(7,7))

abs_raw = np.arange(0, 1.7, 0.2)
abs_bl = np.arange(0, 1.1, 0.2)

colors = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600']
pol_ang = ['0º', '15º', '30º', '45º', '60º', '75º', '90º']

def subplot_params(axs, ylim=[0, 1.0], abs_val=abs_bl):
    axs.set_xlim([370, 800])
    axs.set_ylim(ylim)
    axs.set_xlabel("Wavelength (nm)")
    axs.set_ylabel("Absorbance")
    #plt.setp(axs, xticks=[400, 450, 500, 500, 550, 600, 650, 700, 750, 800])
    #plt.setp(axs, yticks=abs_val)
    axs.tick_params(axis="x", which="both", top=True, labeltop=False, bottom=True, labelbottom=True, direction="in", labelsize=12)
    axs.tick_params(axis="y", which="both", right=True, labeltop=False, left=True, labelbottom=True, direction="in", labelsize=12)
    #axs.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
    axs.minorticks_on()


subplot_params(ax1, ylim=[0, 1.6])
subplot_params(ax2, ylim=[0, 1.6])
subplot_params(ax3)
subplot_params(ax4)

for k in range(len(band1_df)):
    ax1.plot(band1_df[k][0], band1_df[k][1], label=pol_ang[k], color=colors[k])
    ax2.plot(band2_df[k][0], band2_df[k][1], label=pol_ang[k], color=colors[k])
    if 'band1_bl' and 'band2_bl' in globals():
        ax3.plot(band1_bl_df[k][0], band1_bl_df[k][1], label=pol_ang[k], color=colors[k])
        ax4.plot(band2_bl_df[k][0], band2_bl_df[k][1], label=pol_ang[k], color=colors[k])

fig1.savefig(f'{path}/band_dep_abs_band1_v.0.4.png', dpi=300, bbox_inches='tight', transparent=True)
fig2.savefig(f'{path}/band_dep_abs_band2_v.0.4.png',dpi=300, bbox_inches='tight', transparent=True)
fig3.savefig(f'{path}/band_dep_abs_band1_bl_v.0.4.png', dpi=300, bbox_inches='tight', transparent=True)
fig4.savefig(f'{path}/band_dep_abs_band2_bl_v.0.4.png', dpi=300, bbox_inches='tight', transparent=True)

ax1.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
ax2.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
ax3.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
ax4.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
plt.show()


