class Punto:
  """
  Representa un punto en el plano cartesiano con sus coordenadas X e Y.
  """

  def __init__(self, x=0, y=0):
    """
    Inicializa un punto con las coordenadas especificadas.

    Args:
      x (float): Coordenada X (horizontal). Predeterminado: 0.
      y (float): Coordenada Y (vertical). Predeterminado: 0.
    """
    self.x = x
    self.y = y

  def __str__(self):
    """
    Devuelve una representación textual del punto en formato (X, Y).
    """
    return f"({self.x}, {self.y})"

  def cuadrante(self):
    """
    Indica en qué cuadrante se encuentra el punto.

    Returns:
      int: Número de cuadrante (1, 2, 3 o 4).
      - 0: Si el punto está en el origen.
      - None: Si el punto está sobre uno de los ejes (X o Y).
    """
    if self.x == 0 and self.y == 0:
      return 0
    elif self.x > 0 and self.y > 0:
      return 1
    elif self.x < 0 and self.y > 0:
      return 2
    elif self.x < 0 and self.y < 0:
      return 3
    elif self.x > 0 and self.y < 0:
      return 4
    else:
      return None

  def vector(self, otro_punto):
    """
    Calcula el vector resultante entre dos puntos.

    Args:
      otro_punto (Punto): El punto final del vector.

    Returns:
      Punto: Vector resultante (diferencia entre las coordenadas).
    """
    return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

  def distancia(self, otro_punto):
    """
    Calcula la distancia entre dos puntos utilizando la fórmula de la distancia euclidiana.

    Args:
      otro_punto (Punto): El punto al que se calcula la distancia.

    Returns:
      float: Distancia entre los dos puntos.
    """
    import math
    return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

# Ejemplo de uso
punto1 = Punto(2, 3)
punto2 = Punto(5, 5)
punto3 = Punto(-3, -1)
punto4 = Punto(0, 0)

print(f"Punto 1: {punto1}")  # Salida: (2, 3)
print(f"Punto 2: {punto2}")  # Salida: (5, 5)
print(f"Punto 3: {punto3}")  # Salida: (-3, -1)
print(f"Punto 4: {punto4}")  # Salida: (0, 0)

print(f"Punto 1 en cuadrante: {punto1.cuadrante()}")  # Salida: 1
print(f"Punto 3 en cuadrante: {punto3.cuadrante()}")  # Salida: 3
print(f"Punto 4 en cuadrante: {punto4.cuadrante()}")  # Salida: 0

vector_ab = punto1.vector(punto2)
print(f"Vector AB: {vector_ab}")  # Salida: (3, 2)

distancia_ab = punto1.distancia(punto2)
print(f"Distancia entre A y B: {distancia_ab:.2f}")  # Salida: 5.00

distancia_ba = punto2.distancia(punto1)
print(f"Distancia entre B y A: {distancia_ba:.2f}")  # Salida: 5.00

# Punto más lejano al origen (opcional)
puntos = [punto1, punto2, punto3]
punto_mas_lejano = max(puntos, key=lambda p: p.distancia(punto4))
print(f"Punto más lejano al origen: {punto_mas_lejano}")  # Salida: (-3, -1)

# Ejemplo de uso con más puntos
punto5 = Punto(1, -2)
punto6 = Punto(6, 7)
punto7 = Punto(-4, 3)

puntos_todos = [punto1, punto2, punto3, punto4, punto5, punto6, punto7]
punto_mas_lejano_todos = max(puntos_todos, key=lambda p: p.distancia(punto4))
print(f"Punto más lejano al origen (todos los puntos): {punto_mas_lejano_todos}")
