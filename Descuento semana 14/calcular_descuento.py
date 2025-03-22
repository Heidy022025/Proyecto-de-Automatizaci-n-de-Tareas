# Definir la función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=15):
    """

    calcular el monto del descuento y lo devuelve.

    :param monto_total: Total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 15%)
    :return: Monto de descuento
    """
    # calculo el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 350
    # Devuelve el valor del descuento
    return descuento
# llamadas a la función con diferentes casos
monto = 350 # monto de a compra
descuento = calcular_descuento(monto) #se usa el descuento por defecto
print(f"Monto: ${monto} ")
print(f"Descuento: ${descuento}")
print(f"Total a pagar: ${monto - descuento}")