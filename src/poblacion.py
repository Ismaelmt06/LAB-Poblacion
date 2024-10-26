from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')


def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero, encoding = 'UTF-8') as f:
        lector = csv.reader(f)
        registro_poblacion = []
        for pais, codigo, año, censo in lector:
            t_pais = pais
            t_codigo = codigo 
            t_año = int(año)
            t_censo = int(censo)
            tupla = RegistroPoblacion(t_pais, t_codigo, t_año, t_censo)
            registro_poblacion.append(tupla)
    return registro_poblacion
    
def calcula_paises(poblaciones):
    '''_summary_

    :param poblaciones: _description_
    :type poblaciones: list[tuple(str, str, int, int)]
    :return: _description_
    :rtype: _type_
    '''
    paises = set()
    for t_poblaciones in poblaciones:
        paises.add(t_poblaciones.pais)
    return sorted(paises)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    filtro = []
    for t_poblaciones in poblaciones:
        if t_poblaciones.pais == nombre_o_codigo or t_poblaciones.codigo == nombre_o_codigo:
            filtro.append((t_poblaciones.año, t_poblaciones.censo))
    return  filtro

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    filtro = []
    for t_poblaciones in poblaciones:
        if t_poblaciones.año == anyo and t_poblaciones.pais == paises:
            filtro.append((t_poblaciones.pais, t_poblaciones.censo))
    return filtro

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años = []
    lista_habitantes=[]
    for t_poblaciones in poblaciones:
        if t_poblaciones.pais == nombre_o_codigo or t_poblaciones.codigo == nombre_o_codigo:
            lista_años.append(t_poblaciones.año)
            lista_habitantes.append(t_poblaciones.censo)
    plt.title(f"Evolucion de la poblacion de {nombre_o_codigo}")
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, año, pais):
    lista_años = []
    lista_habitantes=[]
    for t_poblaciones in poblaciones:
        if t_poblaciones.pais in pais and t_poblaciones.codigo == año:
            lista_años.append(t_poblaciones.año)
            lista_habitantes.append(t_poblaciones.censo)
    plt.title(f"Evolucion de la poblacion de {pais}")
    plt.bar(lista_años, lista_habitantes)
    plt.show()