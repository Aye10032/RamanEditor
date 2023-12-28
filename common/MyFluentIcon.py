from enum import Enum

from qfluentwidgets import FluentIconBase, Theme, getIconColor

from loguru import logger


class LetterIcon(FluentIconBase, Enum):

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'

    def path(self, theme=Theme.AUTO):
        # logger.debug(getIconColor(theme))
        return f'resources/icon/{self.value}_{getIconColor(theme)}.svg'
