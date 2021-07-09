#Hierarchical-Cluster-Techniques

##CS252 Project:

##Objective: 
Generate 2-3 datsets. Use at least 3 different linkage types, and compare the optimal amount of clusters for each dataset according to the output of each of the three internal validation indices. Then, compare similarity of each of the clustering outcomes to the known clusters of each dataset 

##Cluster Types:
(1) Spherical Classes/Circles - 2 or more smaller circles surrounded by a larger circle
(2) Non-Zero covariance
(3) Gaussian Mixture Model

##Measure: 
Calinski and Harabasz Index: ratio between the within-cluster dispersion and between cluster dispersion.

##Linkages:
Chose the following three (3) linkage methods:
(1) Single Linkage: combine elements/clusters in a bottom-up fashion. At each step, combine the closest pair of elements.
(2) Average Linkage: average distance between two pairs is used. Takes into account the size of each cluster.  
(3) McQuitty: distance is calculated as follows: (distkj + distij)/2

##Generating the Datasets:
(2) Gaussian Micture Models
We use the function rmvnorm from the package mvtnorm to generate random numbers following a multivariate normal distribution.

The function rmovMF from the movMF package generates samples given the two parameters of the Von Mises-Fisher distribution. 

(3) Spherical
For this, we will create data for one spiral, by creating columns for:

the angle which spreads evenly between angleStart and angleStart + 2.5 * pi,
the radius which decrements for each sample,
the x and y coordinates, based on the radius and the angle.
The second spiral is the same as the first one, except we take the negative values of x and y.

We then combine the two dataframes and add some noise, and shift it so the coordinates stay in the same range as in the other datasets.

Sources:
https://stats.stackexchange.com/questions/195446/choosing-the-right-linkage-method-for-hierarchical-clustering
https://www.r-bloggers.com/2018/11/generate-datasets-to-understand-some-clustering-algorithms-behavior/

