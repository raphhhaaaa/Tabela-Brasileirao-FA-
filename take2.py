from dataclasses import dataclass
jogos = ['Sao-Paulo 1 Atletico-MG 2\n', 'Flamengo 2 Palmeiras 1\n', 'Palmeiras 0 Sao-Paulo 0\n', 'Atletico-MG 1 Flamengo 2\n']

@dataclass
class Time:
    nome: str
    saldo_gols: int

def time_anfitriao(resultado: str) -> str:
    '''
    Dado uma string *resultado* de jogo entre dois times, retorna o nome do time 
    anfitrião (mais a esquerda).

    Exeplos: 

    >>> time_anfitrião('Sao-Paulo 2 Flamengo 1')
    'Sao-Paulo'
    '''
    ind_espaco = 0
    while resultado[ind_espaco] != ' ':
        ind_espaco = ind_espaco + 1
    gols = int(resultado[ind_espaco + 1])
    nome = resultado[:ind_espaco]
    return Time(nome, gols)
print(time_anfitriao(jogos[0]))
def time_visitante(resultado: str) -> str:
    '''
    Dado uma string *resultado* de jogo entre dois times, retorna o nome do time
    visitante (mais a direita).

    Exemplos:

    >>> time_visitane('Sao-Paulo 2 Flamengo 1')
    'Flamengo'
    '''
    prim_espaco = 0
    while resultado[prim_espaco] != ' ':
        prim_espaco = prim_espaco + 1

    for c in range(0, len(resultado) - 1):
        if resultado[c] == ' ':
            ult_espaco = c
    return resultado[prim_espaco + 3:ult_espaco]