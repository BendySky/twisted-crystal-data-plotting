import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


'''Functions for plotting XRD data from .CSV, .XY and .TSV data. 
Connect this code with pXRD_script_v.$.$.py script for maximum 
functionality. These functions are placed on the backend to 
shorten the total length of the frontend code'''

def convert_th_q_int_norm(df_th, df_int):

    '''
    1st part of function converts 2theta to q space and
    second part normalizes intensity b/t [0, 1]
    '''
    new_q = []
    norm_int = []
    new_q_int_df = []

    # Convert th to q
    wav = 1.5403
    new_q = (4 * np.pi / wav) * np.sin(np.radians(df_th / 2))

    # Normalize Intensity
    norm_int = (df_int - np.min(df_int)) / (np.max(df_int) - np.min(df_int))

    return new_q, norm_int


def incr_norm_vals(df_int_norm, val=0):

    '''
    Artificially raises intensity of normalized data
    (df_int_norm) by arbitrary value (val)
    '''

    df_int_norm = df_int_norm + val

    return df_int_norm


def ref_data():

    '''Reference data to compare with other pXRD patterns'''

    rename = ['Angle', 'Intensity']
    col_list = [0, 1]

    sq_pl = ''
    needle = ''
    comm_pow = ''

    sq_pl_df = pd.read_csv(sq_pl, delimiter='   ', header=None, names=rename, engine='python')
    needle_df = pd.read_csv(needle, delimiter='   ', header=None, names=rename, engine='python')
    comm_pow_df = pd.read_csv(comm_pow, delimiter=',', header=None, names=rename, engine='python')

    sq_pl_q_norm = convert_th_q_int_norm(sq_pl_df['Angle'], sq_pl_df['Intensity'])
    needle_q_norm = convert_th_q_int_norm(needle_df['Angle'], needle_df['Intensity'])
    comm_pow_q_norm = convert_th_q_int_norm(comm_pow_df['Angle'], comm_pow_df['Intensity'])

    sq_pl_plot_data = [sq_pl_q_norm[0], incr_norm_vals(sq_pl_q_norm[1], 0)]
    needle_plot_data = [needle_q_norm[0], incr_norm_vals(needle_q_norm[1], 1)]
    comm_pow_plot_data = [comm_pow_q_norm[0], incr_norm_vals(comm_pow_q_norm[1], 2)]

    return sq_pl_plot_data, needle_plot_data, comm_pow_plot_data


def plot_params(x_lim=(min, max), y_lim=(min, max), x_ticks=(min, max, '''step'''),
                y_ticks=(min, max, '''step'''), show_plot=True, savepath='str', save_name='str'):

    plt.legend(fontsize=8, loc="upper right", bbox_to_anchor=(1, 1), frameon=True)
    plt.xlabel('q ($\mathrm{\AA}^{-1}$)')
    plt.ylabel('Normalized Intensity')
    plt.xlim(x_lim)
    plt.ylim(y_lim)

    # Tickmarks
    plt.minorticks_on()
    xticks = np.arange(x_ticks)
    yticks = np.arange(y_ticks)

    plt.tick_params(direction='in', right=True, top=True)
    plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)
    plt.tick_params(direction='in', which='minor', length=3, bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='major', length=5, bottom=True, top=True, left=True, right=True)
    plt.xticks(xticks)

    plt.gcf().set_size_inches(15, 7)


    if show_plot==True:
        plt.show()
        plt.savefig(f'{savepath}/{save_name}.png', dpi=300, bbox_inches='tight')
    if show_plot == False:
        plt.savefig(f'{savepath}/{save_name}.png', dpi=300, bbox_inches='tight')