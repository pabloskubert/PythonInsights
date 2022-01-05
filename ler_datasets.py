from multiprocessing import Pool
from typing import Final

PROCESSOS: Final = 40


# Ex: fn([1,2,3,4], 2) => [[1,2], [3,4]]
def dividir_em_sublistas(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def processar_csv(linhas_dt_csv: list):
  	pass # TODO
  
# Abre o dataset e lê todas as linhas 
dt_linhas = open('dataset_10gb.csv', mode='r').readlines()
  	
# Dividi as linhas do dataset em sublistas
dt_listas_proc = dividir_em_sublistas(dt_linhas, PROCESSOS)

# Para cada sublista executa um novo processo à parte (!= THREAD)
with Pool(PROCESSOS) as p:
  	p.map(processar_csv, dt_listas_proc)