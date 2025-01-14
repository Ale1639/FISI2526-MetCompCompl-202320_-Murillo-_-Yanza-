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
        return 'Si' in self.composicion and 'O' in self.composicion

    def calcular_densidad(self):
        #(gramos por centímetro cúbico)
        return self.specific_gravity * 1000
    
    def visualizar_color(self):
        plt.figure()
        plt.imshow([[self.color]])
        plt.axis('off')
        plt.show()

    def imprimir_info(self):
        print(f"Dureza: {self.dureza}")
        print(f"Tipo de Rompimiento: {'Fractura' if self.rompimiento_fractura else 'Escisión'}")
        print(f"Sistema de Organización de los Átomos: {self.sistema_cristalino}")
