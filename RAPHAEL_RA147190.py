import sys
from dataclasses import dataclass

@dataclass
class Time:
    nome: str
    vitorias: int
    pontos: int
    tot_gols: int
    aproveita_anfi: float
    gols_sofridos: int

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo(sys.argv[1])

    print(classifica_times(ordena_times(times_compostos(jogos)), jogos))
    print('O/s time/s com melhor aproveitamento jogando como anfitrião:\n',melhor_aproveitamento(times_compostos(jogos)))
    print('=-=-' * 10)
    print('O time com a defesa menos vazada foi:\n', defesa_menos_vazada(times_compostos(jogos))+' - '+str(gols_sofridos(defesa_menos_vazada(times_compostos(jogos)), jogos)) + ' gols sofridos')
    # TODO: solução da pergunta 1
def time_anfitriao(resultado: str) -> str:
    '''
    Dado uma string *resultado* de jogo entre dois times, retorna o nome do time 
    anfitrião (mais a esquerda).

    Exemplos: 

    >>> time_anfitriao('Sao-Paulo 2 Flamengo 1')
    'Sao-Paulo'
    '''
    ind_espaco = 0
    while resultado[ind_espaco] != ' ':
        ind_espaco = ind_espaco + 1
    return resultado[:ind_espaco]
def time_visitante(resultado: str) -> str:
    '''
    Dado uma string *resultado* de jogo entre dois times, retorna o nome do time
    visitante (mais a direita).

    Exemplos:

    >>> time_visitante('Sao-Paulo 2 Flamengo 1')
    'Flamengo'
    '''
    prim_espaco = 0
    while resultado[prim_espaco] != ' ':
        prim_espaco = prim_espaco + 1

    for c in range(0, len(resultado) - 1):
        if resultado[c] == ' ':
            ult_espaco = c
    return resultado[prim_espaco + 3:ult_espaco]

def gols_anfitriao(resultado: str) -> int:
    '''
    Identifica e retorna a pontuação do time anfitrião com base no *resultado* de um determinado jogo.

    Exemplos: 

    >>> gols_anfitriao('Flamengo 2 Palmeiras 1')
    2
    >>> gols_anfitriao('Palmeiras 0 Sao-Paulo 0')
    0
    >>> gols_anfitriao('Atletico-MG 1 Flamengo 2')
    1
    '''
    ind_espaco = 0
    while resultado[ind_espaco] != ' ':
        ind_espaco = ind_espaco + 1
    return int(resultado[ind_espaco + 1])
def gols_visitante(resultado: str) -> int:

    '''
    Identifica e retorna a pontuação do time visitante com base no *resultado* de um determinado jogo.

    Exemplos: 

    >>> gols_visitante('Flamengo 2 Palmeiras 1')
    1
    >>> gols_visitante('Palmeiras 0 Sao-Paulo 0')
    0
    >>> gols_visitante('Atletico-MG 1 Flamengo 2')
    2
    '''
    for c in range(0, len(resultado) - 1):
        if resultado[c] == ' ':
            ult_espaco = c
    return int(resultado[ult_espaco + 1])  

def vitoria(resultado: str) -> str:
    '''
    Retorna qual foi o time vencedor com base no *resultado* de uma partida.
    Retorna 'EMPATE' caso os gols do time anfitrião e do time visitante sejam iguais.
    Exemplos:

    >>> vitoria('Flamengo 2 Palmeiras 1')
    'Flamengo'
    >>> vitoria('Palmeiras 0 Sao-Paulo 0')
    'EMPATE'
    >>> vitoria('Sao-Paulo 1 Atletico-MG 2')
    'Atletico-MG'
    '''
    if gols_anfitriao(resultado) > gols_visitante(resultado):
        vitoria = time_anfitriao(resultado)
    elif gols_visitante(resultado) > gols_anfitriao(resultado):
        vitoria = time_visitante(resultado)
    else:
        vitoria = 'EMPATE'
    return vitoria

def conta_vitorias(time: str, jogos: list) -> int:              # FUNÇÃO RECURSIVA - PERGUNTA 1 #
    '''
    Recebe o nome de um *time* e *jogos* com o resultado de várias partidas, 
    e retorna o número de vitórias que *time* conquistou.

    Exemplos:

    >>> conta_vitorias('Flamengo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    2
    >>> conta_vitorias('Atletico-MG', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    1
    >>> conta_vitorias('Sao-Paulo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    0
    '''
    vitorias = 0
    if len(jogos) == 0:
        vitorias = 0
    else:      
        if vitoria(jogos[0]) == time:
            vitorias = 1 + conta_vitorias(time, jogos[1:])
        else:
            vitorias = 0 + conta_vitorias(time, jogos[1:])
    return vitorias

def saldo_gols(time: str, jogos: list) -> int:
    '''
    Determina o saldo de gols de determinado *time* a partir da diferença de quantos gols foram feitos por
    quantos gols foram sofridos. Basedo em uma lista de *jogos*.

    Exemplos:

    >>> saldo_gols('Flamengo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    2
    >>> saldo_gols('Sao-Paulo', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    -1
    >>> saldo_gols('Atletico-MG', ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    0
    '''
    gols = 0
    sofreu = 0
    for jogo in jogos:
        if jogo[:prim_espaco(jogo)] == time:
            gols = gols + int(jogo[prim_espaco(jogo) + 1])
        elif jogo[prim_espaco(jogo) + 3:ulti_espaco(jogo)] == time:
            gols = gols + int(jogo[ulti_espaco(jogo) + 1])
        if jogo[:prim_espaco(jogo)] == time:
            sofreu = sofreu + int(jogo[ulti_espaco(jogo) + 1])
        elif jogo[prim_espaco(jogo) + 3:ulti_espaco(jogo)] == time:
            sofreu = sofreu + int(jogo[prim_espaco(jogo) + 1])
    return gols - sofreu
def empate(time: str, jogo: str) -> bool:
    '''
    Determina se determinado *time* empatou em um *jogo*. Retorna True caso sim, e False caso contrário.

    >>> empate('Sao-Paulo', 'Sao-Paulo 1 Atletico-MG 2')
    False
    >>> empate('Sao-Paulo', 'Palmeiras 0 Sao-Paulo 0')
    True
    >>> empate('Palmeiras', 'Palmeiras 0 Sao-Paulo 0')
    True
    '''
    empate = False
    if gols_anfitriao(jogo) == gols_visitante(jogo):
        if time == time_anfitriao(jogo) or time == time_visitante(jogo):
            empate = True
    return empate

def calcula_pontos(time: str, jogos: list[str]) -> int:
    '''
    Calcula a quantidade de pontos que determinado *time* possui com base em suas vitórias e empates.

    Exemplos:

    >>> t1 = ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2']

    >>> calcula_pontos('Flamengo', t1)
    6
    '''
    pontos = conta_vitorias(time, jogos) * 3
    for jogo in jogos:
        if empate(time, jogo) == True:
            pontos = pontos + 1
    return pontos

def ulti_espaco(jogo: str) -> int:
    '''
    Identifica o índice do último espaço em branco de uma string *jogo*.

    Exemplos:

    >>> ulti_espaco('Sao-Paulo 1 Atletico-MG 2')
    23
    >>> ulti_espaco('Palmeiras 0 Sao-Paulo 0')
    21
    >>> ulti_espaco('Flamengo 2 Palmeiras 1')
    20
    '''
    idx = 0
    for c in range(0, len(jogo)): 
        if jogo[c] == ' ':
            idx = c
    return idx

def prim_espaco(jogo: str) -> int:
    '''
    Identifica o índice do primeiro espaço em branco de uma string *jogo*.

    Exemplo: 

    >>> prim_espaco('Sao-Paulo 1 Atletico-MG 2')
    9
    >>> prim_espaco('Flamengo 2 Palmeiras 1')
    8
    >>> prim_espaco('Atletico-MG 1 Flamengo 2')
    11
    '''
    idx = 0
    while jogo[idx] != ' ':
        idx = idx + 1
    return idx

def times_compostos(jogos: list) -> list:
    '''
    Organiza todos os dados (nome, vitorias, pontos, saldo de gols) dos times da lista *jogos* em um tipo composto e os coloca em uma lista.
    Remove os excedentes de times repetidos se houver.

    Exemplos:

    >>> times_compostos(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    [Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)]
    '''
    aux = []
    times: list[Time] = []
    for j in range(0, len(jogos)):
         aux.append(Time(time_anfitriao(jogos[j]), conta_vitorias(time_anfitriao(jogos[j]), jogos), calcula_pontos(time_anfitriao(jogos[j]), jogos), saldo_gols(time_anfitriao(jogos[j]), jogos), aproveitamento_anfitriao(time_anfitriao(jogos[j]),jogos), gols_sofridos(time_anfitriao(jogos[j]), jogos)))
    for time in aux:
        if acha_x(times, time.nome) == False:
            times.append(time)
    return times

def maior_nome(jogos: list[str]) -> str:        # REFAZER ESSA FUNÇÃO PASSANDO A LISTA COMPOSTA (TIME) COMO PARAMETRO #
    '''
    Identifica e retorna o time com maior quantidade de caracteres.

    Exemplos: 

    >>> maior_nome(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'])
    'Atletico-MG'
    '''
    maior = len(time_anfitriao(jogos[0]))
    nome = time_anfitriao(jogos[0])
    for j in range(0, len(jogos)):
        if len(time_anfitriao(jogos[j])) > maior:
            maior = len(time_anfitriao(jogos[j]))
            nome = time_anfitriao(jogos[j])
    return nome        

def classifica_times(dados: list[Time], jogos: list[str]) -> str:
    '''
    Classifica os times em uma tabela com base em seus *dados* e outros critérios de classificação.
    
    Exemplos:

    >>> t1 = [Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0), Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1)]
    >>> t2 = ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2']

    >>> classifica_times(t1, t2)
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    TIME         P  V  S
    Flamengo     6  2  2
    Atletico-MG  3  1  0
    Sao-Paulo    1  0  -1
    Palmeiras    1  0  -1
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    '''
    espaco = len(maior_nome(jogos)) - 4
    print('=-=-' * 10)
    print('TIME' + ' ' * espaco ,'', 'P'+'  ''V'+'  ''S')
    for time in dados:
        if len(str(time.pontos)) == 2:
            espaco_pontos = 1
        else:
            espaco_pontos = 2
        if len(str(time.vitorias)) == 2:
            espaco_vitorias = 1
        else:
            espaco_vitorias = 2
        print(time.nome + ' ' *(len(maior_nome(jogos)) - len(time.nome)),'', str(time.pontos) + ' '* (espaco_pontos)+str(time.vitorias)+' '* (espaco_vitorias)+str(time.tot_gols))
    return '=-=-' * 10

def ordena_times(dados: list[Time]) -> list[Time]:
    '''
	Ordena a lista de tipo composto *dados* dos times em ordem decrescente, do time que mais pontuou ao time que menos pontou.
    Se dois ou mais times têm o mesmo número de pontos, então, os seguintes critérios são utilizados para o desempate: número de *vitorias*, *tot_gols*
	
	Exemplos:
	
	>>> t1 = [Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)]
				
	>>> ordena_times(t1)
	[Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3), Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2)]
    '''
    houve_troca = True
    aux = dados[0]
    while houve_troca == True:
        houve_troca = False
        for i in range(len(dados) - 1):
            if dados[i].pontos < dados[i + 1].pontos:
                aux = dados[i]
                dados[i] = dados[i + 1]
                dados[i + 1] = aux
                houve_troca = True
            elif dados[i].pontos == dados[i + 1].pontos:
                if dados[i].vitorias < dados[i + 1].vitorias:
                    aux = dados[i]
                    dados[i] = dados[i + 1]
                    dados[i + 1] = aux
                    houve_troca = True
                elif dados[i].vitorias == dados[i + 1].vitorias:
                    if dados[i].tot_gols < dados[i + 1].tot_gols:
                        aux = dados[i]
                        dados[i] = dados[i + 1]
                        dados[i + 1] = aux
                        houve_troca = True       
    return dados

def acha_x(times: list[Time], string: str) -> bool:
    '''
    Identifica se uma *string* existe em *lista*. Retorna True caso exista
    e False caso não exista.

    Exemplos:

    >>> acha_x([], 'Atletico-PR')
    False
    >>> acha_x([Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)], 'Atletico-MG')
    True
    >>> acha_x([Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Botafogo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)], 'Flamengo')
    False
    >>> acha_x([Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)], 'Palmeiras')
    True
    '''
    encontrou = False
    for time in times:
        if time.nome == string:
            encontrou = True
    return encontrou
    # TODO: solução da pergunta 1

    # TODO: solução da pergunta 2
def conta_partidas_anfitriao(time: str, jogos: list) -> int:        # FUNÇÃO RECURSIVA #
    '''
     Conta quantas vezes determinado *time* jogou como anfitrião, baseado em uma lista de *jogos*.

    Exemplos:
    >>> t1 = ['Atletico-PR 2 Coritiba 1', 'Londrina 1 Parana-Clube 1', 'Atletico-PR 1 Londrina 0', 'Coritiba 3 Parana-Clube 0',
    ... 'Atletico-PR 2 Parana-Clube 2', 'Coritiba 1 Londrina 1', 'Coritiba 1 Atletico-PR 0', 'Parana-Clube 0 Londrina 1',
    ... 'Londrina 2 Atletico-PR 2', 'Parana-Clube 1 Coritiba 2', 'Parana-Clube 0 Atletico-PR 3', 'Londrina 1 Coritiba 1']

    >>> conta_partidas_anfitriao('Atletico-PR', t1)
    3
    >>> conta_partidas_anfitriao('Londrina', t1)
    3
    >>> conta_partidas_anfitriao('Flamengo', t1)
    0
    '''
    cont = 0
    if len(jogos) == 0:
        cont = 0
    else:
        if jogos[0][:prim_espaco(jogos[0])] == time:
            cont = 1 + conta_partidas_anfitriao(time, jogos[1:])
        else:
            cont = 0 + conta_partidas_anfitriao(time, jogos[1:])
    return cont

def isola_partidas_anfitriao(time: str, jogos: list) -> list:
    '''
    Isola as partidas em que determinado *time* jogou como anfitrião e as coloca em uma lista.

    Exemplos:

    >>> t1 = ['Atletico-PR 2 Coritiba 1', 'Londrina 1 Parana-Clube 1', 'Atletico-PR 1 Londrina 0', 'Coritiba 3 Parana-Clube 0',
    ... 'Atletico-PR 2 Parana-Clube 2', 'Coritiba 1 Londrina 1', 'Coritiba 1 Atletico-PR 0', 'Parana-Clube 0 Londrina 1',
    ... 'Londrina 2 Atletico-PR 2', 'Parana-Clube 1 Coritiba 2', 'Parana-Clube 0 Atletico-PR 3', 'Londrina 1 Coritiba 1']

    >>> isola_partidas_anfitriao('Atletico-PR', t1)
    ['Atletico-PR 2 Coritiba 1', 'Atletico-PR 1 Londrina 0', 'Atletico-PR 2 Parana-Clube 2']
    >>> isola_partidas_anfitriao('Londrina', t1)
    ['Londrina 1 Parana-Clube 1', 'Londrina 2 Atletico-PR 2', 'Londrina 1 Coritiba 1']
    >>> isola_partidas_anfitriao('Parana-Clube', t1)
    ['Parana-Clube 0 Londrina 1', 'Parana-Clube 1 Coritiba 2', 'Parana-Clube 0 Atletico-PR 3']
    '''
    lst = []
    for jogo in jogos:
        if jogo[:prim_espaco(jogo)] == time:
            lst.append(jogo)
    return lst

def aproveitamento_anfitriao(time: str, jogos: list) -> float:
    '''
    Calcula o aproveitamento como anfitrião de determinado *time*.

    Exemplos:

    >>> t1 = ['Atletico-PR 2 Coritiba 1', 'Londrina 1 Parana-Clube 1', 'Atletico-PR 1 Londrina 0', 'Coritiba 3 Parana-Clube 0',
    ... 'Atletico-PR 2 Parana-Clube 2', 'Coritiba 1 Londrina 1', 'Coritiba 1 Atletico-PR 0', 'Parana-Clube 0 Londrina 1',
    ... 'Londrina 2 Atletico-PR 2', 'Parana-Clube 1 Coritiba 2', 'Parana-Clube 0 Atletico-PR 3', 'Londrina 1 Coritiba 1']

    >>> aproveitamento_anfitriao('Atletico-PR', t1)
    78
    >>> aproveitamento_anfitriao('Londrina', t1)
    33
    >>> aproveitamento_anfitriao('Parana-Clube', t1)
    0
    '''
    partidas_anfitriao = conta_partidas_anfitriao(time, jogos)
    pontos_possiveis = partidas_anfitriao * 3
    aproveitamento = calcula_pontos(time,isola_partidas_anfitriao(time, jogos)) / pontos_possiveis * 100
    return round(aproveitamento)

def acha_maior_aprov(times: list[Time]) -> int:
    '''
    Percorre a lista composta *times* e retorna o índice do time com maior aproveitamento como anfitrião.
    
    Exemplos:

    >>> t1 = [Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)]
    
    >>> t2 = [Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=3, aproveita_anfi=100, gols_sofridos=0), Time(nome='Palmeiras', vitorias=1, pontos=4, tot_gols=2, aproveita_anfi=33, gols_sofridos=2), Time(nome='Sao-Paulo', vitorias=0, pontos=0, tot_gols=-1, aproveita_anfi=0, gols_sofridos=1), Time(nome='Gremio', vitorias=0, pontos=0, tot_gols=-4, aproveita_anfi=0, gols_sofridos=5)]

    >>> acha_maior_aprov(t1)
    1
    >>> acha_maior_aprov(t2)
    0
    '''
    idx = 0
    maior = times[0].aproveita_anfi
    for t in range(len(times)):
        if times[t].aproveita_anfi > maior:
            maior = times[t].aproveita_anfi
            idx = t
    return idx

def melhor_aproveitamento(times: list[Time]) -> list:
    '''
    Identifica os *times* que tiveram o melhor aproveitamento jogando como anfitrião em jogos e os coloca em uma lista.

    Exemplo:

    >>> melhor_aproveitamento([Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=2), Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=100, gols_sofridos=2), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)])
    ['Flamengo 100%', 'Palmeiras 100%']
    '''
    maior = times[acha_maior_aprov(times)].aproveita_anfi
    nomes_maior = []
    for t in range(len(times)):
        if times[t].aproveita_anfi >= maior:
            maior = times[t].aproveita_anfi
            nomes_maior.append(times[t].nome+' '+str(times[t].aproveita_anfi)+'%')
    return nomes_maior
    # TODO: solução da pergunta 2
    
    # TODO: solução da pergunta 3
def gols_sofridos(time: str, jogos: list[str]) -> int:
    '''
    Identifica e retorna a quantidade de gols que *time* sofreu.

    Exemplos:

    >>> t1 = ['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1', 'Palmeiras 0 Sao-Paulo 0', 'Atletico-MG 1 Flamengo 2'] 
    >>> t2 = ['Flamengo 2 Gremio 0', 'Palmeiras 1 Corinthians 1', 'Sao-Paulo 0 Flamengo 1', 'Gremio 1 Palmeiras 3']
    >>> t3 = ['Atletico-PR 2 Coritiba 1', 'Londrina 1 Parana-Clube 1', 'Atletico-PR 1 Londrina 0', 'Coritiba 3 Parana-Clube 0',
    ... 'Atletico-PR 2 Parana-Clube 2', 'Coritiba 1 Londrina 1', 'Coritiba 1 Atletico-PR 0', 'Parana-Clube 0 Londrina 1',
    ... 'Londrina 2 Atletico-PR 2', 'Parana-Clube 1 Coritiba 2', 'Parana-Clube 0 Atletico-PR 3', 'Londrina 1 Coritiba 1']

    >>> gols_sofridos('Flamengo', t1)
    2
    >>> gols_sofridos('Sao-Paulo', t2)
    1
    >>> gols_sofridos('Coritiba', t3)
    5
    '''
    sofreu = 0
    for jogo in jogos:
        if jogo[:prim_espaco(jogo)] == time:
            sofreu = sofreu + int(jogo[ulti_espaco(jogo) + 1])
        elif jogo[prim_espaco(jogo) + 3:ulti_espaco(jogo)] == time:
            sofreu = sofreu + int(jogo[prim_espaco(jogo) + 1])
    return sofreu

def defesa_menos_vazada(times: list[Time]) -> str:
    '''
    Identifica e retorna o nome do time com menos gols sofridos da lista *times*.

    Exemplos:

    >>> t1 = [Time(nome='Sao-Paulo', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=0, gols_sofridos=2), Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=2, aproveita_anfi=100, gols_sofridos=4),
    ...  Time(nome='Palmeiras', vitorias=0, pontos=1, tot_gols=-1, aproveita_anfi=33, gols_sofridos=5), Time(nome='Atletico-MG', vitorias=1, pontos=3, tot_gols=0, aproveita_anfi=0, gols_sofridos=3)]
    
    >>> t2 = [Time(nome='Flamengo', vitorias=2, pontos=6, tot_gols=3, aproveita_anfi=100, gols_sofridos=0), Time(nome='Palmeiras', vitorias=1, pontos=4, tot_gols=2, aproveita_anfi=33, gols_sofridos=2),
    ...  Time(nome='Sao-Paulo', vitorias=0, pontos=0, tot_gols=-1, aproveita_anfi=0, gols_sofridos=1), Time(nome='Gremio', vitorias=0, pontos=0, tot_gols=-4, aproveita_anfi=0, gols_sofridos=5)]
    
    >>> defesa_menos_vazada(t1)
    'Sao-Paulo'
    >>> defesa_menos_vazada(t2)
    'Flamengo'
    '''
    menor = times[0].gols_sofridos
    nome = times[0].nome
    for t in range(len(times)):
        if times[t].gols_sofridos < menor:
            menor = times[t].gols_sofridos
            nome = times[t].nome
    return nome
    # TODO: solução da pergunta 3

def le_arquivo(nome: str) -> list[str]:

    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento     
    representa uma linha.

    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2 
    Flamengo 2 Palmeiras 1 

    a resposta produzida é
    [‘Sao-Paulo 1 Atletico-MG 2’, ‘Flamengo 2 Palmeiras 1’]
    '''
    try:
        with open(nome) as f:
            return f.readlines()
           
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)
if __name__ == '__main__':
    main()
