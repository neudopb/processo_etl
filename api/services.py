import requests
from pathlib import Path

class NumbersClass(object):

    def __init__(self, *args, **kw):
        pass

    def do_work(self):
        list_numbers = extract_numbers()
        
        list_numbers = transform_numbers(list_numbers)
        
        return list_numbers

# ************************* EXTRACT *************************

def extract_numbers():

    list_numbers = [] # Lista com todos os números
    page = 1 # Página da API

    while True: # Se mantem no loop enquanto a api não vinher vazia
        
        # if page % 100 == 0: # Imprimir a cada 500 paginas
        print('TAMANHO DA LISTA:', len(list_numbers))
        print('PAGINA:', page)
        
        request = requests.get('http://challenge.dienekes.com.br/api/numbers?page=' + str(page)) # Requisição na API
        
        if request.status_code == 200:

            if not request.json()['numbers']: # Se vinher vazia sai do while
                break

            list_numbers.extend(request.json()['numbers']) # Adiciona o resultado a lista com todos os valores
            page += 1

    return list_numbers

# ************************* TRANSFORM *************************

def transform_numbers(list_numbers):

    list_numbers = sort(list_numbers, 0, len(list_numbers)) # Chama a função de ondenação
    
    return list_numbers

def sort(list_numbers, inicio, fim):

    if inicio < fim-1: # Verifica se o inicio e o fim não são o mesmo elemento
        meio = (inicio + fim) // 2 # Encontrar o indice do meio

        sort(list_numbers, inicio, meio) # Chamar recursivamente a primeira metade da lista
        sort(list_numbers, meio, fim) # Chamar recursivamente a segunda metade da lista

        list_esquerda = list_numbers[inicio:meio]
        list_direita = list_numbers[meio:fim]
        pos_esq, pos_dir = 0, 0

        for i in range(inicio, fim):
            if pos_esq >= len(list_esquerda): # Verifica se ainda tem elementos na lista da esquerda
                list_numbers[i] = list_direita[pos_dir]
                pos_dir += 1
            elif pos_dir >= len(list_direita): # Verifica se ainda tem elementos na lista da direita
                list_numbers[i] = list_esquerda[pos_esq]
                pos_esq += 1
            elif list_esquerda[pos_esq] < list_direita[pos_dir]: # Verifica qual valor é menor
                list_numbers[i] = list_esquerda[pos_esq]
                pos_esq += 1
            else:
                list_numbers[i] = list_direita[pos_dir]
                pos_dir += 1

    return list_numbers