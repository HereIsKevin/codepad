from PySide6.QtGui import QAction, QFontDatabase, QKeySequence
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QTextEdit


class Window(QMainWindow):
    def __init__(self, application):
        super().__init__()

        self._file = None
        self._application = application

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPixelSize(14)

        self._text = QTextEdit()
        self._text.setFont(font)
        self._text.document().contentsChanged.connect(self._modified)

        file_menu = self.menuBar().addMenu(self.tr("&File"))
        file_menu.addAction(self.tr("&New"), self._new, QKeySequence.New)
        file_menu.addAction(self.tr("&Open..."), self._open, QKeySequence.Open)
        file_menu.addAction(self.tr("&Save"), self._save, QKeySequence.Save)
        file_menu.addAction(self.tr("Save &As..."), self._save_as, QKeySequence.SaveAs)
        file_menu.addSeparator()
        file_menu.addAction(self.tr("&Close"), self._close, QKeySequence.Close)

        edit_menu = self.menuBar().addMenu(self.tr("&Edit"))
        edit_menu.addAction(self.tr("&Undo"), self._text.undo, QKeySequence.Undo)
        edit_menu.addAction(self.tr("&Redo"), self._text.redo, QKeySequence.Redo)
        edit_menu.addSeparator()
        edit_menu.addAction(self.tr("Cu&t"), self._text.cut, QKeySequence.Cut)
        edit_menu.addAction(self.tr("&Copy"), self._text.copy, QKeySequence.Copy)
        edit_menu.addAction(self.tr("&Paste"), self._text.paste, QKeySequence.Paste)

        help_menu = self.menuBar().addMenu(self.tr("&Help"))
        help_menu.addAction(self.tr("Codepad &Help"), self._help)

        about = help_menu.addAction(self.tr("&About Codepad"), self._about)
        about.setMenuRole(QAction.AboutRole)

        self._current_file(None)

        self.setCentralWidget(self._text)

    def load(self, path):
        try:
            with open(path) as file:
                self._text.setPlainText(file.read())
        except EnvironmentError as error:
            QMessageBox.warning(
                self,
                self.tr("Codepad"),
                self.tr(f"Cannot read file at {path}:\n{error}"),
            )

            return

        self._current_file(path)

    def closeEvent(self, event):
        if self._text.document().isModified():
            result = QMessageBox.warning(
                self,
                self.tr("Codepad"),
                self.tr("Do you want to save the changes you made to this document?"),
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            )

            if result == QMessageBox.Save:
                if self._save():
                    event.accept()
                    self._application.close(self)
                else:
                    event.ignore()
            elif result == QMessageBox.Cancel:
                event.ignore()
            else:
                event.accept()
                self._application.close(self)

    def _modified(self):
        self.setWindowModified(self._text.document().isModified())

    def _new(self):
        self._application.new()

    def _open(self):
        file, _ = QFileDialog.getOpenFileName(self)

        if file != "":
            if self._file is None:
                self.load(file)
            else:
                self._application.open(file)

    def _save(self):
        if self._file is None:
            return self._save_as()
        else:
            return self._write(self._file)

    def _save_as(self):
        file, _ = QFileDialog.getSaveFileName(self)

        if file != "":
            return self._write(file)
        else:
            return False

    def _close(self):
        self.close()

    def _help(self):
        QMessageBox.information(
            self,
            self.tr("Codepad Help"),
            self.tr("Help is currently unavailable for Codepad."),
        )

    def _about(self):
        QMessageBox.about(
            self,
            self.tr("Codepad"),
            self.tr(
                '<a href="https://github.com/HereIsKevin/codepad">Codepad</a>,'
                + "the simple text editor built with Python and Qt. Copyright "
                + "© 2021 Kevin Feng.<br /><br />"
                + "This program is free software: you can redistribute it "
                + "and/or modify it under the terms of the GNU General Public "
                + "License as published by the Free Software Foundation, "
                + "either version 3 of the License, or (at your option) any "
                + "later version.<br /><br />"
                + "This program is distributed in the hope that it will be "
                + "useful, but WITHOUT ANY WARRANTY; without even the implied "
                + "warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR "
                + "PURPOSE. See the GNU General Public License for more "
                + "details.<br /><br />"
                + "You should have received a copy of the GNU General Public "
                + "License along with this program. If not, see "
                + '<a href="https://www.gnu.org/licenses/">'
                + "https://www.gnu.org/licenses/</a>."
            ),
        )

    def _write(self, path):
        try:
            with open(path, "w") as file:
                file.write(self._text.toPlainText())
        except EnvironmentError as error:
            QMessageBox.warning(
                self,
                self.tr("Codepad"),
                self.tr(f"Cannot write file at {path}:\n{error}"),
            )

            return False

        self._current_file(path)

        return True

    def _current_file(self, path):
        self._file = path

        self._text.document().setModified(False)
        self.setWindowModified(False)

        if self._file is not None:
            self.setWindowFilePath(self._file)
