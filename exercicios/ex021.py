'''Program that plays audio from the MP3 file'''
'''Programa que reproduz o audio de um arquivo MP3'''

import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music. play()
pygame.event.wait()