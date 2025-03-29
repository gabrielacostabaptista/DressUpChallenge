#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Game:
    def __init__(self, window, palavra_secreta):
        self.window = window
        self.palavra_secreta = palavra_secreta.upper()  # Armazena a palavra convertida para maiúscula
        self.erros = 0
        self.letras_corretas = []
        self.letras_erradas = []

    def run(self):
        """Loop principal do jogo"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Aqui virá toda a lógica do jogo da forca
            self.window.fill((255, 255, 255))  # Fundo branco

            pygame.display.flip()  # Atualiza a tela

    def adicionar_palavra(self, palavra):
        pass
