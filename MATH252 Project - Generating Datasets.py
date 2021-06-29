# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:57:46 2020

@author: Max & Devinesh
"""

print(__doc__)

import time
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

#Corr Gaussian 4

centers = [5,5],[10,10],[15,15],[20,20]
cluster_std = [.5, 1.25, 0.75, 2] #define standard deviations (diagonals) of each cluster
n_samples = 1500

# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0
transformation = [[0.6, -0.6], [-0.4, 0.8]]# change "transformation" top change the correlation
X_aniso = np.dot(varied[0], transformation)
aniso = (X_aniso, varied[1])# correlated gausian. 


# Circles 2 
# circles0 = pd.DataFrame(noisy_circles[0]).reset_index(drop=True)
# circles1 = pd.DataFrame(noisy_circles[1])
# circles = pd.concat([circles0,circles1],axis = 1)
# circles.columns = ["x","y","lable"]
# circles.to_csv('Circles2.csv') 


Cor1 = pd.DataFrame(aniso[0])
Cor2 = pd.DataFrame(aniso[1])
Cor3 = pd.concat([Cor1,Cor2],axis = 1)

Cor3.columns = ["x","y","lable"]
Cor3.to_csv('Cor4.csv') 

#Corr Gaussian 5

centers = [5,5],[10,10],[15,15],[20,20], [25,25]
cluster_std = [.5, 1.25, 0.75, 2, 1.5] #define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0
transformation = [[0.6, -0.6], [-0.4, 0.8]]# change "transformation" top change the correlation
X_aniso = np.dot(varied[0], transformation)
aniso = (X_aniso, varied[1])# correlated gausian. 
Cor1 = pd.DataFrame(aniso[0])
Cor2 = pd.DataFrame(aniso[1])
Cor3 = pd.concat([Cor1,Cor2],axis = 1)

Cor3.columns = ["x","y","lable"]
Cor3.to_csv('Cor5.csv') 

#Corr gaussian 3

centers = [5,5],[10,10],[15,15]
cluster_std = [.5, 1.25, 0.75] #define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0
transformation = [[0.6, -0.6], [-0.4, 0.8]]# change "transformation" top change the correlation
X_aniso = np.dot(varied[0], transformation)
aniso = (X_aniso, varied[1])# correlated gausian. 
Cor1 = pd.DataFrame(aniso[0])
Cor2 = pd.DataFrame(aniso[1])
Cor3 = pd.concat([Cor1,Cor2],axis = 1)

Cor3.columns = ["x","y","lable"]
Cor3.to_csv('Cor3.csv') 

#Corr gaussian 2

centers = [10,10],[15,15]
cluster_std = [ 1.25, 0.75] #define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0
transformation = [[0.6, -0.6], [-0.4, 0.8]]# change "transformation" top change the correlation
X_aniso = np.dot(varied[0], transformation)
aniso = (X_aniso, varied[1])# correlated gausian. 
Cor1 = pd.DataFrame(aniso[0])
Cor2 = pd.DataFrame(aniso[1])
Cor3 = pd.concat([Cor1,Cor2],axis = 1)

Cor3.columns = ["x","y","lable"]
Cor3.to_csv('Cor2.csv') 

# GMM 4

random_state = 170
centers = [[-0.11992874,2.71817015],[ 6.06204351 ,-8.33915292],[ 9.58746162, -16.80337833],[6,2]] # define two dimentional centers
#centers = [5,5],[10,10],[15,15],[20,20]
cluster_std = [1.9, 2.25, 1.25, 2] #define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0

plt.scatter(varied[0][:,0],varied[0][:,1],c = varied[1]) #look at graph corr = 0

GMM1 = pd.DataFrame(varied[0])
GMM2 = pd.DataFrame(varied[1])
GMM3 = pd.concat([GMM1,GMM2],axis = 1)
GMM3.columns = ["x","y","lable"]
GMM3.to_csv('GMM4.csv') 


# GMM 3

random_state = 170
centers = [[-0.11992874,2.71817015],[ 6.06204351 ,-8.33915292],[ 9.58746162, -16.80337833]] # define two dimentional centers
#centers = [5,5],[10,10],[15,15],[20,20]
cluster_std = [2.5, 2.25, 2] #define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0

plt.scatter(varied[0][:,0],varied[0][:,1],c = varied[1]) #look at graph corr = 0

GMM1 = pd.DataFrame(varied[0])
GMM2 = pd.DataFrame(varied[1])
GMM3 = pd.concat([GMM1,GMM2],axis = 1)
GMM3.columns = ["x","y","lable"]
GMM3.to_csv('GMM3.csv')

# GMM 2

random_state = 170
centers = [[ 6.06204351 ,-8.33915292],[ 9.58746162, -16.80337833]] # define two dimentional centers
#centers = [5,5],[10,10],[15,15],[20,20]
cluster_std = [2.25, 2] #define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0

plt.scatter(varied[0][:,0],varied[0][:,1],c = varied[1]) #look at graph corr = 0

GMM1 = pd.DataFrame(varied[0])
GMM2 = pd.DataFrame(varied[1])
GMM3 = pd.concat([GMM1,GMM2],axis = 1)
GMM3.columns = ["x","y","lable"]
GMM3.to_csv('GMM2.csv')

# GMM 5

random_state = 170
centers = [[-0.11992874,2.71817015],[ 6.06204351 ,-8.33915292],[ 9.58746162, -16.80337833],[6,2],[11,9]] # define two dimentional centers
#centers = [5,5],[10,10],[15,15],[20,20]
cluster_std = [1.9, 2.25, 1.25, 2,3]#define standard deviations (diagonals) of each cluster
n_samples = 1500
# Making The Datasets
varied = datasets.make_blobs(n_samples=n_samples,centers = centers
                             ,cluster_std=cluster_std,random_state=random_state) # gaussian mixure model.corr = 0

plt.scatter(varied[0][:,0],varied[0][:,1],c = varied[1]) #look at graph corr = 0

GMM1 = pd.DataFrame(varied[0])
GMM2 = pd.DataFrame(varied[1])
GMM3 = pd.concat([GMM1,GMM2],axis = 1)
GMM3.columns = ["x","y","lable"]
GMM3.to_csv('GMM5.csv') 

