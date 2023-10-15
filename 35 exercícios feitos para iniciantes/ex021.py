# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load(' "arquivo de música mp3" ')
pygame.mixer.music.play()
pygame.event.wait()

'''  Deve-se criar uma pasta com o arquivo da música mp3 e digitar na line 5  '''
