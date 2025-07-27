from matplotlib import pyplot as plt
from fnmatch import fnmatch
import pandas as pd
import numpy as np
import os

'''
Functions for plotting Band dependent absorbance
'''


def bands(filepath, band_no=1, bl_corr='true', sort='true'):

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
        files.sort()
        for name in files:
            if fnmatch(name, mime):
                data_name.append(os.path.join(path, name))

    return data_name


abs_raw = np.arange(0, 1.7, 0.2)
abs_bl = np.arange(0, 1.1, 0.2)


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


colors = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600']
pol_ang = ['0º', '15º', '30º', '45º', '60º', '75º', '90º']


'''
Functions for plotting Max Absorbances in a polar plot
'''


def max_abs(band_df):

    '''
    Gets max absorbance values from polarization-dependent absorbance
    :param band_df: Absorbance values in the dataframe
    :return:
    '''

    band_peaks = []
    for i in range(len(band_df)):
        band_peaks.append(band_df[i].loc[band_df[i][1].idxmax()].tolist())

    return band_peaks


def pol_plot_params(ax2, ylim=[0, 1.0]):
    ax2.set_thetamin(0)
    ax2.set_thetamax(90)
    ax2.set_ylim(ylim)
    ax2.set_thetagrids([0, 15, 30, 45, 60, 75, 90])