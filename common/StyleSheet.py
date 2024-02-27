from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, qconfig

from Path import BASE_DIR


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    SCROLL = 'scroll_interface'
    NODE = 'node_editor_interface'

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f'{BASE_DIR}/resources/qss/{theme.value.lower()}/{self.value}.qss'
