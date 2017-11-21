import pygame
import time

class Winodw:

    def message_to_screen(msg, color):
        screen_text = font.render(msg, True, color)
        gameDisplay.blit(screen_text, [display_width/2, display_height/2])

    def main():
        pygame.init()

        white = (255,255,255)
        black = (0, 0, 0)
        red = (255, 0, 0)

        #variables:
        display_width = 800
        display_height = 600

        gameDisplay = pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption('Tytuł')

        block_size = 10
        FPS = 10

        clock = pygame.time.Clock()

        font = pygame.font.SysFont(None, 25)
        lead_x = display_width/2
        lead_y = display_height/2
        lead_x_change = 0
        lead_y_change = 0
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -block_size
                    if event.key == pygame.K_RIGHT:
                        lead_x_change = block_size
                    if event.key == pygame.K_DOWN:
                        lead_y_change = block_size
                    if event.key == pygame.K_UP:
                        lead_y_change = -block_size
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        lead_x_change = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        lead_y_change = 0
            #bounderies:
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameExit = True
            lead_x += lead_x_change
            lead_y += lead_y_change

            gameDisplay.fill(white)
            pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])

            gameDisplay.fill(red, rect=[200,200,50,50])
            pygame.display.update()

            clock.tick(FPS)
        message_to_screen("You lose", red)
        pygame.display.update()
        pygame.guit()
        sys.quit()
