import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plot_params import convert_th_q_int_norm as tqni
from plot_params import incr_norm_vals as icv
from plot_params import plot_params as plt_par


sq_pl = ''
needle = ''
comm_pow = ''

df1 = ''
df2 = ''
df3 = ''
df4 = ''

savepath = ''

rename = ["Angle", "Intensity"]
col_list = [0, 1]

sq_pl_df = pd.read_csv(sq_pl, delimiter='   ', header=None, names=rename, engine='python')
needle_df = pd.read_csv(needle, delimiter='   ', header=None, names=rename, engine='python')
comm_pow_df = pd.read_csv(comm_pow, delimiter=',', header=None, names=rename, engine='python')

acetonitrile_df = pd.read_csv(df1, sep='\s', header=0, names=rename, engine='python')
diet_ether_df = pd.read_csv(df2, sep='\s', header=0, names=rename, engine='python')
hexane_df = pd.read_csv(df3, sep='\s', header=0, names=rename, engine='python')
chcl3_df = pd.read_csv(df4, sep='\s', header=0, names=rename, engine='python')


def convert_th_to_q(df_theta, df_intensity):

    new_q = []
    norm_int = []
    new_q_int_df = []

    ### Convert th to q ###
    wav = 1.5403
    new_q = (4*np.pi/wav)*np.sin(np.radians(df_theta/2))

    ### Normalize Intensity ###
    norm_int = (df_intensity-np.min(df_intensity)) / (np.max(df_intensity) - np.min(df_intensity))

    return new_q, norm_int


def incr_norm_vals(df_int_norm, val=0):
    '''Artificially raises intensity of normalized data
    (df_int_norm) by arbitrary value (val)'''

    df_int_norm = df_int_norm + val
    return df_int_norm


### Reference Data: DO NOT TOUCH ###
sq_pl_q_norm_int_df = convert_th_to_q(sq_pl_df['Angle'], sq_pl_df['Intensity'])
needle_q_norm_int_df = convert_th_to_q(needle_df['Angle'], needle_df['Intensity'])
comm_pow_q_norm_int_df = convert_th_to_q(comm_pow_df['Angle'], comm_pow_df['Intensity'])

sq_pl_plot_data = [sq_pl_q_norm_int_df[0], incr_norm_vals(sq_pl_q_norm_int_df[1], 0)]
needle_plot_data = [needle_q_norm_int_df[0], incr_norm_vals(needle_q_norm_int_df[1], 1)]
comm_pow_plot_data = [comm_pow_q_norm_int_df[0], incr_norm_vals(comm_pow_q_norm_int_df[1], 2)]


### Measured Data: CAN BE CHANGED ###
acetonitrile_q_norm_df = convert_th_to_q(acetonitrile_df['Angle'], acetonitrile_df['Intensity'])
diet_ether_q_norm_df = convert_th_to_q(diet_ether_df['Angle'], diet_ether_df['Intensity'])
hexane_q_norm_df = convert_th_to_q(hexane_df['Angle'], hexane_df['Intensity'])
chcl3_q_norm_df = convert_th_to_q(chcl3_df['Angle'], chcl3_df['Intensity'])

acetonitrile_data = [acetonitrile_q_norm_df[0], incr_norm_vals(acetonitrile_q_norm_df[1], 3)]
diet_ether_data = [diet_ether_q_norm_df[0], incr_norm_vals(diet_ether_q_norm_df[1], 4)]
hexane_data = [hexane_q_norm_df[0], incr_norm_vals(hexane_q_norm_df[1], 5)]
chcl3_data = [chcl3_q_norm_df[0], incr_norm_vals(chcl3_q_norm_df[1], 6)]


### Collected Data: CAN BE CHANGED
plt.plot(chcl3_data[0], chcl3_data[1], label="Evap Chloroform")
plt.plot(hexane_data[0], hexane_data[1], label="Evap Hexanes")
plt.plot(diet_ether_data[0], diet_ether_data[1], label="Evap Diethyl Ether")
plt.plot(acetonitrile_data[0], acetonitrile_data[1], label="Evap Acetonitrile")

### Ref Data: DO NOT CHANGE ###
plt.plot(comm_pow_plot_data[0], comm_pow_plot_data[1], label="Collected Commercial Powder")
plt.plot(needle_plot_data[0], needle_plot_data[1], label="Simulated Needle")
plt.plot(sq_pl_plot_data[0], sq_pl_plot_data[1], label="Simulated Square Planar")


plt.legend(fontsize=8, loc="upper right", bbox_to_anchor=(1, 1), frameon=False)
plt.xlabel('q ($\mathrm{\AA}^{-1}$)')
plt.ylabel('Normalized Intensity')
plt.xlim(.25, 2.25)
plt.ylim(0, 8)

#Tickmarks
plt.minorticks_on()
xticks = np.arange(.25, 2.25, 0.25)
yticks = np.arange(0, 7, 1)

plt.tick_params(direction='in', right=True, top=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)
plt.tick_params(direction='in', which='minor', length=3, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in', which='major', length=5, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)

plt.gcf().set_size_inches(15, 7)
#plt.savefig(f'{savepath}/sol_screen_1_code_v0.1.png', dpi=300, bbox_inches='tight')
#plt.figure(figsize=2000, 1000)
plt.savefig(f'{savepath}/sol_screen_1_code_v0.1.png', dpi=300, bbox_inches='tight')
plt.show()