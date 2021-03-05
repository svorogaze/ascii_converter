import cv2
import tkinter
from tkinter import filedialog
import pygame
import sys
import numba


@numba.njit
def rgb_to_num_of_char(r, g, b):
    brightness = 0.212671 * r + 0.71516 * g + 0.072169 * b
    return round((len_of_string - 1) * brightness / 255)


def to_ascii():
    rendered_chrs = [myfont.render(char, False, (255, 255, 255)) for char in string_of_chars]
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            b, g, r = img[y][x]
            text_surface = rendered_chrs[rgb_to_num_of_char(r, g, b)]
            screen.blit(text_surface, (x * SIZE_OF_FONT, y * SIZE_OF_FONT))
            pygame.display.update()


def to_color_ascii():
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            b, g, r = img[y][x]
            text_surface = myfont.render(string_of_chars[rgb_to_num_of_char(r, g, b)], False, (r, g, b))
            screen.blit(text_surface, (x * SIZE_OF_FONT, y * SIZE_OF_FONT))
            pygame.display.update()


string_of_chars = ' .",:;!~+-xmo*#W&8@'
len_of_string = len(string_of_chars)
SIZE_OF_FONT = 7

root = tkinter.Tk()
image = tkinter.filedialog.askopenfilename()
root.destroy()

img = cv2.imread(image, cv2.IMREAD_COLOR)
height, width, _ = img.shape
img = cv2.resize(img, dsize=(width // SIZE_OF_FONT, height // SIZE_OF_FONT))

mode = input('black and white ascii or color ascii?\n')

pygame.init()
myfont = pygame.font.SysFont('Courier', SIZE_OF_FONT)
screen = pygame.display.set_mode((width, height))

if mode.lower() == 'black and white':
    to_ascii()
elif mode.lower() == 'color':
    to_color_ascii()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            three_d_array = pygame.surfarray.array3d(screen)
            output = cv2.transpose(three_d_array)
            output = cv2.cvtColor(output,cv2.COLOR_RGB2BGR)
            cv2.imwrite('output.png',output)
