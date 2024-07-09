import streamlit as st
import jellyfish
import pandas as pd
from processing import (
    calcular_puntuacion,
    encontrar_mejor_coincidencia,
    seleccionar_mejor_opcion,
    grabar
)
from rapidfuzz import fuzz 
from helpers import transformar_cadena

df = pd.read_csv('./Personas (3).csv')
df['puntuacion'] = df.apply(calcular_puntuacion, axis=1)
df = df[['ID', 'Nro. Documento', 'puntuacion', 'Nombre Completo']]

# print(encontrar_mejor_coincidencia(df, "QUISPE  TORRES WILBER", 2, 90))

print(encontrar_mejor_coincidencia(df, "VALDIVIA  HILARIO VLADIMIR", 1, 85))


# print(100 * jellyfish.jaro_winkler_similarity( "TORRES QUISPE WILDER ESTEBAN","TORRES QUISPE WILDER"))
# print(fuzz.partial_token_sort_ratio( "TORRES QUISPE WILDER ESTEBAN","TORRES WILDR QUISPE"))