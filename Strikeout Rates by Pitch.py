import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('pitchdata.csv')


#Filter the data for Game 1 and Game 2
game1_data = data[data['GamePk'] == 1]
game2_data = data[data['GamePk'] == 2]

strikeout_pitch_calls = ['called_strike', 'swinging_strike', 'strikeout']

#Calculate strikeout rates for Game 1 and Game 2 based on 'PitchType'
def calculate_strikeout_rate(df):
    total_pitches = len(df)
    strike_pitches = (df['PitchCall'] == 'called_strike').sum()
    return strike_pitches / total_pitches

strikeout_rate_game1 = game1_data.groupby('PitchType').apply(calculate_strikeout_rate)
strikeout_rate_game2 = game2_data.groupby('PitchType').apply(calculate_strikeout_rate)

#Create separate line graphs for strikeout rates
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)  
plt.plot(strikeout_rate_game1.index, strikeout_rate_game1, marker='o')
plt.title('Game 1 Strikeout Rate by Pitch Type')
plt.xlabel('Pitch Type')
plt.ylabel('Strikeout Rate')
plt.xticks(rotation=45)

plt.subplot(2, 1, 2)  
plt.plot(strikeout_rate_game2.index, strikeout_rate_game2, marker='o')
plt.title('Game 2 Strikeout Rate by Pitch Type')
plt.xlabel('Pitch Type')
plt.ylabel('Strikeout Rate')
plt.xticks(rotation=45)

plt.tight_layout()  


plt.show()

