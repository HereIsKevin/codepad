from PySide6.QtWidgets import QApplication

from codepad.window import Window


class Application(QApplication):
    def __init__(self):
        super().__init__()

        self._windows = []

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
