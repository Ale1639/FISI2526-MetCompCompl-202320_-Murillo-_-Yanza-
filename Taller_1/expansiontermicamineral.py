import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from mineral import Mineral


class ExpansionTermicaMineral (Mineral):
    def __init__(self, archivo):
        linea= pd.read_csv(archivo,sep=",")
        self.temperatura=np.array(linea["celsius_temperature"])
        self.volumen= np.arrray(linea["volume_cc"])
    
    def coeficiente_exp(self):
        def diff_cen(yi,yf,xi,xf):
            return (yf-yi)/(2*(xf-xi))
        ytemp=np.zeros(len(self.temperatura),2)
        x=np.zeros(len(self.temperatura),2)
        sum=0
        for temp in range(len(self.temperatura)):
            ytemp[temp][0]=self.temperatura[temp]
            x[temp][0]=self.temperatura[temp]

        for cont in range(len(self.temperatura)):
            if cont==(len(self.temperatura)-1):
                ytemp[cont][1]=diff_cen(self.temperatura[cont-1],self.temperatura[cont],self.volumen[cont-1],self.volumen[cont])
                x[cont][1]=(1/self.volumen[cont])*ytemp[cont][1]
            elif cont==0:
                ytemp[cont][1]=diff_cen(self.temperatura[cont],self.temperatura[cont+1],self.volumen[cont],self.volumen[cont+1])
                x[cont][1]=(1/self.volumen[cont])*ytemp[cont][1]
            else:
                ytemp[cont][1]=diff_cen(self.temperatura[cont-1],self.temperatura[cont+1],self.volumen[cont-1],self.volumen[cont+1])
                x[cont][1]=(1/self.volumen[cont])*ytemp[cont][1]
        for i in range (len(self.temperatura)):
            sum+=x[i][1]

            error=np.std(x[:][1])
            promedio=sum/len(self.temperatura)
            figure=plt.figure(figsize=(10,4))
            abajo=figure.add_subplot(121)
            arriba=figure.add_subplot(122)
            abajo.scatter(np.array(self.temperatura),self.volumen)
            print(x[:,1])
            arriba.scatter(np.array(self.temperatura),x[:,1])

            return np.array([figure, promedio, error])

        





        