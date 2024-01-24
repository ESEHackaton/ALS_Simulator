#This is all information based from Neurokit2 Repo, see there repo for more information
# https://github.com/neuropsychology/NeuroKit/
import neurokit2 as nk
import pandas as pd

# Alternate heart rate and noise levels
ecg50 = nk.ecg_simulate(duration=10, noise=0.05, heart_rate=50)
ecg100 = nk.ecg_simulate(duration=10, noise=0.01, heart_rate=100)

df = pd.DataFrame(ecg50) #conversion panda dataframe
df.to_csv("ecg50.csv",  header=False, index=False)
df = pd.DataFrame(ecg100) #conversion panda dataframe
df.to_csv("ecg100.csv",  header=False, index=False,)

# Simulate Respiratory
rsp15_sim = nk.rsp_simulate(duration=20, respiratory_rate=15, method="sinusoidal")
rsp15_com = nk.rsp_simulate(duration=20, respiratory_rate=15, method="breathmetrics")
rsp7 = nk.rsp_simulate(duration=20, respiratory_rate=7, method="breathmetrics")

#save to file in order to use with Embedded Controller
df = pd.DataFrame(rsp15_sim)
df.to_csv("rsp15_sim.csv", header=False, index=False) #conversion
df = pd.DataFrame(rsp15_com)
df.to_csv("rsp15_com.csv",  header=False, index=False)
df = pd.DataFrame(rsp7)
df.to_csv("rsp7.csv", header=False, index=False)
