"""Padeiro pobre precisa de ajuda para começar a ganhar dinheiro.
Ele precisa conseguir uma grana para comprar massas para produzir pão.
Com o dinheiro da compra da massa ele pode ir à padaria, fazer e vender pães.
Ele poderá pedir esmola na rua.
Pode pedir esmola para a mãe.
"""
from random import uniform, randint


class Padeiro:
    def __init__(self, nome, idade, dinheiro):
        self.nome = nome
        self.idade = idade
        self.dinheiro = float(dinheiro)
        self.massa = float(15)
        self.exp = 1.0

    def trabalhar(self):
        x = 0
        fabricar = int(input('\tQuantos pães deseja produzir?\n\t'))   # precisa fazer validação
        if fabricar > self.massa:
            print('\tVocê não tem massa suficiente para essa quantidade.')
        else:
            while x < fabricar:
                p = uniform(0.5, 1) * self.exp
                print('\t\tPão fabricado, vendido por R$ {:.2f}.'.format(p))
                self.dinheiro += p
                x += 1
                aprend = randint(1,15)
                if aprend == 5:
                    self.exp += aprend / 25
        self.menu()

    # def imprimir(self):
    #     print('O nome do padeiro é {}, ele tem {} anos de idade e começou com {} reais.'.format(self.nome,self.idade,self.dinheiro))

    def imprimir_din(self):
        print('{} está com R$ {:.2f}.'.format(self.nome, self.dinheiro))
        self.menu()

    def visita_mae(self):
        print('\n\tQue bom que veio me ver. É sempre muito gratificante receber um filho em casa.')
        print('\tPosso te ajudar dando dicas de padaria.')
        self.dinheiro -= int(input('\tMas o que você tem a me oferecer?\n\t'))   # precisa fazer validação
        self.menu()

    def menu(self):
        print('\nSkill: {:.2f}%, R$ {:.2f}, massas: {}.'.format(self.exp, self.dinheiro, self.massa))
        print('\n\tVocê pode levar {} ao supermercado, ao trabalho, para pedir esmola e outros lugares.'
              .format(self.nome))
        print('\tAções:')
        esc = int(input('\t\t1 - Ir ao trabalho.'
                        '\n\t\t2 - Ir ao supermercado.'
                        '\n\t\t3 - Ir à casa da mãe.'
                        '\n\t\t4 - Pedir esmola.'
                        '\n\t\t5 - Pedir empréstimo.'
                        '\n\t\t6 - Sair.\n'))
        if esc == 1:
            self.trabalhar()


def home():
    print('Olá, nosso amigo garçom precisa de ajuda. Que bom que te encontramos.\n')
    print('Ele está desempregado e totalmente sem dinheiro, para isso, está contando com sua orientação.')
    input('Existem algumas coisas que ele pode fazer mas ele está totalmente desorientado e não sabe por onde começar.')


produtos = ['bolo', 'pão', 'broa', 'rosca', 'bolachinha']
valores = [5, 0.10, 0.5, 6, 1]
prod = dict(zip(produtos, valores))
padeiro = Padeiro('Jucinaldo', 32, 0)  # criando padeiro

home()
padeiro.menu()