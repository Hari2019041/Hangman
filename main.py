import pygame
import random

pygame.init()

# GLOBAL VARIABLES
WIDTH = 600
HEIGHT = 600
TITLE = "Hangman"
ICON = pygame.image.load("icon.png")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def setTitle(TITLE):
    pygame.display.set_caption(TITLE)


def setIcon(ICON):
    pygame.display.set_icon(ICON)


class Hangman:
    def __init__(self):
        pass

    def drawGullotine(self):
        pass

    def drawHead(self):
        pass

    def drawBody(self):
        pass

    def drawRightHand(self):
        pass

    def drawLeftHand(self):
        pass

    def drawRightLeg(self):
        pass

    def drawLeftLeg(self):
        pass


class Player:
    def __init__(self):
        pass

    def chooseLetter(self):
        pass


class Game:
    def __init__(self):
        pass

    def chooseWord(self):
        pass

    def showWord(self):
        pass

    def showLetters(self):
        pass

    def showScore(self):
        pass

    def mainScreen(self):
        pass

    def start(self):
        pass


def main():
    setTitle(TITLE)
    setIcon(ICON)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
