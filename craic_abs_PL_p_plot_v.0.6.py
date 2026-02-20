from band_dep_params_v3 import pol_df, subplot_params, max_abs, pol_plot_params, split_list
from band_dep_params_v3 import plot_colors_pol_orient
from matplotlib import pyplot as plt
from math import radians
import pandas as pd
import numpy as np

'''Need to crop data between 400-800 nm before max_abs() method is run'''

mainpath = '/Volumes/T7/Research/liquid_crystals/Crystal_dying/Dye_7AC/angle_dep_horz'

## Globals ##
abs_rg = [0, 1.0]
fig_sz = (10,10)
colors = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600']
pol_ang = ['0º', '15º', '30º', '45º', '60º', '75º', '90º']
bands = []
peak_abs = []
r1 = [0, 15, 30, 45, 60, 75, 90]
angle = [radians(a) for a in r1]

# Shape Data: (no. df, no. angles, no datapoints, abs/int) – (2, 7, 924, 2)
# Shape peak abs: (2, 7, 2)
for data in range(0, len(pol_df(mainpath))):
    bands.append(pol_df(mainpath)[data])
    for peak in range(0, len(max_abs(bands[0]))):
        peak_abs.append(max_abs(bands[data])[0:][peak][1])

peak_abs = split_list(peak_abs)

# For Loop plots Abs plot and Polar Plot
for k in range(0, len(bands)):
    fig, ax = plt.subplots(figsize=fig_sz)
    fig1, pol = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=fig_sz)
    #subplot_params(ax, ylim=abs_rg)
    for j in range(0, len(bands[1])):
        subplot_params(ax, ylim=abs_rg)
        ax.plot(bands[k][j][0], bands[k][j][1], label=pol_ang[j], color=colors[j])
        pol_plot_params(pol, ylim=abs_rg)
        pol.scatter(angle, peak_abs[k], c=colors, alpha=0.75, s=200)

    fig.savefig(f'{mainpath}/band_dep_abs_band{k+1}_v.0.6.png', dpi=300, bbox_inches='tight', transparent=True)
    fig1.savefig(f'{mainpath}/pol_plot_band{k+1}_v.0.6.png', dpi=300, bbox_inches='tight', transparent=True)
