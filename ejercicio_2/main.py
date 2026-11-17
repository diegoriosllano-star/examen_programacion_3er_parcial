# PARTE 3. CALCULADORA CON HERENCIA


# PROBLEMA
# Crear una calculadora sencilla utilizando herencia.
# La clase padre realizará una suma y la clase hija realizará una resta.


# ENTRADAS
# numero1 : float
# Primer número ingresado por el usuario.
#
# numero2 : float
# Segundo número ingresado por el usuario.


# SALIDAS
# Mostrar:
# - Resultado de la suma.
# - Resultado de la resta.


# CLASE PADRE
# Nombre: Operacion
# Responsabilidad:
# Guardar dos números, realizar una suma y mostrar el resultado.


# PROPIEDADES
# numero1 : float
# numero2 : float


# CONTRATO DE CLASE PADRE
# class Operacion:
#
#   __init__(self, numero1, numero2) -> None:
#       Recibe los dos números y los guarda en
#       self.numero1 y self.numero2.
#
#   calcular(self) -> float:
#       Devuelve la suma de self.numero1 y self.numero2.
#
#   mostrarResultado(self) -> None:
#       Llama al método calcular() y muestra el resultado.


# CLASE HIJA
# Nombre: Resta
# Hereda de: Operacion
# Responsabilidad:
# Utilizar las propiedades heredadas y cambiar el cálculo
# para realizar una resta.


# CONTRATO DE CLASE HIJA
# class Resta(Operacion):
#
#   calcular(self) -> float:
#       Sobrescribe calcular() y devuelve
#       self.numero1 - self.numero2.
#
# - Resta NO debe tener un __init__ propio.
# - Debe utilizar el constructor heredado de Operacion.
# - Debe heredar mostrarResultado() sin volver a escribirlo.


# ALGORITMO
# 1. Solicitar numero1 al usuario.
# 2. Solicitar numero2 al usuario.
# 3. Crear un objeto Operacion con ambos números.
# 4. Crear un objeto Resta con ambos números.
# 5. Mostrar el texto "Resultado de la suma:".
# 6. Llamar a mostrarResultado() del objeto Operacion.
# 7. Mostrar el texto "Resultado de la resta:".
# 8. Llamar a mostrarResultado() del objeto Resta.
#
# Cuando mostrarResultado() se ejecute:
# - En un objeto Operacion, calcular() realizará una suma.
# - En un objeto Resta, calcular() realizará una resta.


# CASOS DE PRUEBA
# Caso obligatorio:
# numero1 = 20
# numero2 = 8
# suma = 28
# resta = 12
#
# También realizar otra ejecución con valores diferentes.


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente las clases Operacion y Resta.
# - Operacion debe contener __init__, calcular y mostrarResultado.
# - Resta debe heredar de Operacion.
# - Resta solo debe sobrescribir calcular().
# - No agregues un __init__ a Resta.
# - No dupliques propiedades en Resta.
# - mostrarResultado() debe llamar a calcular().
# - No agregues clases ni métodos adicionales.
# - No agregues bibliotecas externas.
# - No agregues funcionalidades que no estén solicitadas.


# Implementa la solución exactamente según esta especificación.

class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2

    def mostrarResultado(self):
        print(f"{self.calcular():g}")


class Resta(Operacion):
    def calcular(self):
        return self.numero1 - self.numero2


numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))

operacion = Operacion(numero1, numero2)
resta = Resta(numero1, numero2)

print("Resultado de la suma: ", end="")
operacion.mostrarResultado()

print("Resultado de la resta: ", end="")
resta.mostrarResultado()