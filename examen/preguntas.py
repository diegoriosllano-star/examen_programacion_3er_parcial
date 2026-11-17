# ACTIVIDAD 1. IDENTIFICAR ELEMENTOS DE POO


class Producto(object):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.total = 0

    def calcularTotal(self, cantidad):
        self.total = self.precio * cantidad

    def mostrarTotal(self):
        print(f"Producto: {self.nombre}")
        print(f"Total: ${self.total:.2f}")


producto1 = Producto("Cuaderno", 35)
producto1.calcularTotal(3)
producto1.mostrarTotal()


# 1. ¿Cuál es el nombre de la clase?
# Producto


# 2. ¿Cuáles son sus propiedades?
# nombre, precio y total.


# 3. ¿Cuáles son sus métodos?
# __init__(), calcularTotal() y mostrarTotal().


# 4. ¿Qué función cumple __init__?
# Inicializa las propiedades del objeto cuando se crea.


# 5. ¿Para qué se utiliza self?
# Se utiliza para hacer referencia al objeto actual y acceder
# a sus propiedades y métodos.


# 6. ¿En qué instrucción se crea un objeto?
# producto1 = Producto("Cuaderno", 35)


# 7. ¿Cuál es el nombre del objeto?
# producto1


# 8. ¿Cómo se llama a calcularTotal()?
# producto1.calcularTotal(3)


# 9. ¿Qué valores recibe el constructor cuando se crea el objeto?
# "Cuaderno" y 35.


# 10. ¿Qué resultado mostrará el programa?
# Producto: Cuaderno
# Total: $105.00



# ACTIVIDAD 2. COMPLETAR CÓDIGO


class Rectangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def mostrarArea(self):
        print(f"El área del rectángulo es: {self.calcularArea()}")


rectangulo1 = Rectangulo(8, 5)
rectangulo1.mostrarArea()



# ACTIVIDAD 3. INTERPRETAR HERENCIA


class Operacion(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2


class Multiplicacion(Operacion):
    def calcular(self):
        return self.numero1 * self.numero2


operacion1 = Operacion(8, 4)
operacion2 = Multiplicacion(8, 4)

print(operacion1.calcular())
print(operacion2.calcular())


# 1. ¿Cuál es la clase padre?
# Operacion


# 2. ¿Cuál es la clase hija?
# Multiplicacion


# 3. ¿Cómo se indica la herencia?
# Se indica escribiendo la clase padre entre paréntesis:
# class Multiplicacion(Operacion):


# 4. ¿Qué propiedades utiliza la clase hija?
# numero1 y numero2.


# 5. ¿Por qué puede utilizarlas sin definir su propio __init__?
# Porque Multiplicacion hereda el __init__ de Operacion.


# 6. ¿Por qué los métodos calcular() tienen resultados distintos?
# Porque la clase Multiplicacion hereda de Operacion, pero redefine
# el método calcular(). La clase Operacion usa calcular() para sumar
# numero1 y numero2, mientras que Multiplicacion sobrescribe ese mismo
# método para multiplicarlos. Por eso, aunque ambos objetos tienen las
# mismas propiedades, cada clase ejecuta una operación diferente.


# 7. ¿Qué valores se imprimen?
# 12
# 32


# 8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
# Multiplicacion heredaría el método calcular() de Operacion.
# Por lo tanto, en lugar de multiplicar realizaría una suma
# y operacion2.calcular() devolvería 12.