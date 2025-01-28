""" Crie uma função que retorne datas dentro de um texto. 
A função deve retornar uma lista com todas as datas encontradas no texto. 
Caso não haja nenhuma data, a função deve retornar uma lista vazia."""

import re

def find_date_string(text):
    date = re.findall(r'\d{2}/\d{2}/\d{4}', text)
    return date

    """ Crie uma função que retorne datas dentro de um texto. 
A função deve retornar uma lista com todas as datas encontradas no texto. As datas podem estar 
no formato dd/mm/aaaa ou dd-mm-aaaa. 
Caso não haja nenhuma data, a função deve retornar uma lista vazia."""

def find_date_string(text):
    date = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)
    return date

    """ Crie uma função que retorne datas dentro de um texto. 
A função deve retornar uma lista com todas as datas encontradas no texto. As datas podem estar 
no formato dd/mm/aaaa ou dd-mm-aaaa. Se houver datas repetidas, a função deve retornar apenas uma vez.
Caso não haja nenhuma data, a função deve retornar uma lista vazia."""

def find_date_string(text):
    date = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)
    return list(set(date))

""" Crie uma função que recebe uma lista de datas em formatos diferentes e retorne todas as datas
não repetidas. Caso não haja nenhuma data, a função deve retornar uma lista vazia."""

def find_date_string(dates):
    date = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', str(dates))

    " converta as datas para o formato dd/mm/aaaa"
    date = [d.replace('-', '/') for d in date]
    
    return list(set(date))