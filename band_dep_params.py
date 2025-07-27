import os, os.path
import shutil
import glob

import pandas as pd

main_path = ''


#subdirs = os.listdir(main_path)
#print((f'{main_path}/{subdirs[0]}'))


def path_to_df(band_no):
    col_list = [0, 1]
    band_df = []
    # Iterively read absorbance to pandas dataframe
    for i in range(len(band_no)):
        band_df.append(pd.read_csv(band_no[i], skiprows=8, sep=',', header=0, engine='python', names=col_list))

    return band_df


def get_max_abs(band_df):
    # Find max absorbance values in each Spectra
    band1_peaks = []
    for i in range(len(band_df)):
        band1_peaks.append(band_df[i].loc[band_df[i][1].idxmax()].tolist())

    return band1_peaks


def band_dep_df():
    # Band 1 Absorbance Data
    band1_0deg = f'{main_path}/0deg/0deg_BF2_band1.csv'
    band1_15deg = f'{main_path}/15deg/15deg_BF2_band1.csv'
    band1_30deg = f'{main_path}/30deg/30deg_BF2_band1.csv'
    band1_45deg = f'{main_path}/45deg/45deg_BF2_band1.csv'
    band1_60deg = f'{main_path}/60deg/60deg_BF2_band1.csv'
    band1_75deg = f'{main_path}/75deg/75deg_BF2_band1.csv'
    band1_90deg = f'{main_path}/90deg/90deg_BF2_band1.csv'

    # Band 2 Absorbance data
    band2_0deg = f'{main_path}/0deg/0deg_BF2_band2.csv'
    band2_15deg = f'{main_path}/15deg/15deg_BF2_band2.csv'
    band2_30deg = f'{main_path}/30deg/30deg_BF2_band2.csv'
    band2_45deg = f'{main_path}/45deg/45deg_BF2_band2.csv'
    band2_60deg = f'{main_path}/60deg/60deg_BF2_band2.csv'
    band2_75deg = f'{main_path}/75deg/75deg_BF2_band2.csv'
    band2_90deg = f'{main_path}/90deg/90deg_BF2_band2.csv'

    col_list = [0, 1]
    band1_list = [band1_0deg, band1_15deg, band1_30deg, band1_45deg, band1_60deg, band1_75deg, band1_90deg]
    band2_list = [band2_0deg, band2_15deg, band2_30deg, band2_45deg, band2_60deg, band2_75deg, band2_90deg]

    band1_df = []
    # Iterively read absorbance to pandas dataframe
    for i in range(len(band1_list)):
        band1_df.append(pd.read_csv(band1_list[i], skiprows=8, sep=',', header=0, engine='python', names=col_list))

    return band1_df

def max_abs(band1_df):
    # Find max absorbance values in each Spectra
    band1_peaks = []
    for i in range(len(band1_df)):
        band1_peaks.append(band1_df[i].loc[band1_df[i][1].idxmax()].tolist())

    return band1_peaks


def max_pk_to_polar(band_peaks):

    bn_theta = []  # polarizer angle
    bn_r = []  # max absorbance
    for i in range(len(band_peaks)):
        bn_r.append(band_peaks[i][1])
        bn_theta.append(band_peaks[i][0])

    return bn_theta, bn_r
