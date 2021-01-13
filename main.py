import pygame
import random

pygame.init()

# GLOBAL VARIABLES
WIDTH = 600
HEIGHT = 650
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
        if len(word) >= 6 and len(word) <= 11:
            words.append(word[0:-1].upper())

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def setTitle(TITLE):
    pygame.display.set_caption(TITLE)


def setIcon(ICON):
    pygame.display.set_icon(ICON)


class Hangman:
    def __init__(self):
        self.stage = 5
        self.gullotine = [(MARGIN, 350, 150, 5),
                          (MARGIN+73, 350-300, 5, 300),
                          (MARGIN+73, 350-300, 120, 5),
                          (MARGIN+193, 350-300, 5, 50)
                          ]
        self.head = [(MARGIN+193, 130), 30]
        self.body = (MARGIN+193, 160, 5, 80)
        self.hands = (MARGIN+160, 200, 71, 5)
        self.rightLeg = ((MARGIN+193, 240),
                         (MARGIN+193+5, 240),
                         (MARGIN+160+5, 300),
                         (MARGIN+160, 300))
        self.leftLeg = ((MARGIN+193, 240),
                        (MARGIN+193+5, 240),
                        (MARGIN+226+5, 300),
                        (MARGIN+226, 300))

    def drawStage(self):
        if self.stage == 1:
            self.drawGullotine()
        elif self.stage == 2:
            self.drawHead()
        elif self.stage == 3:
            self.drawBody()
        elif self.stage == 4:
            self.drawLegs()
        elif self.stage == 5:
            self.drawHands()
        pygame.display.update()

    def drawGullotine(self):
        for part in self.gullotine:
            pygame.draw.rect(screen, BLACK, part)

    def drawHead(self):
        self.drawGullotine()
        pygame.draw.circle(screen, BLACK, self.head[0], self.head[1], 5)

    def drawBody(self):
        self.drawHead()
        pygame.draw.rect(screen, BLACK, self.body)

    def drawLegs(self):
        self.drawBody()
        pygame.draw.polygon(screen, BLACK, self.rightLeg)
        pygame.draw.polygon(screen, BLACK, self.leftLeg)

    def drawHands(self):
        self.drawLegs()
        pygame.draw.rect(screen, BLACK, self.hands)


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
        self.wordFont = pygame.font.SysFont("Comic Sans MS", 25)
        self.player = player
        self.words = words
        self.guesses = 0
        self.maxGuesses = 5
        self.currentWord = ""
        self.letters = []
        self.lettersnotGuessed = [self.font.render(
            chr(i), True, BLACK, WHITE) for i in range(65, 91)]
        self.hangman = Hangman()

    def end(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def reset(self):
        self.chooseWord()

    def chooseWord(self):
        self.currentWord = random.choice(self.words)
        for letter in self.currentWord:
            if letter not in self.letters:
                self.letters.append(letter)

    def showWord(self):
        x = 75 + 45*((10-len(self.currentWord))//2)
        y = 400
        for letter in self.currentWord:
            if letter in self.letters:
                label = self.wordFont.render(
                    "__ ", True, BLACK, WHITE)
            else:
                label = self.wordFont.render(letter, True, BLACK, WHITE)
            screen.blit(label, (x, y))
            x += 45
        pygame.display.update()

    def showLetters(self):
        x = MARGIN
        y = 475
        no = 1
        for letter_label in self.lettersnotGuessed:
            if x == 570:
                x = MARGIN
            if no > 10:
                y += 40
                no = 1
            screen.blit(letter_label, (x, y))
            x += 54
            no += 1
        pygame.display.update()

    def showBorder(self):
        pygame.draw.line(screen, BLACK, (0, 10), (WIDTH, 10))
        pygame.draw.line(screen, BLACK, (0, HEIGHT-30), (WIDTH, HEIGHT-30))
        pygame.draw.line(screen, BLACK, (0, 10), (WIDTH, 10))
        pygame.draw.line(screen, BLACK, (0, 10), (WIDTH, 10))

    def showScore(self):
        player.showScore()

    def showHangman(self):
        self.hangman.drawStage()

    def mainScreen(self):
        pass

    def start(self):
        self.chooseWord()
        while self.running:
            screen.fill(WHITE)
            self.showBorder()
            self.showLetters()
            self.showHangman()
            self.showWord()
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
