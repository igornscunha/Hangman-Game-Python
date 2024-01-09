import selection

class Game:

    def __init__(self):
        self.selecao = selection.Selection()
        self.tentativas = ''
        self.erro = 0

    def campo(self):
        #os.system('clear')
        print("<<<<<<<<<<<<<<<<<<<< Jogo da Forca >>>>>>>>>>>>>>>>>>>\n")
        print(self.selecao.forca[self.erro], '\n')
        print('Tentativas: ', self.tentativas)

        conteudo = ''
        for item in self.selecao.palavraSecreta:
            conteudo += item
        print('Palavra: ', conteudo)

    def start(self):

        self.selecao.selecionaPalavra()
        while self.selecao.palavraSecreta != self.selecao.palavra:

            count = 0
            self.campo()
            jogada = input("Digite uma letra: ")

            if jogada in self.selecao.palavra:
                for word in self.selecao.palavra:
                    if jogada == word: self.selecao.palavraSecreta[count] = jogada
                    count += 1
            else:
                self.tentativas += jogada
                self.erro += 1

            if self.erro == 6:
                self.campo()
                finalizou = ''
                for item in self.selecao.palavra:
                    finalizou += item
                print(f"Palavra: {finalizou}\n","Você perdeu!!!\n")
                break
            if self.selecao.palavraSecreta == self.selecao.palavra:
                self.campo()
                print("Meus parabéns!!! Agora jogue de novo.")
                break