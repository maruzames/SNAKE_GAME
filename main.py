import pygame
import random

pygame.init()
pygame.display.set_caption("SNAKE GAME")
largura, altura = 600, 400
pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock

#cores RGB
preta = (0,0,0)
branca = (255,255,255)
vermelha = (255,0,0)
verde = (0,255,0)

#parâmetros SNAKE

Tamanho_quadrado = 10
velocidade_game = 15