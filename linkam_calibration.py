import numpy as np

T_ty_rt = 25.0
T_ty_heat = 80.0
T_ty_slope = np.array([T_ty_rt, T_ty_heat])

print("Actual Temp @ R.T.:")
T_act_rt = float(input())

print("Actual Temp @ Heat:")
T_act_heat = float(input())

T_act_slope = np.array([T_act_rt, T_act_heat])

#Create list with wanted values
Yt = []
for i in range(25, 85, 5):
    Yt.append(i)
x_vals = np.array([len(Yt)/len(Yt), len(Yt)])


#Get Linear Fit from Expected values
b_t, m_t = np.polynomial.polynomial.polyfit(x_vals, T_ty_slope, 1)
b_a, m_a = np.polynomial.polynomial.polyfit(x_vals, T_act_slope, 1)

Ya = []
Y_set = []

#Ya = ((Yt - bt)/mt)*ma + ba
for i in range(len(Yt)):
    Ya.append(((Yt[i] - b_t)/m_t)*m_a + b_a)
    Y_set.append(2 * Yt[i] - Ya[i])
    print(f"Setpoint at {Yt[i]} ºC:", round(Y_set[i], 1), " ºC")
