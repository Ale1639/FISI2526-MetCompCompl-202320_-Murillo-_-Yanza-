import matplotlib.pyplot as plt

class Mineral:
    def __init__(self, nombre, dureza, lustre, rompimiento_fractura, color, composicion, sistema_cristalino, specific_gravity):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_fractura = rompimiento_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def __str__(self):
        return f"Mineral: {self.nombre}\nDureza: {self.dureza}\nLustre: {self.lustre}\nRompimiento por Fractura: {self.rompimiento_fractura}\nColor: {self.color}\nComposición Química: {self.composicion}\nSistema Cristalino: {self.sistema_cristalino}\nGravedad Específica: {self.specific_gravity}"

    def es_silicato(self):
        # Verificar si la composición química contiene Si (silicio) y O (oxígeno)
        return 'Si' in self.composicion and 'O' in self.composicion

    def calcular_densidad(self):
        # Calcular la densidad en unidades SI (gramos por centímetro cúbico)
        return self.specific_gravity * 1000
    def visualizar_color(self):
        # Visualizar el color utilizando matplotlib
        plt.figure()
        plt.imshow([[self.color]])
        plt.axis('off')
        plt.show()
