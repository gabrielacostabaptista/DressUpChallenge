#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.AddSecretWord import AddSecretWord
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_PINK, MENU_OPTION, COLOR_GREEN, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('C:\\Users\\gabri\\OneDrive\\Documents\\DEV\\JogoDaForca\\asset\\BgMenu.png')
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def menu_text(self, text_size, text, text_color, text_center_pos):
        font = pygame.font.Font(None, text_size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(text_surface, text_rect)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('C:\\Users\\gabri\\OneDrive\\Documents\\DEV\\JogoDaForca\\asset\\SondMenu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(text_size=50, text="Dress- Up", text_color=COLOR_PINK,
                           text_center_pos=(WIN_WIDTH / 2, 70))
            self.menu_text(text_size=50, text="Challenge", text_color=COLOR_PINK,
                           text_center_pos=(WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=27, text=MENU_OPTION[i], text_color=COLOR_YELLOW,
                                   text_center_pos=(WIN_WIDTH / 2, 170 + 30 * i))
                else:
                    self.menu_text(text_size=27, text=MENU_OPTION[i], text_color=COLOR_GREEN,
                                   text_center_pos=(WIN_WIDTH / 2, 170 + 30 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #encerrar o programa quando apeta o X
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]  # Retorna a opção selecionada
                    else:
                        pygame.quit()
                        quit()


            pygame.display.flip()

import pygame
from code.MenuScreen import Menu
from code.AddSecretWord import AddSecretWord
from code.Const import WIN_WIDTH, WIN_HEIGHT

def main():
    pygame.init()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Dress Up Challenge")

    menu = Menu(window)  # Instancia o menu
    add_secret_word = AddSecretWord(window)  # Instancia a tela de AddSecretWord

    while True:
        selected_option = menu.run()  # Executa o menu e captura a opção selecionada
        if selected_option == "NEW GAME":
            # Após o menu, instancia a tela de adicionar palavra
            add_secret_word = AddSecretWord(window)
            secret_word = add_secret_word.run()
        else:
            pygame.quit()
            quit()

if __name__ == "__main__":
    main()
