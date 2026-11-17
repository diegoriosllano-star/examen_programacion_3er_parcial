# PARTE 2. CLASE ESTACIONAMIENTO


# PROBLEMA
# Calcular el importe total que debe pagar un vehículo
# según la cantidad de horas que permaneció estacionado.


# ENTRADA
# horas : int
# Cantidad de horas estacionadas.
# Debe ser un número entero mayor que cero.


# SALIDA
# Mostrar:
# - Horas estacionadas.
# - Total a pagar en pesos con dos decimales.


# REGLAS Y SUPUESTOS
# - Si la estancia es de 1 a 2 horas, la tarifa es de $15.00 por hora.
# - Si la estancia es de 3 a 5 horas, la tarifa es de $12.00 por hora.
# - Si la estancia es mayor a 5 horas, la tarifa es de $10.00 por hora.
# - La tarifa correspondiente se aplica a TODAS las horas registradas.
# - Las horas deben ser un número entero mayor que cero.
# - El total debe mostrarse con dos decimales.


# CLASE
# Nombre: Estacionamiento
# Responsabilidad:
# Guardar las horas estacionadas, calcular el pago correspondiente
# y mostrar el recibo.


# PROPIEDADES
# horas : int
# Guarda la cantidad de horas estacionadas.


# CONTRATO DE CLASE
# class Estacionamiento:
#
#   __init__(self, horas) -> None:
#       Recibe las horas y las guarda en self.horas.
#
#   calcularPago(self) -> float:
#       Calcula y devuelve el importe total según las tarifas.
#
#   mostrarRecibo(self) -> None:
#       Utiliza calcularPago() y muestra:
#       RECIBO DE ESTACIONAMIENTO
#       Horas: cantidad
#       Total a pagar: $importe


# ALGORITMO
# 1. Solicitar al usuario las horas estacionadas.
# 2. Convertir las horas a int.
# 3. Comprobar que horas sea mayor que cero.
# 4. Si el valor es válido:
#       Crear un objeto Estacionamiento con las horas.
#       Llamar al método mostrarRecibo().
#
# 5. En calcularPago():
#       Si self.horas <= 2:
#           tarifa = 15
#       En caso contrario, si self.horas <= 5:
#           tarifa = 12
#       En caso contrario:
#           tarifa = 10
#
#       pago = self.horas * tarifa
#       Devolver pago.
#
# 6. mostrarRecibo() debe llamar a calcularPago()
#    y mostrar el resultado con dos decimales.


# CASOS DE PRUEBA
# 2 horas:
# 2 * 15 = $30.00
#
# 4 horas:
# 4 * 12 = $48.00
#
# 6 horas:
# 6 * 10 = $60.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente la clase Estacionamiento.
# - Usa únicamente los métodos indicados:
#   __init__, calcularPago y mostrarRecibo.
# - Utiliza self para acceder a la propiedad horas.
# - calcularPago() debe utilizar if / elif / else.
# - mostrarRecibo() debe llamar a calcularPago().
# - No agregues clases ni métodos adicionales.
# - No agregues bibliotecas externas.
# - No cambies las tarifas especificadas.
# - No agregues funcionalidades que no hayan sido solicitadas.


# Implementa la solución exactamente según esta especificación.

class Estacionamiento:
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if self.horas <= 2:
            tarifa = 15
        elif self.horas <= 5:
            tarifa = 12
        else:
            tarifa = 10

        return self.horas * tarifa

    def mostrarRecibo(self):
        total = self.calcularPago()

        print("RECIBO DE ESTACIONAMIENTO")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total:.2f}")


horas = int(input("Horas estacionadas: "))

if horas > 0:
    estacionamiento = Estacionamiento(horas)
    estacionamiento.mostrarRecibo()
else:
    print("Las horas deben ser mayores que cero.")