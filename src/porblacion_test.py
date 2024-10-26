from poblacion import *

def test_lee_poblaciones(ruta_fichero):
    print("Prueba de lee poblaciones")
    poblaciones = lee_poblaciones(ruta_fichero)
    print(poblaciones[:4])
    print(poblaciones[-4:])
    return poblaciones

def test_calcula_paises(poblaciones):
    print("Prueba de calcula paises")
    print(calcula_paises(poblaciones))

def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    print("Prueba de filtrar por pais")
    print(filtra_por_pais(poblaciones, nombre_o_codigo))

def test_filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    print("Prueba de filtrar por pais y año")
    print(filtra_por_paises_y_anyo(poblaciones, anyo, paises))

def test_muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    print("Prubea de muestra de la evolucion de la población")
    print(muestra_evolucion_poblacion(poblaciones, nombre_o_codigo))

def test_muestra_comparativa_paises_anyo(poblaciones, año, pais):
    print("Prueba de muestra de la comparativa de paises en un año determinado")
    print(muestra_comparativa_paises_anyo(poblaciones, año, pais))

if __name__ == "__main__":
    poblaciones = test_lee_poblaciones('data\population.csv')
    # test_calcula_paises(poblaciones)
    # test_filtra_por_pais(poblaciones, 'Central Europe and the Baltics')
    # test_filtra_por_paises_y_anyo(poblaciones, 2000, 'India')
    # test_muestra_evolucion_poblacion(poblaciones, "Spain")
    test_muestra_comparativa_paises_anyo(poblaciones, 1988, ("Bermuda", "Guam", "Kenya", "Spain", "Tonga"))