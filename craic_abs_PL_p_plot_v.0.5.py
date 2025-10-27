from band_dep_params_v2 import bands, subplot_params, max_abs, pol_plot_params
from band_dep_params_v2 import colors, pol_ang
from matplotlib import pyplot as plt
from math import radians
import pandas as pd
import numpy as np


mainpath = '/Volumes/T7/Research/liquid_crystals/7ocb/craic/7OCB_Oligothiophene_EP_34nmol/Band_Dep_Abs/polarized_undoped'


## comment this out if baseline correction was not used
band1_bl = bands(mainpath, band_no=1, bl_corr='false')
band2_bl = bands(mainpath, band_no=2, bl_corr='false')

band1 = bands(mainpath, band_no=1, bl_corr='true')
band2 = bands(mainpath, band_no=2, bl_corr='true')

band1_df = []
band2_df = []
for i in range(len(band1)):
    band1_df.append(pd.read_csv(band1[i], skiprows=9, delimiter=',', header=None, engine='python'))
    band2_df.append(pd.read_csv(band2[i], skiprows=9, delimiter=',', header=None, engine='python'))

# searches for band1_bl and band2_bl in global variables
# if the baseline paths were commented out, the below line will automatically run
if 'band1_bl' and 'band2_bl' in globals():
    print('Baseline Correction Used\n')
    band1_bl_df = []
    band2_bl_df = []
    for i in range(len(band1_bl)):
        band1_bl_df.append(pd.read_csv(band1_bl[i], skiprows=9, delimiter=',', header=None, engine='python'))
        band2_bl_df.append(pd.read_csv(band2_bl[i], skiprows=9, delimiter=',', header=None, engine='python'))
print(np.shape(band1_df))


fig1, ax1 = plt.subplots(figsize=(7,7))
fig2, ax2 = plt.subplots(figsize=(7,7))

subplot_params(ax1, ylim=[0, 1.6])
subplot_params(ax2, ylim=[0, 1.6])

if 'band1_bl' and 'band2_bl' in globals():
    fig3, ax3 = plt.subplots(figsize=(7,7))
    fig4, ax4 = plt.subplots(figsize=(7,7))

    subplot_params(ax3)
    subplot_params(ax4)

for k in range(len(band1_df)):
    ax1.plot(band1_df[k][0], band1_df[k][1], label=pol_ang[k], color=colors[k])
    ax2.plot(band2_df[k][0], band2_df[k][1], label=pol_ang[k], color=colors[k])
    if 'band1_bl' and 'band2_bl' in globals():
        ax3.plot(band1_bl_df[k][0], band1_bl_df[k][1], label=pol_ang[k], color=colors[k])
        ax4.plot(band2_bl_df[k][0], band2_bl_df[k][1], label=pol_ang[k], color=colors[k])

ax1.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
ax2.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
#ax3.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
#ax4.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)

fig1.savefig(f'{mainpath}/band_dep_abs_band1_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)
fig2.savefig(f'{mainpath}/band_dep_abs_band2_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)
#fig3.savefig(f'{mainpath}/band_dep_abs_band1_bl_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)
#fig4.savefig(f'{mainpath}/band_dep_abs_band2_bl_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)


b1 = []
b2 = []
b1_bl = []
b2_bl = []
r1 = [0, 15, 30, 45, 60, 75, 90]
angle = [radians(a) for a in r1]

b1_peak = max_abs(band1_df)
b2_peak = max_abs(band2_df)
#b1_bl_peak = max_abs(band1_bl_df)
#b2_bl_peak = max_abs(band2_bl_df)


for i in range(len(b1_peak)):
    b1.append(b1_peak[i][1])
    b2.append(b2_peak[i][1])
    #b1_bl.append(b1_bl_peak[i][1])
    #b2_bl.append(b2_bl_peak[i][1])

fig5, pol1 = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))
fig6, pol2 = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))
#fig7, pol1_bl = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))
#fig8, pol2_bl = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))

pol_plot_params(pol1, ylim=[0, 1.6])
pol_plot_params(pol2, ylim=[0, 1.6])
#pol_plot_params(pol1_bl)
#pol_plot_params(pol2_bl)


pol1.scatter(angle, b1, c=colors, alpha=0.75, s=200)
pol2.scatter(angle, b2, c=colors, alpha=0.75, s=200)
#pol1_bl.scatter(angle, b1, c=colors, alpha=0.75, s=200)
#pol2_bl.scatter(angle, b2_bl, c=colors, alpha=0.75, s=200)


fig5.savefig(f'{mainpath}/pol_plot_band1_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)
fig6.savefig(f'{mainpath}/pol_plot_band2_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)
#fig7.savefig(f'{mainpath}/pol_plot_band1_bl_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)
f#ig8.savefig(f'{mainpath}/pol_plot_band2_bl_v.0.5.png', dpi=300, bbox_inches='tight', transparent=True)

#plt.show()
