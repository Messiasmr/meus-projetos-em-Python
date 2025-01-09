import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import pygame

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initMusic()

    def initUI(self):
        # Configurar a janela principal
        self.setWindowTitle('Calculadora Anime')
        self.setGeometry(100, 100, 400, 500)

        # Adicionar imagem de fundo
        oImage = QPixmap("C:\\Users\\marmo\\Desktop\\imagens\\patoshino.jpg")
        sImage = oImage.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        # Layout principal
        layout = QVBoxLayout()

        # Campo de entrada
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.display)

        # Layout dos botões
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('/', 3, 3),
            ('=', 4, 0, 1, 4)
        ]

        for text, row, col, rowspan, colspan in [(b[0], b[1], b[2], 1, 1) if len(b) == 3 else b for b in buttons]:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(self.on_click)
            grid.addWidget(button, row, col, rowspan, colspan)

        layout.addLayout(grid)
        self.setLayout(layout)

    def initMusic(self):
        # Inicializar o mixer do pygame
        pygame.mixer.init()
        # Carregar e tocar a música
        pygame.mixer.music.load("C:\\Users\\marmo\\Desktop\\imagens\\musica.mp3")
        pygame.mixer.music.play(-1)  # Tocar em loop

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Erro')
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())
