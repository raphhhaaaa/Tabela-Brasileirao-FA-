# Tabela do Brasileirão

Trabalho acadêmico desenvolvido para a disciplina **Fundamentos de Algoritmos**.  

O objetivo foi implementar, em Python, um programa que **lê resultados de jogos de futebol armazenados em arquivos `.txt`**, processa esses dados e **gera uma tabela formatada** com base nos critérios de pontuação adotados no Campeonato Brasileiro.

---

## 📌 Funcionalidades

- Leitura de resultados de partidas a partir de arquivos de texto.
- Identificação de:
  - Time vencedor ou empate.
  - Gols marcados e sofridos por cada equipe.
  - Pontuação acumulada de cada time (3 pontos por vitória, 1 por empate).
  - Saldo de gols.
  - Aproveitamento dos times como mandantes.
  - Defesa menos vazada do campeonato.
- Exibição de uma **tabela classificatória** com critérios de desempate:
  1. Pontos
  2. Número de vitórias
  3. Saldo de gols
  4. Se necessário, ordem alfabética

---

## 📂 Estrutura do Projeto
├── main.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Código principal do trabalho

├── jogos_exemplo.txt &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Arquivo de entrada com resultados (exemplo)

├── README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Documentação

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Salve os resultados das partidas em um arquivo `.txt`, por exemplo: 
**`jogos_exemplo.txt`:**
Sao-Paulo 1 Atletico-MG 2
Flamengo 2 Palmeiras 1
Palmeiras 0 Sao-Paulo 0
Atletico-MG 1 Flamengo 2

ou alternativamente, use o arquivo `jogos_exemplo.txt` fornecido.

3. Clone este reposítorio e execute o programa no terminal:
```bash
git clone https://github.com/raphhhaaaa/Tabela-Brasileirao-FA-.git
```
```bash
cd Tabela-Brasileirao-FA-
```
```bash
python RAPHAEL_RA147190.py jogos_exemplo.txt
```

---

## 🛠️ Tecnologias/Métodos Utilizados

- Python 3

- Dataclasses para representar os times e suas estatísticas.

- Manipulação de arquivos texto.

- Estruturas condicionais, laços e funções recursivas.

---

## 👤 Autor

**Raphael Henrique**

RA: 147190

**Disciplina**: Fundamentos de Algoritmos

**Instituição**: Universidade Estadual de Maringá
