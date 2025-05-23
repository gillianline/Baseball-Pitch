#Gillian Line-Luttrell


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Load the data from the CSV file
data = pd.read_csv('pitchdata.csv')


data = pd.get_dummies(data, columns=['PitchType'])

#Filter data Game 2
game_1_data = data[data['GamePk'] == 2]

#Create scatter plots for different games
def create_scatter_plot(data, title, k):
    X = data[['StrikeZoneBottom', 'StrikeZoneTop'] + [col for col in data.columns if col.startswith('PitchType_')]]

    kmeans = KMeans(n_clusters=k)
    data['Cluster'] = kmeans.fit_predict(X)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    plt.figure(figsize=(8, 8))
    for i in range(k):
        cluster_data = data[data['Cluster'] == i]
        plt.scatter(cluster_data['StrikeZoneBottom'], cluster_data['StrikeZoneTop'], c=colors[i], label=f'Cluster {i+1}')

    plt.xlabel('Strike Zone Bottom')
    plt.ylabel('Strike Zone Top')
    plt.title(title)
    plt.legend()
    plt.show()

#Clustering plots for Game 2
create_scatter_plot(game_1_data, 'Game 2 Pitch Location Clusters', 7)



