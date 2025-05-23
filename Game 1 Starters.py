#Gillian Line-Luttrell

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('pitchdata.csv')

#Filter data for Pitcher 11
pitcher_11_data = df[df['PitcherId'] == 11]

#Filter data for Pitcher 18 
pitcher_1_data = df[df['PitcherId'] == 1]

#Pitch types and corresponding colors for Pitcher 11
pitch_types = pitcher_11_data['PitchType'].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(pitch_types)))

#Scatter plot with different colors for each pitch type for Pitcher 11
plt.figure(figsize=(10, 6))
for i, pitch_type in enumerate(pitch_types):
    pitch_type_data = pitcher_11_data[pitcher_11_data['PitchType'] == pitch_type]
    plt.scatter(pitch_type_data['TrajectoryHorizontalBreak'], pitch_type_data['TrajectoryVerticalBreakInduced'], label=f'Pitcher 11 - {pitch_type}', color=colors[i], alpha=0.5)

#Scatter plot with different colors for each pitch type for Pitcher 18
for i, pitch_type in enumerate(pitch_types):
    pitch_type_data = pitcher_1_data[pitcher_1_data['PitchType'] == pitch_type]
    plt.scatter(pitch_type_data['TrajectoryHorizontalBreak'], pitch_type_data['TrajectoryVerticalBreakInduced'], label=f'Pitcher 1 - {pitch_type}', color=colors[i], marker='x', alpha=0.5)

plt.xlabel('Horizontal Break')
plt.ylabel('Vertical Break')
plt.title('Scatter Plot: Pitcher 11 and 1 Break Values by Pitch Type')
plt.grid(True)
plt.legend()
plt.show()
