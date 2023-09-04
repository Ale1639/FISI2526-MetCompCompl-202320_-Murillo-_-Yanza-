import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def tuplasdata (archivo):
    listaarreglo=[]
    centinela=False
    datos=open(str(archivo),"r")
    linea=datos.readline()
    while centinela == False:
        linea=datos.readline()
        if "data: |" in linea:
            while linea != "" and centinela == False:
                linea=datos.readline().strip()
                lista=linea.split(" ")
                try:
                    float(lista[0])
                except ValueError:
                    centinela = True
                if linea != "" and centinela == False:
                    tupla=(lista[0],lista[1])
                    listaarreglo.append(tupla)
            centinela = True
    arreglo=np.array(listaarreglo,dtype=[('longitud_onda', float), ('indice_refraccion', float)])
    datos.close()
    return arreglo
print(tuplasdata("Taller_1/Vidrio/BF1.yml"))

X= "Taller_1/Plásticos Comerciales/Kapton.yml"
print(X)

def ejesgraf (archivo):
    arraytuplas=tuplasdata(archivo)
    nombre = os.path.splitext(os.path.basename(archivo))[0]
    x=[]
    y=[]
    n=0
    for i in arraytuplas:
        x.append(i[0])
        y.append(i[1])
        n+=i[1]
    ejex=(np.array(x))
    ejey=(np.array(y))
    npromedio=round(n/len(arraytuplas),3)
    desvest=round(np.std(ejey),3)
    fig,axs = plt.subplots(figsize=(5,4.5))
    axs.scatter(ejex,ejey,s=8)
    axs.set_ylabel('Índice de Refración (n)')
    axs.set_xlabel('Longitud de Onda (nm)')
    axs.set_title(nombre + " - n Promedio: " + str(npromedio) + " - Desviación Estandar: " +str(desvest))
    plt.show()
    return None

print(ejesgraf(X))