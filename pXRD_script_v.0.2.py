import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plot_params import convert_th_q_int_norm as tqni
from plot_params import incr_norm_vals as icv
from plot_params import plot_params as plt_par
from plot_params import ref_data as ref_data

savepath = '/Volumes/T7/Research/liquid_crystals/7ocb/pXRD/solubility_crystal_form_screen/jbb_7ocb_evap_sol_actontrile0'
### Data to compare with reference data: CHANGEABLE ###
path1 = f'{savepath}/jbb_7ocb_evap_sol_actontri_01_001_bg_subtracted.xy'
path2 = ''
path3 = ''
path4 = ''

rename = ['Angle', 'Intensity']
col_list = [0, 1]

# Collect Reference data from plot_params script
#ref_data_plot = ref_data()
# Create dataframe from collected pXRD data
df1 = pd.read_csv(path1, sep='\s', header=0, names=rename, engine='python')
#df2 = pd.read_csv(path2, sep='\s', header=0, names=rename, engine='python')
#df3 = pd.read_csv(path3, sep='\s', header=0, names=rename, engine='python')
#df4 = pd.read_csv(path4, sep='\s', header=0, names=rename, engine='python')

#Convert theta to q and normalize all intensities to 1
df1_q_norm = tqni(df1['Angle'], df1['Intensity'])
#df2_q_norm = tqni(df2['Angle'], df2['Intensity'])
#df3_q_norm = tqni(df3['Angle'], df3['Intensity'])
#df4_q_norm = tqni(df4['Angle'], df4['Intensity'])

#recombine data into list and artificicially increase intensity of plot for comparison
df1_plt = [df1_q_norm[0], icv(df1_q_norm[1], .1)]
#df2_plt = [df2_q_norm[0], icv(df2_q_norm[1])]
#df3_plt = [df3_q_norm[0], icv(df3_q_norm[1])]
#df4_plt = [df4_q_norm[0], icv(df4_q_norm[1])]


plt.plot(df1_plt[0], df1_plt[1], label="Evaporation in Acetonitrile")
#plt.plot(ref_data_plot[2][0], ref_data_plot[2][1], label="Simulated Commercial Powder")
#plt.plot(ref_data_plot[1][0], ref_data_plot[1][1], label="Simulated Needle")
#plt.plot(ref_data_plot[0][0], ref_data_plot[0][1], label="Simulated Square Planar")

plt.legend(fontsize=12, loc="upper right", bbox_to_anchor=(1, 1), frameon=False)
plt.xlabel('q ($\mathrm{\AA}^{-1}$)')
plt.ylabel('Normalized Intensity')
plt.xlim(.25, 2.25)
plt.ylim(0, 1.25)

#Tickmarks
plt.minorticks_on()
xticks = np.arange(.25, 2.25, 0.25)
yticks = np.arange(0, 1.25, 1)

plt.tick_params(direction='in', right=True, top=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)
plt.tick_params(direction='in', which='minor', length=3, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in', which='major', length=5, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)

plt.gcf().set_size_inches(15, 7)
plt.savefig(f'{savepath}/sol_screen_ACN_code_v0.2.png', dpi=300, bbox_inches='tight')
plt.show()
