import pygame


class ChessPiece:
    def __init__(self, image, color, piece, value):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.color = color
        self.piece = piece
        self.value = value
