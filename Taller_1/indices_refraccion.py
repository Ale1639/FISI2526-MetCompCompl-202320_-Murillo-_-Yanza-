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

X= tuplasdata("Taller_1/Plásticos Comerciales/Kapton.yml")
print(X)
def ejesgraf (arraytuplas):
    x=[]
    y=[]
    for i in arraytuplas:
        x.append(i[0])
        y.append(i[1])
    ejex=(np.array(x))
    ejey=(np.array(y))
    plt.scatter(ejex,ejey)
    plt.show()
    return None

print(ejesgraf(X))