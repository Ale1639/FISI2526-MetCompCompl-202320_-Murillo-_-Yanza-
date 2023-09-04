class Mineral:
    def __init__(self, nombre, dureza, rompimiento_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = dureza
        self.rompimiento_fractura = rompimiento_fractura
        self.color = color
        self.composicion = composicion
        self.lustre = lustre
        self.specific_gravity = specific_gravity
        self.sistema_cristalino = sistema_cristalino

    def es_silicato(self):
        return 'Si' in self.composicion and 'O' in self.composicion

minerales = []
with open('minerales.txt', 'r') as archivo:
    lineas = archivo.readlines()
    titulos = lineas[0].strip().split('\t')
    for linea in lineas[1:]:
        valores = linea.strip().split('\t')
        if len(valores) == len(titulos):
            datos = dict(zip(titulos, valores))
            mineral = Mineral(datos['nombre'], float(datos['dureza']), datos['rompimiento_por_fractura'],
                              datos['color'], datos['composicion'], datos['lustre'], float(datos['specific_gravity']),
                              datos['sistema cristalino'])
            minerales.append(mineral)


contador_silicatos = sum(1 for mineral in minerales if mineral.es_silicato())


total_densidad = sum(mineral.specific_gravity for mineral in minerales)
densidad_promedio = total_densidad / len(minerales)

print(f"Número de minerales silicatos: {contador_silicatos}")
print(f"Densidad promedio de los minerales en formato SI: {densidad_promedio} g/cm³")
