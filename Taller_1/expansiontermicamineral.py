import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from mineral import Mineral


class ExpansionTermicaMineral (Mineral):
    def __init__(self, archivo):
        linea= pd.read_csv(archivo,",")
        self.temperatura=np.array(linea["celsius_temperature"])
        self.volumen= np.arrray(linea["volume_cc"])

    def coeficiente_dila(self):
        def diff_cen(yi,yf,xi,xf):
            return (yf-yi)/(2*(xf-xi))
        ytemp=np.zeros(len(self.temperaturas),2)
        x=np.zeros(len(self.temperaturas),2)

        for temp in range(len(self.temperatura)):
            ytemp[temp][0]=self.temperatura[temp]
            x[temp][0]=self.temperatura[temp]

        for cont in range(len(self.temperatura)):
            if cont==0:
                
        