import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

class Warehouses:
    def get_warehouses(self, csv_name, number_of_clusters):
        cities = pd.read_csv(csv_name)

        europec = cities[cities['CNTRY_NAME'].isin(['Austria', 'Belgium', 'Cyprus',
        'Czech Republic', 'Denmark'
        'Estonia', 'Finland', 'France',
        'Germany', 'United Kingdom',
        'Greece', 'Hungary', 'Iceland',
        'Ireland', 'Italy', 'Latvia',
        'Lithuania', 'Luxembourg',
        'Netherlands', 'Norway',
        'Poland', 'Portugal', 'Romania',
        'Slovakia', 'Slovenia', 'Spain',
        'Sweden', 'Switzerland'])]

        cities = ['Funchal', 'Ponta Delgada', 'Santa Cruz de Tenerife', 'Las Palmas']
        europec = europec[~europec['CITY_NAME'].isin(cities)]
        europec = europec.reset_index()
        clf = KMeans(n_clusters=number_of_clusters)
        X = europec[['X', 'Y']].as_matrix()
        clf.fit(X)
        centroids = clf.cluster_centers_
        labels = clf.labels_
        return centroids, labels, europec
    def get_attachments(self, csv_name, number_of_clusters):
        centroids, labels, europec = self.get_warehouses(csv_name, number_of_clusters)
        europec.loc[:,'warehouse'] = pd.Series(labels, index = europec.index)
        europec['wareX'] = centroids[europec['warehouse'], 0]
        europec['wareY'] = centroids[europec['warehouse'], 1]
        warehousesdf = pd.DataFrame(columns =['X', 'Y'])
        warehousesdf['X'] = centroids[:, 0]
        warehousesdf['Y'] = centroids[:, 1]
        return warehousesdf, europec
