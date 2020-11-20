import requests
import sys
import json 

URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name'

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisição em:', url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except Exception as error:
        print('Erro ao fazer persing')
        print(error)

def contagem_paises(todos_paises):
    resposta = requisicao(URL_ALL)
    if resposta:
        return len(todos_paises)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}:{} habitantes'.format(pais['name'], pais['population']))
    else:
        print('País não encontrado!')

def mostrar_moeda(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                moedas = pais['currencies']
                print('Moedas do', pais['name'])
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code'])) 
    else:
        print('País não encontrado!')


            


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('##Bem vindo sistema de busca de paises##')
        print('Uso: python pises.py <ações> <nome do pais>')
        print('Ações: contagem, moeda, populacao')

    else:
        argumento1 = sys.argv[1]
        pais = sys.argv[2]
        if argumento1 == "contagem":
            numero_paises = len(URL_ALL)
            print('existem {} paises no mundo!'.format(numero_paises))
        elif argumento1 == 'moeda':
            if pais:
                mostrar_moeda(pais)
        elif argumento1 == 'populacao':
            if pais:
                mostrar_populacao(pais)
        else:
            print('Argumentos invalidos!')

    


