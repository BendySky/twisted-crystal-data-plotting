from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = '***.csv'


df = pd.read_csv(data)
### choose thresholding value ###
df['Gray_Value'][df['Gray_Value'] < 13 ] = 0

id_peak = find_peaks(df['Gray_Value'])[0]
peaks_new = df.iloc[id_peak]
distance = peaks_new['Distance_(µm)']
#increment of 1 == ::1; increment of 2 == ::2
distance = distance[::1]

pitch = np.diff(distance)
#pitch = [i for i in pitch if i <= 3]
print("Pitch of drawn lines:\n", pitch)
print("\n")
print('Number of Pitches:', (len(pitch)))
print("Average Pitch: ", np.average(pitch))
print('Standard Deviation: ', np.std(pitch))
print('Error: ',1.96*(np.std(pitch))/(np.sqrt(len(pitch))))


def find_peaks(csv_file):

       file = pd.read_csv(csv_file)

       id_peak = find_peaks(file['Gray_Value'])[0]
       peaks_new = df.iloc[id_peak]
       distance = peaks_new['Distance_(µm)']
       distance = distance[::2]

       return distance

def calc_pitch(peaks):

       peaks = find_peaks(peaks)
       pitch = np.diff(peaks)
       # pitch = [i for i in pitch if i <= 2.5]
       print("Pitch of drawn lines:\n", pitch)
       print("\n")
       print('Number of Pitches:', (len(pitch)))
       print("Average Pitch: ", np.average(pitch))
       print('Standard Deviation: ', np.std(pitch))
       print('Error: ', 1.96 * (np.std(pitch)) / (np.sqrt(len(pitch))))