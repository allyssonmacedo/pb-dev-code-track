#Faça um programa em python que abra e reproduza o áudio de arquivo mp3.
# 
#pip install pygame
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
