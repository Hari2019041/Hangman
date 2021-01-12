import pygame
import random

pygame.init()

# GLOBAL VARIABLES
WIDTH = 600
HEIGHT = 600
MARGIN = 30
TITLE = "Hangman"
ICON = pygame.image.load("icon.png")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# READING WORDS FROM DICTIONARY.TXT
words = []
with open("dictionary.txt", "r") as file:
    for word in file.readlines():
        if len(word) >= 4:
            words.append(word)

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
    def __init__(self, name="Player"):
        self.name = name
        self.score = 0
        self.guessedLetters = []

    def chooseLetter(self, mouse_x, mouse_y):
        pass


class Game:
    def __init__(self, player, words):
        self.running = True
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.player = player
        self.words = words
        self.guesses = 0
        self.currentWord = ""
        self.lettersNotGuessed = [self.font.render(
            chr(i), True, BLACK, WHITE) for i in range(65, 91)]
        self.hangman = Hangman()

    def end(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def reset(self):
        pass

    def chooseWord(self):
        self.currentWord = random.choice(self.words)

    def showWord(self):
        pass

    def showLetters(self):
        x = MARGIN
        y = 420
        no = 1
        for letter_label in self.lettersNotGuessed:
            if x == 570:
                x = MARGIN
            if no > 10:
                y += 40
                no = 1
            screen.blit(letter_label, (x, y))
            x += 54
            no += 1
        pygame.display.update()

    def showScore(self):
        pass

    def mainScreen(self):
        pass

    def start(self):
        while self.running:
            screen.fill(WHITE)
            self.showLetters()
            self.end()


def main():
    setTitle(TITLE)
    setIcon(ICON)

    game = Game(Player(), words)
    game.start()


if __name__ == "__main__":
    main()
    player = Player()
    player.chooseLetter(2, 3)
