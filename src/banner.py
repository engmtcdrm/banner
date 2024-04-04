import math

from colorama import Fore, just_fix_windows_console

just_fix_windows_console()

class Banner:
    """
    A class to create a banner for a command line application.

    :app_nm: The name of the application.
    :flavor_text: (optional) A short description of the application.
    :version: (optional) The version of the application.
    :repo_url: (optional) The URL to the repository for the application.
    :width: (optional) The width of the banner.
    :border_char: (optional) The character used to create the border.
    :border_color: (optional) The color of the border.
    :description: (optional) A long description of the application.
    """

    def __init__(
        self,
        app_nm: str,
        flavor_text: str = None,
        version: str = None,
        repo_url: str = None,
        width: int = 80,
        border_char: str = "#",
        border_color: str = "magenta",
        description: str = None
    ):
        self.app_nm = app_nm
        self.flavor_text = flavor_text
        self.version = version
        self.repo_url = repo_url
        self.width = width
        self.border_char = border_char
        self.border_color = border_color
        self.description = description

        self.empty_width = width - 2

    def _str_to_color(self) -> str:
        color_name = self.border_color.lower()

        color_map = {
            'black': Fore.BLACK,
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE
        }

        return color_map.get(color_name, '')

    def _border_char(self) -> str:
        return self._str_to_color() + self.border_char + Fore.RESET

    def _border_line(self):
        return self._str_to_color() + self.border_char * self.width + Fore.RESET + '\n'

    def _empty_line(self):
        return self._border_char() + ' ' * self.empty_width + self.border_char + Fore.RESET + '\n'

    def _side_widths(self, text: str):
        text_len = len(text)

        print('text_len:', text_len)

        left_width = int((self.width - text_len - 2) / 2)
        right_width = left_width

        print(left_width)

        if (self.width - text_len - 2) % 2:
            right_width += 1

        return (left_width, right_width)

    def _wrap_text_left(self, text: str) -> str:
        right_width = self.width - len(text) - 3
        right_pad = ' ' * right_width

        left_text = self._border_char() + ' ' + text + right_pad + self._border_char() + '\n'

        return left_text

    def _wrap_text_center(self, text: str) -> str:
        left_width, right_width = self._side_widths(text)
        left_pad = ' ' * left_width
        right_pad = ' ' * right_width

        return self._border_char() + left_pad + text + right_pad + self._border_char() + '\n'

    def _wrap_text_right(self, text: str) -> str:
        left_width = self.width - len(text) - 3
        left_pad = ' ' * left_width

        right_text = self._border_char() + left_pad + text + ' ' + self._border_char() + '\n'

        return right_text

    def _text_line(self, text: str, align: str = 'center'):

        pad_width = self.width - 4

        chunks = math.ceil(len(text) / pad_width)

        text_line = ''

        if align == 'center':
            method = self._wrap_text_center
        elif align == 'right':
            method = self._wrap_text_right
        else:
            method = self._wrap_text_left

        for x in range(chunks):
            if x == 0:
                text_line += method(text[0:pad_width])
            elif x == chunks - 1:
                text_line += method(text[pad_width * x:])
            else:
                text_line += method(text[pad_width * x:pad_width * (x + 1)])

        return text_line

    @property
    def width(self) -> int:
        """
        The width of the banner.
        """
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width
        self.empty_width = width - 2

    def build(self) -> str:
        """
        Build the banner text.
        """
        banner_text = self._border_line()
        banner_text += self._empty_line()
        banner_text += self._text_line(self.app_nm)

        if self.flavor_text:
            banner_text += self._text_line(self.flavor_text)

        if self.repo_url:
            banner_text += self._empty_line()
            banner_text += self._text_line(self.repo_url)

        if self.version:
            banner_text += self._empty_line()
            banner_text += self._text_line('version ' + self.version)

        if self.description:
            banner_text += self._empty_line()
            banner_text += self._text_line(self.description, align="left")

        banner_text += self._empty_line()
        banner_text += self._border_line()

        return banner_text

    def __str__(self):
        return self.build()
