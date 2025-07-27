import pandas as pd
from matplotlib import pyplot as plt

main_path = '/Volumes/T7/Research/liquid_crystals/7ocb/craic/20250613_7OCB_NR_LP_PL/PL_546nm_10x'

band1_PL = f'{main_path}/7OCB_band1.csv'
band2_PL = f'{main_path}/7OCB_band2.csv'

savepath = ''

rename = ['Wavelength', 'Counts']
col_list = [0, 1]
header_range = (0, 8)

df1 = pd.read_csv(band1_PL, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df2 = pd.read_csv(band2_PL, skiprows=8, sep=',', header=0, engine='python', names=col_list)

plt.plot(df1[0], df1[1], label='Band 1')
plt.plot(df2[0], df2[1], label='Band 2')

plt.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
plt.xlabel('Wavelength')
plt.ylabel('Counts')
plt.xlim(300, 900)
#plt.ylim()

plt.minorticks_on()

plt.gcf().set_size_inches(15, 7)
plt.show()