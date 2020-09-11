# Se importa el .py que contiene los métodos
from tarea1 import operacion

# Para realizar las pruebas es necesario ingresar a
# consola e ingresar la dirección en la cual
# se tienen ambos archivos (tarea1.py y test_tarea1.py).
# Para ello se debe escribir desde cmd "cd 'ruta donde
# se encuentran los archivos' "
# Luego de esto basta con escribir 'pytest' y se
# correrá la prueba (gracias a que el archivo
# contiene test_ en su nombre). Si se quiere
# ver mpas información del proceso, agregar '-v' luego de pytest.

# Caso de exito basic_ops


# Suma
def test_basicops1():
    assert operacion.basic_ops(1, 3, 0) == 4


# Resta
def test_basicops2():
    assert operacion.basic_ops(1, 3, 1) == -2


# AND
def test_basicops3():
    assert operacion.basic_ops(1, 0, 2) == 0


# OR
def test_basicops4():
    assert operacion.basic_ops(1, 0, 3) == 1


# Caso de exito array_ops
# Suma
def test_arrayops1():
    assert operacion.array_ops([1, 2, 3], [1, 2, 3], 0) == [2, 4, 6]


# Resta
def test_arrayops2():
    assert operacion.array_ops([1, 5, 3], [1, 2, 4], 1) == [0, 3, -1]


# AND
def test_arrayops3():
    assert operacion.array_ops([0, 0, 1, 1], [0, 1, 0, 1], 2) == [0, 0, 0, 1]


# OR
def test_arrayops4():
    assert operacion.array_ops([0, 0, 1, 1], [0, 1, 0, 1], 3) == [0, 1, 1, 1]

# Para errores #

# Los errores aparecerán según el orden en el que fueron planteados
# Para probar cada uno llamar a la funcion correspondiente


# Error 1 (caracter no numérico o decimal)
# basic_ops
def test_errorbasicops1():
    assert operacion.basic_ops(1, 3.5, 0) == "E001"


# array_ops
def test_errorarrayops1():
    assert operacion.array_ops([1, 2, 5], ["t", 2, 3], 0) == "E001"


# Error 2 (Mayor a 127 o menor a -127)
# basic_ops
def test_errorbasicops2():
    assert operacion.basic_ops(1, 128, 0) == "E002"
# array_ops


def test_errorarrayops2():
    assert operacion.array_ops([1, 2, 5], [-129, 2, 3], 0) == "E002"


# Error 3 (Operación inválida, no existe selector)
# basic_ops
def test_errorbasicops3():
    assert operacion.basic_ops(1, 12, 8) == "E003"


# array_ops
def test_errorarrayops3():
    assert operacion.array_ops([1, 2, 5], [9, 2, 3], 5) == "E003"
