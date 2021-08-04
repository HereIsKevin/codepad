import platform
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from codepad.window import Window


class Application(QApplication):
    _icon = str(Path(__file__).parent.parent / "resources" / "codepad.png")

    def __init__(self):
        super().__init__()

        self._windows = []

        if platform.system() == "Darwin":
            self.setQuitOnLastWindowClosed(False)

        self.setWindowIcon(QIcon(Application._icon))

    def new(self):
        window = Window(self)
        window.show()

        self._windows.append(window)

    def open(self, file):
        window = Window(self)
        window.load(file)
        window.show()

        self._windows.append(window)

    def close(self, window):
        self._windows.remove(window)
