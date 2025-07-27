from matplotlib import pyplot as plt
from band_dep_params import get_max_abs
import numpy as np
import plotly.express as px
import pandas as pd
from math import radians
import math


main_path = ''


# Band 1 Absorbance Data
band1_0deg = f'{main_path}/0deg/0deg_band1.csv'
band1_15deg = f'{main_path}/15deg/15deg_band1.csv'
band1_30deg = f'{main_path}/30deg/30deg_band1.csv'
band1_45deg = f'{main_path}/45deg/45deg_band1.csv'
band1_75deg = f'{main_path}/60deg/60deg_band1.csv'
band1_60deg = f'{main_path}/75deg/75deg_band1.csv'
band1_90deg = f'{main_path}/90deg/90deg_band1.csv'

# Band 2 Absorbance data
band2_0deg = f'{main_path}/0deg/0deg_band2.csv'
band2_15deg = f'{main_path}/15deg/15deg_band2.csv'
band2_30deg = f'{main_path}/30deg/30deg_band2.csv'
band2_45deg = f'{main_path}/45deg/45deg_band2.csv'
band2_60deg = f'{main_path}/60deg/60deg_band2.csv'
band2_75deg = f'{main_path}/75deg/75deg_band2.csv'
band2_90deg = f'{main_path}/90deg/90deg_band2.csv'

col_list = [0, 1]
band1_list = [band1_0deg, band1_15deg, band1_30deg, band1_45deg, band1_60deg, band1_75deg, band1_90deg]
band2_list = [band2_0deg, band2_15deg, band2_30deg, band2_45deg, band2_60deg, band2_75deg, band2_90deg]

band1_df = []
band2_df = []
# Iterively read absorbance to pandas dataframe
for i in range(len(band1_list)):
    band1_df.append(pd.read_csv(band1_list[i], skiprows=8, sep=',', header=0, engine='python', names=col_list))
    band2_df.append(pd.read_csv(band2_list[i], skiprows=8, sep=',', header=0, engine='python', names=col_list))


band1_peaks = get_max_abs(band1_df)
band2_peaks = get_max_abs(band2_df)


band1_peaks = [[0, band1_peaks[0][1]], [15, band1_peaks[1][1]], [30, band1_peaks[2][1]], [45, band1_peaks[3][1]],
               [60, band1_peaks[4][1]], [75, band1_peaks[5][1]], [90, band1_peaks[6][1]]]

band2_peaks = [[0, band2_peaks[0][1]], [15, band2_peaks[1][1]], [30, band2_peaks[2][1]], [45, band2_peaks[3][1]],
               [60, band2_peaks[4][1]], [75, band2_peaks[5][1]], [90, band2_peaks[6][1]]]

#save polarizer angle:intensity as list
b1_theta = [] #polarizer angle
b1_r = [] #max absorbance
for i in range(len(band1_peaks)):
    b1_r.append(band2_peaks[i][1])
    b1_theta.append(band2_peaks[i][0])

#convert th to radians
angle = [radians(a) for a in b1_theta]


#color bar
colors = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600']


#plotly plot
#fig = px.scatter_polar(r=b1_r, theta=b1_theta, range_theta = [0, 90],
#                       start_angle=0, direction= 'counterclockwise', color=colors)
#fig.show()

#matplotlib plot
plt.figure(figsize=(10,10))

ax = plt.subplot(1, 1, 1, projection='polar')
ax.scatter(angle, b1_r, c=colors, alpha=0.75, s=200)
#ax.set_theta_zero_location('E')
#ax.set_theta_direction(1)
#ax.plot(angle, b1_r, c=colors)

ax.set_thetamin(0)
ax.set_thetamax(90)
ax.set_ylim(0,1)
ax.set_thetagrids([0, 15, 30, 45, 60, 75, 90])
#ax.set_title('Polar Plot @ Peak Absorbance')
plt.savefig(f'{main_path}/polar_plot_band2_v.0.1.png', dpi=300, bbox_inches='tight', transparent='True')
plt.show()