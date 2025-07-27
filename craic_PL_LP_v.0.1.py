import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


main_path = ''

band1 = f'{main_path}/7OCB_LP_band_1.csv'
band2 = f'{main_path}/7OCB_LP_band_2.csv'

col_list = [0, 1]

df1 = pd.read_csv(band1, skiprows=8, sep=',', header=0, engine='python', names=col_list)
df2 = pd.read_csv(band2, skiprows=8, sep=',', header=0, engine='python', names=col_list)


plt.plot(df1[0], df1[1], label="7OCB LP Band 1 10x")
plt.plot(df2[0], df2[1], label="7OCB LP Band 2 10x")

plt.legend(fontsize=10, loc="upper right", bbox_to_anchor=(1, 1), frameon=False)
plt.xlabel('Wavelength')
plt.ylabel('Counts')
#plt.xlim(400, 500)

plt.gcf().set_size_inches(7, 7)
plt.savefig(f'{main_path}/NA_5_10x_Abs_LP_v.0.1.png', dpi=300, bbox_inches='tight', transparent='True')
plt.show()
