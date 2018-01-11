"""Padeiro pobre precisa de ajuda para começar a ganhar dinheiro.
Ele precisa conseguir uma grana para comprar massas para produzir pão.
Com o dinheiro da compra da massa ele pode ir à padaria, fazer e vender pães.
Ele poderá pedir esmola na rua.
Pode pedir esmola para a mãe.
"""
from random import uniform
from random import randint


class Padeiro:
    def __init__(self, nome, idade, dinheiro):
        self.nome = nome
        self.idade = idade
        self.dinheiro = float(dinheiro)
        self.massa = int(0)
        self.exp = 1.0

    def trabalhar(self):
        x = 0
        fabricar = int(input('\tQuantos pães deseja produzir?\n\t'))   # precisa fazer validação
        if fabricar > self.massa:
            print('\tVocê não tem massa suficiente para essa quantidade.')
        elif fabricar == 0:
            print('\tIsso é falta de profissionalismo, quando vier ao trabalho, traga tudo que for necessário.')
        else:
            self.massa -= fabricar
            while x < fabricar:
                p = uniform(0.2, 0.6) * self.exp
                print('\t\tPão fabricado, vendido por R$ {:.2f}.'.format(p))
                self.dinheiro += p
                x += 1
                aprend = randint(1,15)
                if aprend == 5:
                    self.exp += aprend / 35
        self.menu()

    def superm(self):
        print('\tSeja bem-vindo ao Mercado de Massas.')
        compra = int(input('\tNos informe quantas massas deseja comprar: '))
        preco = compra * 10
        if self.dinheiro < preco:
            print('\nOps, você não tem dinheiro suficiente.\nCada uma custa R$ 10,00.')
        elif compra == 0:
            print('Volte sempre! Mas não me faça perder tempo!')
        else:
            self.massa += compra
            self.dinheiro -= preco
            print('Obrigado por sua compra, volte sempre!')
        self.menu()

    # def imprimir(self):
    #     print('O nome do padeiro é {}, ele tem {} anos de idade e começou com {} reais.'.format(self.nome,self.idade,self.dinheiro))

    def imprimir_din(self):
        print('{} está com R$ {:.2f}.'.format(self.nome, self.dinheiro))
        self.menu()

    def mae(self):
        print('\nQue bom que veio me ver. É sempre muito gratificante receber um filho em casa.')
        print('Posso te ajudar dando dicas de padaria. Caso eu tenha algumas moedas, posso te dar.')
        esmola = uniform(0.05, 0.5)
        aprend = randint(1, 11)

        if aprend == 10 and self.dinheiro > 5:
            assalto = uniform(0.6, 0.8)
            self.dinheiro = self.dinheiro * assalto
            print('Sua mãe está pobre! Tomou R$ {:.2f} de você!'.format(self.dinheiro * assalto))
        elif aprend == 5:
            aprendizado = (aprend / 55) * uniform(1, 1.4)
            self.dinheiro += esmola
            self.exp += aprendizado
            print('{} ganha R${:.2f}.'.format(self.nome, esmola))
            print ('E ganha {:.2f} de experiência.'.format(aprendizado))
        else:
            self.dinheiro += esmola
            print('{} ganha R${:.2f}.'.format(self.nome, esmola))
        self.menu()

    def esmola(self):
        esmola = uniform(0.1, 2.5)
        p_exp = uniform(0.2, 1)
        sorte = randint(1,11)
        if sorte == 10 and self.dinheiro > 5:
            assalto = uniform(0.5, 0.8)
            self.dinheiro = self.dinheiro * assalto
            print('Você foi assaltado! Levaram R$ {:.2f}.'.format(assalto))
        elif self.exp > 1:
            self.dinheiro += esmola
            self.exp -= p_exp
            print('\nMe sinto desmotivado ao fazer isso, vou acabar perdendo minhas habilidades.')
            print('{} passa o dia todo pedindo esmola e consegue R$ {:.2f} mas perde {:.2f} de experiência.'
                  .format(self.nome, esmola, p_exp))
        else:
            self.dinheiro += esmola
            print('\nMe sinto desmotivado ao fazer isso, muito triste minha situação')
            print('{} passa o dia todo pedindo esmola e consegue R$ {:.2f}.'.format(self.nome, esmola))
        self.menu()

    def menu(self):
        print('\nSkill: {:.2f}, R$ {:.2f}, massas: {}.'.format(self.exp, self.dinheiro, self.massa))
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
        elif esc == 2:
            self.superm()
        elif esc == 3:
            self.mae()
        elif esc == 4:
            self.esmola()


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
