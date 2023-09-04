import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def tuplasdata (archivo):
    listaarreglo=[]
    centinela=False
    datos=open(str(archivo),"r")
    linea=datos.readline()
    while centinela == False:
        linea=datos.readline()
        if "data: |" in linea:
            while linea != "":
                linea=datos.readline().strip()
                if linea != "":
                    lista=linea.split(" ")
                    tupla=(lista[0],lista[1])
                    listaarreglo.append(tupla)
            centinela = True
    arreglo=np.array(listaarreglo,dtype=[('longitud_onda', float), ('indice_refraccion', float)])
    datos.close()
    return arreglo
print(tuplasdata("Taller_1/Vidrio/BF1.yml"))