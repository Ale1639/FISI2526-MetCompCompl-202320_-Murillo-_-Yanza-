from mineral import Mineral
import numpy as np

minerales = []
with open("FISI2526-MetCompCompl-202320_-Murillo-_-Yanza-/Taller_1/minerales.txt" , 'r') as archivo:
    lineas = archivo.readlines()
    titulos = lineas[0].strip().split('\t')
    for linea in lineas[1:]:
        valores = linea.strip().split('\t')
        if len(valores) == len(titulos):
            datos = dict(zip(titulos, valores))
            mineral = Mineral(datos['nombre'], float(datos['dureza']), datos['lustre'], datos['rompimiento_por_fractura'],
                              datos['color'], datos['composicion'],
                              datos['sistema cristalino'], float(datos['specific_gravity']))
            minerales.append(mineral)
    minerales=np.array(minerales)


contador_silicatos = sum(1 for mineral in minerales if Mineral.es_silicato(mineral))

total_densidad = sum(float(Mineral.calcular_densidad(mineral)) for mineral in minerales)

densidad_promedio = total_densidad / len(minerales)

print(f"Número de minerales silicatos: {contador_silicatos}")
print(f"Densidad promedio de los minerales: {densidad_promedio} g/cm^3")

