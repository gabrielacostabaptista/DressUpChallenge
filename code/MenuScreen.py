import pygame
from code.AddSecretWord import AddSecretWord
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_PINK, MENU_OPTION, COLOR_GREEN, COLOR_YELLOW, COLOR_WHITE

class Menu:
    def __init__(self, window):
        self.window = window
        # Adicionando a imagem ao menu
        self.surf = pygame.image.load('C:\\Users\\gabri\\OneDrive\\Documents\\DEV\\JogoDaForca\\asset\\BgMenu.png')
        # Redimensionando a imagem para ajustar na janela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        # Posicionando a imagem no canto superior esquerdo no retângulo
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def menu_text(self, text_size, text, text_color, text_center_pos):
        # Renderiza o texto na tela
        font = pygame.font.Font(None, text_size)  # Usando a fonte padrão do Pygame
        text_surface = font.render(text, True, text_color)  # Cria a superfície com o texto
        text_rect = text_surface.get_rect(center=text_center_pos)  # Posiciona o texto centralizado
        self.window.blit(text_surface, text_rect)  # Desenha o texto na janela

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('C:\\Users\\gabri\\OneDrive\\Documents\\DEV\\JogoDaForca\\asset\\SondMenu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(text_size=50, text="Dress-up", text_color=COLOR_PINK,
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    elif event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]  # Retorna a opção selecionada e sai do loop

            pygame.display.flip()

def main():
    # Função principal para inicializar o jogo
    pygame.init()  # Inicializa o Pygame

    # Cria a janela com as dimensões definidas
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # Define o título da janela
    pygame.display.set_caption("Dress Up Challenge - Menu")

    # Instancia o menu e executa
    menu = Menu(window)
    selected_option = menu.run()  # Chama o menu e captura a opção selecionada

    if selected_option == "NEW GAME":
        # Após o menu, instancia a tela de adicionar palavra
        add_secret_word_screen = AddSecretWord(window)
        secret_word = add_secret_word_screen.run()
        print(f"Palavra secreta capturada: {secret_word}")

    elif selected_option == "EXIT":
        pygame.quit()
        quit()

if __name__ == "__main__":
    main()  # Executa a função principal