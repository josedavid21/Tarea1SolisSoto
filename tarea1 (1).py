################################################################
# ITCR                                                         #
# Cristofher Solís y José David Soto                           #
# Tarea 1 Microprocesadores y microcontoladores                #
# ##############################################################
# Importar pytest


# Para crear los métodos se define una clase llamada operación, en la cual se
# desarrollarán los métodos basic_ops y array_ops


class operacion:

    # se define basic_ops: toma como parámetros de entrada dos operandos (x,y)
    # y un número que representa un selector de operación,
    # el cual se describe a continuación:
    # op=0 : suma
    # op=1 : resta
    # op=2 : AND
    # op=3 : OR

    def basic_ops(x, y, op):

        # El assert definido a continuación permite verificar que los
        # valores introducidos no contengan decimales o carácteres no númericos
        assert((type(x) == int) and (type(y) == int)
               and (type(op) == int)), "Valor inválido"

        # El siguiente assert se encarga de mostrar error en caso
        # de que un operando sea mayor a 127 o bien menor a -127.
        assert(-127 <= x <= 127 and -127 <= y <= 127),\
            "Valores no pueden ser mayores a 127 ni menores a -127"

        # El próximo assert se encarga de verificar que el selector se
        # encuentre dentro del rango definido para las operaciones (0-3).
        assert(0 <= op <= 3), "Operación inválida"

        # A continuación se presentan las operaciones por realizar
        # según el selector de operación escogido.
        # Nótese que el método regresa el resultado
        # de la operación seleccionada.

        # Suma
        if op == 0:
            result = x + y

        # Resta
        elif op == 1:
            result = x - y

        # AND
        elif op == 2:
            result = x and y

        # OR
        elif op == 3:
            result = x or y

        return result

    # Se define array_ops, el cual realiza las operaciones
    # de basic_ops entre arreglos del mismo tamaño (60)
    def array_ops(x, y, op):

        # El assert definido a continuación permite verificar
        # que los valores introducidos no contengan decimales
        # o carácteres no númericos.
        assert type(op) == int, "Valor inválido"

        # El próximo assert se encarga de verificar
        # que el selector se encuentre dentro del rango
        # definido para las operaciones (0-3).
        assert(0 <= op <= 3), "Operación inválida"

        # Se define un arreglo vacío el cual alojará los
        # resultados de cada operación (cada elemento de la lista
        # será un operando para basic_ops).
        # y será el resultado retornado por este método
        array = []

        # La siguiente variable se define para ser utilizada
        # como un contador, cuyo uso es el de recorrer el array
        # para ir aplicando basic_ops a cada elemento
        # de los array empleados.
        cont = 0

        # Seguidamente se presentan las operacion por realizar
        # según el selector de operación elegido.

        # Suma
        if op == 0:
            while(cont < len(x)):
                array.append(operacion.basic_ops(x[cont], y[cont], 0))
                cont += 1

        # Resta
        elif op == 1:
            while(cont < len(x)):
                array.append(operacion.basic_ops(x[cont], y[cont], 1))
                cont += 1

        # AND
        elif op == 2:
            while(cont < len(x)):
                array.append(operacion.basic_ops(x[cont], y[cont], 2))
                cont += 1

        # OR
        elif op == 3:
            while(cont < len(x)):
                array.append(operacion.basic_ops(x[cont], y[cont], 3))
                cont += 1

        return array
