"""Padeiro pobre precisa de ajuda para começar a ganhar dinheiro.
Ele precisa conseguir uma grana para comprar massas para produzir pão.
Com o dinheiro da compra da massa ele pode ir à padaria, fazer e vender pães.
Ele poderá pedir esmola na rua.
Pode pedir esmola para a mãe.
"""
from random import uniform


class Padeiro:
    def __init__(self, nome, idade, dinheiro):
        self.nome = nome
        self.idade = idade
        self.dinheiro = float(dinheiro)
        self.massa = float(15)
        self.exp = 1.0

    def trabalhar(self):
        x = 0
        self.fabricar = int(input('\tQuantos pães deseja produzir?\n'))   # precisa fazer validação
        if self.fabricar > self.massa:
            print('\tVocê não tem massa suficiente para essa quantidade.')
        else:
            while x < self.fabricar:
                p = uniform(0.5, 1)
                print('\t\tPão fabricado, vendido por R$ {:.2f}.'.format(p))
                self.dinheiro += p
                x += 1

    # def imprimir(self):
    #     print('O nome do padeiro é {}, ele tem {} anos de idade e começou com {} reais.'.format(self.nome,self.idade,self.dinheiro))

    def imprimir_dinh(self):
        print('{} está com R$ {:.2f}.'.format(self.nome, self.dinheiro))

    def visita_mae(self):
        print('\tQue bom que veio me ver. É sempre muito gratificante receber um filho em casa.')
        print('\tPosso te ajudar dando dicas de padaria.')
        self.dinheiro -= input('\tMas o que você tem a me oferecer?')   # precisa fazer validação


def menu():
    print('\tAções:')
    print('\t\t'
          '1 - Ir ao trabalho.'
          '2 - Ir ao supermercado.')


def home():
    print('Olá, nosso amigo garçom precisa de ajuda. Que bom que te encontramos.\n')
    print('Ele está desempregado e totalmente sem dinheiro, para isso, está contando com sua orientação.')
    print('Existe algumas coisas que ele pode fazer mas ele está totalmente perdido e não sabe por onde começar.')


produtos = ['bolo', 'pão', 'broa', 'rosca', 'bolachinha']
valores = [5, 0.10, 0.5, 6, 1]
prod = dict(zip(produtos, valores))

home()
padeiro = Padeiro('Jucinaldo', 32, 10)  # criando padeiro
padeiro.trabalhar()
padeiro.visita_mae()
menu()