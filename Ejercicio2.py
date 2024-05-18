class Rectangulo:
  """
  Representa un rectángulo definido por dos puntos (inicial y final) de su diagonal.
  """

  def __init__(self, punto_inicial=Punto(0, 0), punto_final=Punto(0, 0)):
    """
    Inicializa un rectángulo con los puntos inicial y final de su diagonal.

    Args:
      punto_inicial (Punto): Punto inicial de la diagonal (por defecto, (0, 0)).
      punto_final (Punto): Punto final de la diagonal (por defecto, (0, 0)).
    """
    self.punto_inicial = punto_inicial
    self.punto_final = punto_final

  def base(self):
    """
    Calcula y devuelve la base del rectángulo (diferencia en X).

    Returns:
      float: La longitud de la base.
    """
    return abs(self.punto_final.x - self.punto_inicial.x)

  def altura(self):
    """
    Calcula y devuelve la altura del rectángulo (diferencia en Y).

    Returns:
      float: La longitud de la altura.
    """
    return abs(self.punto_final.y - self.punto_inicial.y)

  def area(self):
    """
    Calcula y devuelve el área del rectángulo (base * altura).

    Returns:
      float: El área del rectángulo.
    """
    return self.base() * self.altura()

# Ejemplo de uso
rectangulo1 = Rectangulo(Punto(2, 3), Punto(5, 5))
rectangulo2 = Rectangulo(Punto(-1, 0), Punto(2, 3))

print(f"Rectángulo 1: Base = {rectangulo1.base():.2f}, Altura = {rectangulo1.altura():.2f}, Área = {rectangulo1.area():.2f}")  # Salida: Base = 3.00, Altura = 2.00, Área = 6.00
print(f"Rectángulo 2: Base = {rectangulo2.base():.2f}, Altura = {rectangulo2.altura():.2f}, Área = {rectangulo2.area():.2f}")  # Salida: Base = 3.00, Altura = 3.00, Área = 9.00
