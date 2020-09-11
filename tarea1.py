################################################################
# ITCR                                                         #
# Cristofher Solís y José David Soto                           #
# Tarea 1 Microprocesadores y microcontoladores                #
# ##############################################################


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
    # La salida corresponde al resultado de la operación

    def basic_ops(x, y, op):

        # El error definido a continuación permite verificar que los
        # valores introducidos no contengan decimales o carácteres no númericos
        if not((type(x) == int) and (type(y) == int)
               and (type(op) == int)):
            return "E001"

        # El siguiente error se retorna en caso
        # de que un operando sea mayor a 127 o bien menor a -127.
        elif not(-127 <= x <= 127 and -127 <= y <= 127):
            return "E002"

        # El próximo error aparece en caso de que el selector se
        # encuentre fuera del rango definido para las operaciones [0-3].
        elif not(0 <= op <= 3):
            return "E003"

        # A continuación se presentan las operaciones por realizar
        # según el selector de operación escogido.
        # Nótese que el método regresa el resultado
        # de la operación seleccionada.
        else:
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
    # de basic_ops entre arreglos del mismo tamaño.
    # Toma como parámetros de entrada dos arrays (x, y) y
    # un selector de operación (op) el cual se describe
    # de la misma manera que el parámetro "op" de basic_ops
    # Su salida corresponde a un arreglo con los resultados
    # de la operación para cada elemento de los array
    def array_ops(x, y, op):

        # El error se muestra cuando
        # los valores introducidos no contengan decimales
        # o carácteres no númericos.
        for i in range(len(x)):
            if not((type(x[i]) == int) and (type(y[i]) == int)):
                return "E001"

        if not (type(op) == int):
            return "E001"

        # El siguiente error se retorna en caso
        # de que un operando sea mayor a 127 o bien menor a -127.
        for i in range(len(x)):
            if not((-127 <= x[i] <= 127) and (-127 <= y[i] <= 127)):
                return "E002"
        # El próximo error se muestra cuando
        # el selector se encuentre fuera del rango
        # definido para las operaciones [0-3].
        if not (0 <= op <= 3):
            return "E003"
        else:
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
