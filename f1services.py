import requests
import configparser
import logging

base_url = 'http://ergast.com/api/f1/'

def pesquisa_pilotos(temporada):
    endpoint = base_url + str(temporada) + '/drivers.json';
    return requests.get(endpoint).json()['MRData']

def pesquisa_equipes(temporada):
    endpoint = base_url + str(temporada) + '/constructors.json';
    return requests.get(endpoint).json()['MRData']

def pesquisa_classificacao(temporada):
    endpoint = base_url + str(temporada) + '/results.json?limit=1000';
    return requests.get(endpoint).json()['MRData']

