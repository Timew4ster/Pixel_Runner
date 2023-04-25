# resource_loader.py

import os

import pygame

current_directory = os.path.dirname(os.path.abspath(__file__))

def load_image(image_path):
    return pygame.image.load(os.path.join(current_directory, image_path))

def load_sound(sound_path):
    return pygame.mixer.Sound(os.path.join(current_directory, sound_path))

def load_font(font_path, size):
    return pygame.font.Font(os.path.join(current_directory, font_path), size)
