library(stats)
library(cluster)
library(fpc)
library(clv)
library(ggplot2)
library(clValid)
library(dplyr)
library(MixGHD)
library(ggpubr)

Circles2 <- read.csv("C:\\Users\\hate4\\Circles2.csv", header = T)
Cor2 <- read.csv("C:\\Users\\hate4\\Cor2.csv", header = T)
Cor3 <- read.csv("C:\\Users\\hate4\\Cor3.csv", header = T)
Cor4<- read.csv("C:\\Users\\hate4\\Cor4.csv", header = T)
Cor5<-read.csv("C:\\Users\\hate4\\Cor5.csv", header = T)
GMM2<-read.csv("C:\\Users\\hate4\\GMM2.csv", header = T)
GMM3<-read.csv("C:\\Users\\hate4\\GMM3.csv", header = T)
GMM4<- read.csv("C:\\Users\\hate4\\GMM4.csv", header = T)
GMM5<-read.csv("C:\\Users\\hate4\\GMM5.csv", header = T)

# Making Circles 4
Test1<-rbind(DATA[[1]][,1:2],DATA[[1]][,1:2]*4)
Test2<-t(cbind(t(DATA[[1]][,3]),t(DATA[[1]][,3]+2)))
Test3<-cbind(Test1,Test2)
Test4 <- Test3 %>% slice(-seq(2,length(Test3[,1]),2))
Circles4<-cbind(NA*length(Test4[,1]),Test4)



Results<-list()
DATA<-list(Circles2,Circles4,Cor2,Cor3,Cor4,Cor5,GMM2,GMM3,GMM4,GMM5)# add all datasets!
for (j in 1:length(DATA)) #wrengle data and put all 3 Higharchical clusters into the right "pots."
{
  DATA[[j]]<- DATA[[j]][2:4] # Wrangle the Data
  DATA[[j]][,3]<-DATA[[j]][,3]+1 # Wrangle the Data
  Single.Results<-hclust(dist(DATA[[j]][,1:2]),method = "single")
  Average.Results<-hclust(dist(DATA[[j]][,1:2]),method = "average")
  Mcquitty.Results<-hclust(dist(DATA[[j]][,1:2]),method = "mcquitty")
  Results[[j]]<-list(Single.Results,Average.Results,Mcquitty.Results)
} 


As<- array(NA,dim = c( n = length(DATA[[1]][,2]),Clusters = 6,data = length(DATA))) # array for single linkage
Aa<- array(NA,dim = c( n = length(DATA[[1]][,2]),Clusters = 6,data = length(DATA))) # array for ave linkage
Am<- array(NA,dim = c( n = length(DATA[[1]][,2]),Clusters = 6,data = length(DATA))) # array for mcquitty linkage

for (k in 1:3) # is is type of linkage: 1 = single, 2 = ave , 3 = mcwitty
{  
  for (j in 1:length(DATA)) # datasets: 1 = circles2, 2 = circles3 etc...
  #for (linkage in dateset)
  {
    M<-matrix(NA,length(DATA[[j]][,3]),6)
    for (i in 2:6) # number of clusters as a result of the cutree function.
      {
        M[,i]<-cutree(Results[[j]][[k]],i)  #(# datapoints)x(#Clusters(from cutree)) matrix
      }
    if (k == 1){As[,,j]<-M}
    else if (k == 2){Aa[,,j]<-M}
    else if (k == 3){Am[,,j]<-M}
  }
}
Adim4<-list(As,Aa,Am) #Adim4[[Which Linkage]][obs,nclust,dataset] #COntains all the "cutree" values for all possible combinations.

DONE<-array(NA,dim =c(length(Adim4[[1]][1,,1]),3,length(DATA)),dimnames = list(1:6,c("CH-Single","CH-Complete","CH-Mcquitty"),c("Circles2","Circles4","Cor2","Cor3","Cor4","Cor5","GMM2","GMM3","GMM4","GMM5"))) #DONE[nclusters(from cutree),linkages,] Array "Done" will contain 
#j=2

for (j in 1:length(DATA))
{
  for(i in 2:length(Adim4[[1]][1,,1]))
  {
    # Compares sillhouettesAve, dunn & CH internal validation chriteria. It seems that the dunn index did not function as hoped, and so this comparison was aborted in favor of other, more useful findings.
    # DONE[i,1,j]<-mean(silhouette(Adim4[[1]][,i,1],dist(DATA[[jp]][,1:2]))[,3])
    # DONE[i,2,j]<- calinhara(DATA[[j]][,1:2],Adim4[[1]][,i,1],i)
    # DONE[i,3,j]<-dunn(distance = NULL,clusters = Adim4[[1]][,i,1],Data = DATA[[j]][,1:2],method = "euclidean")
    
    DONE[i,1,j]<-calinhara(DATA[[j]][,1:2],Adim4[[1]][,i,1],i)
    DONE[i,2,j]<- calinhara(DATA[[j]][,1:2],Adim4[[2]][,i,1],i)
    DONE[i,3,j]<-calinhara(DATA[[j]][,1:2],Adim4[[3]][,i,1],i)
    

  }  
}


# The numbers lables of the decided upon by the the CH criterion. Each dataset plot was plotted. The ideal clustering of each of the linkage types (according to CH... chriterion, at least) were plotted side by side. This was done by hand for each of the ten datasets.
p <- ggplot(DATA[[10]][,1:2],aes(x=x,y=y))
P1 = p+geom_point(color =Adim4[[1]][,5,10])
P2 = p+geom_point(color =Adim4[[2]][,2,10])
P3 = p+geom_point(color =Adim4[[3]][,2,10])

ggarrange(P1, P2, P3, 
          labels = c("Single", "Ave", "Mcquitty"),
          ncol = 3, nrow = 1)

#Each linkage allocation was compared to the actual cluster allocation. The ARI was used as a measurement of the results.
ARI.1<-ARI(DATA[[10]][,3],Adim4[[1]][,5,10])
ARI.2<-ARI(DATA[[10]][,3],Adim4[[2]][,2,10])
ARI.3<-ARI(DATA[[10]][,3],Adim4[[3]][,2,10])
ARI.T = c(ARI.1,ARI.2,ARI.3)
dim(ARI.T) = c(1,3)
colnames(ARI.T)<-c("ARI Single","ARI Ave","ARI Mcquitty")
data.frame(ARI.T)



p <- ggplot(DATA[[2]][,1:2],aes(x=x,y=y))
P1 = p+geom_point(color =Adim4[[1]][,5,2])
P2 = p+geom_point(color =Adim4[[2]][,4,2])
P3 = p+geom_point(color =Adim4[[3]][,2,2])

ggarrange(P1, P2, P3, 
          labels = c("Single", "Ave", "Mcquitty"),
          ncol = 3, nrow = 1)

#Each linkage allocation was compared to the actual cluster allocation. The ARI was used as a measurement of the results.
ARI.1<-ARI(DATA[[2]][,3],Adim4[[1]][,5,2])
ARI.2<-ARI(DATA[[2]][,3],Adim4[[2]][,4,2])
ARI.3<-ARI(DATA[[2]][,3],Adim4[[3]][,2,2])
ARI.T = c(ARI.1,ARI.2,ARI.3)
dim(ARI.T) = c(1,3)
colnames(ARI.T)<-c("ARI Single","ARI Ave","ARI Mcquitty")
data.frame(ARI.T)
