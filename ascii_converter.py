import cv2
import tkinter
from tkinter import filedialog
import pygame
import sys
import numba


@numba.njit
def rgb_to_num_of_char(r, g, b):
    brightness = 0.212671 * r + 0.71516 * g + 0.072169 * b
    return round((LEN_OF_CHARS_STRING - 1) * brightness / 255)


def to_ascii():
    rendered_chrs = [myfont.render(char, False, (255, 255, 255)) for char in STRING_OF_CHARS]
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
            text_surface = myfont.render(STRING_OF_CHARS[rgb_to_num_of_char(r, g, b)], False, (r, g, b))
            screen.blit(text_surface, (x * SIZE_OF_FONT, y * SIZE_OF_FONT))
            pygame.display.update()


STRING_OF_CHARS = ' .",:;!~+-xmo*#W&8@'
LEN_OF_CHARS_STRING = len(STRING_OF_CHARS)
SIZE_OF_FONT = 4

root = tkinter.Tk()
image = tkinter.filedialog.askopenfilename()
root.destroy()

img = cv2.imread(image, cv2.IMREAD_COLOR)
height, width, _ = img.shape
img = cv2.resize(img, dsize=(width // SIZE_OF_FONT, height // SIZE_OF_FONT))

mode = input('Please, type 1 for black and white mode and 2 for color mode\n')

pygame.init()
myfont = pygame.font.SysFont('Courier', SIZE_OF_FONT)
screen = pygame.display.set_mode((width, height))

if mode.lower() == '1':
    to_ascii()
elif mode.lower() == '2':
    to_color_ascii()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            three_d_array = pygame.surfarray.array3d(screen)
            output = cv2.transpose(three_d_array)
            output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
            cv2.imwrite('output.png', output)
