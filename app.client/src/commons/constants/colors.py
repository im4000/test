
from colorama import (
    Fore, Back, init as colorama_init
)


class Color:
    colorama_init(autoreset = True)

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"