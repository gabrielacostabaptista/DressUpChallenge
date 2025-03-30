#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.AddSecretWord import AddSecretWord
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.MenuScreen import Menu


class Game:
    def __init__(self):
        pygame.init()

        #configurando a janela
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Meu jogo com menu")
        self.running = True

        #instancia o menu
        self.menu = Menu(self.window)

    def run (self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()  # Retorna a escolha feita no menu

            if menu_return == MENU_OPTION[0]:  # "NEW GAME"
                # Aqui, quando "New Game" é escolhido, o jogo vai para a tela de AddSecretWord
                level = AddSecretWord(self.window, name='AddSecretWord', menu_return=menu_return)
                level.run()  # Executa a tela AddSecretWord e depois vai para o jogo
            elif menu_return == MENU_OPTION[1]:  # "EXIT"
                pygame.quit()
                quit()
            else:
                pass



        #self.palavra_secreta = palavra_secreta.upper()  # Armazena a palavra convertida para maiúscula
        #self.erros = 0
        #self.letras_corretas = []
        #self.letras_erradas = []



            pygame.display.flip()  # Atualiza a tela

    #def adicionar_palavra(self, palavra):
        #pass
