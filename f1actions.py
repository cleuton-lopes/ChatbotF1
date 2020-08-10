import f1services
import logging
from collections import defaultdict

logger = logging.getLogger('f1actions')


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'pilotos':
        return_values = pesquisa_pilotos(parameters, return_var)
    elif action == 'equipes':
        return_values = pesquisa_equipes(parameters, return_var)
    elif action == 'classificacao':
        return_values = pesquisa_classificacao(parameters, return_var)
    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def pesquisa_pilotos(parameters, return_var):
    temporada = parameters['temporada']
    pesquisa = f1services.pesquisa_pilotos(temporada)
    pilotos = pesquisa['DriverTable']['Drivers']
    pilotos = sorted(pilotos, key=lambda k: k['givenName'])

    pilotos_str = '\n\n'
    if (int(pesquisa['total']) > 0):
        pilotos_str = 'Os seguintes pilotos participaram da temporada '
    else :
        pilotos_str = 'Não foram encontrados pilotos na temporada '

    pilotos_str += str(temporada) + ' de fórmula 1: \n'
    for piloto in pilotos:
        pilotos_str = pilotos_str + piloto['givenName'] + ' ' + piloto['familyName'] + ',\n'

    pilotos_str = pilotos_str[:-2]
    return {
        return_var: pilotos_str
    }

def pesquisa_equipes(parameters, return_var):
    temporada = parameters['temporada']
    pesquisa = f1services.pesquisa_equipes(temporada)

    equipes = pesquisa['ConstructorTable']['Constructors']
    equipes = sorted(equipes, key=lambda k: k['name'])

    equipes_str = '\n\n'
    if (int(pesquisa['total']) > 0):
        equipes_str = 'As seguintes equipes participaram da temporada '
    else:
        equipes_str = 'Não foram encontradas equipes na temporada '

    equipes_str += str(temporada) + ' de fórmula 1: \n'
    for equipe in equipes:
        equipes_str = equipes_str + equipe['name'] + ',\n'

    equipes_str = equipes_str[:-2]
    return {
        return_var: equipes_str
    }

def pesquisa_classificacao(parameters, return_var):
    temporada = parameters['temporada']
    pesquisa = f1services.pesquisa_classificacao(temporada)

    corridas = pesquisa['RaceTable']['Races']

    classificacao_str = '\n\n'
    if (int(pesquisa['total']) > 0):
        classificacao_str = 'Classificação da temporada '
    else:
        classificacao_str = 'Não foram corridas na temporada '

    classificacao_str += str(temporada) + ' de fórmula 1: \n'

    classificacao_pilotos = defaultdict(float)
    classificacao_pilotos[nome_piloto] += float(resultado['points'])
    for corrida in corridas:
        for resultado in corrida['Results']:
            piloto = resultado['Driver']
            nome_piloto = piloto['givenName'] + " " + piloto['familyName']
            classificacao_pilotos[nome_piloto] += float(resultado['points'])

    classificacao_pilotos = {k: v for k, v in sorted(classificacao_pilotos.items(), key=lambda item: item[1], reverse=True)}

    posicao = 1
    for nome_piloto in classificacao_pilotos.keys():
        pontos = str(classificacao_pilotos[nome_piloto])
        classificacao_str = classificacao_str + str(posicao) + 'º ' + nome_piloto + ', com ' + pontos + ' pontos'  + ',\n'
        posicao += 1

    classificacao_str = classificacao_str[:-2]
    return {
        return_var: classificacao_str
    }


