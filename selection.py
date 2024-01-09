import random

class Selection():
    def __init__(self):
        self.lista = []
        self.palavra = ['Sabine']
        self.palavraSecreta = ['_']
        self.forca = [' +--------+ \n |        | \n          | \n          | \n          | \n          | \n^^^^^^^^^^T^\n',
                      ' +--------+ \n |        | \n o        | \n          | \n          | \n          | \n^^^^^^^^^^T^\n',
                      ' +--------+ \n |        | \n o        | \n |        | \n          | \n          | \n^^^^^^^^^^T^\n',
                      ' +--------+ \n |        | \n o        | \n/|        | \n          | \n          | \n^^^^^^^^^^T^\n',
                      ' +--------+ \n |        | \n o        | \n/|\       | \n          | \n          | \n^^^^^^^^^^T^\n',
                      ' +--------+ \n |        | \n o        | \n/|\       | \n/         | \n          | \n^^^^^^^^^^T^\n',
                      ' +--------+ \n |        | \n o        | \n/|\       | \n/ \       | \n          | \n^^^^^^^^^^T^\n']

    def get(self):
        return print(self.lista)

    def lerArquivo(self):
        with open('src/palavras.txt', 'r') as arquivo:
            return arquivo.read().split('\n')

    def selecionaPalavra(self):
        self.lista = self.lerArquivo()
        self.palavra = [p for p in random.choice(self.lista)]
        self.palavraEscondida()

    def palavraEscondida(self):
        self.palavraSecreta = ['_' for i in self.palavra]