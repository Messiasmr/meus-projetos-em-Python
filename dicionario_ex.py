import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QFileDialog, QMenu, QAction, QTextEdit, QComboBox, QTabWidget, QLabel
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor
from PyQt5.QtCore import Qt
import pygame
import math
import matplotlib.pyplot as plt
import numpy as np

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initMusic()

    def initUI(self):
        # Configurar a janela principal
        self.setWindowTitle('Calculadora Científica Anime')
        self.setGeometry(100, 100, 600, 800)

        # Layout principal
        layout = QVBoxLayout()

        # Botão de menu de hambúrguer
        self.btn_menu = QPushButton('☰')
        self.btn_menu.setFixedSize(30, 30)
        self.btn_menu.setStyleSheet("font-size: 18px; background: transparent; border: none; color: white;")
        self.btn_menu.clicked.connect(self.toggle_menu)
        layout.addWidget(self.btn_menu, alignment=Qt.AlignRight)

        # Campo de entrada
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; background: transparent; border: none; color: white;")
        layout.addWidget(self.display)

        # Histórico de cálculos
        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.history.setStyleSheet("font-size: 18px; background: transparent; border: none; color: white;")
        layout.addWidget(self.history)

        # Layout dos botões
        self.grid = QGridLayout()
        self.buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('/', 3, 3),
            ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('log', 4, 3),
            ('sqrt', 5, 0), ('exp', 5, 1), ('(', 5, 2), (')', 5, 3),
            ('=', 6, 0, 1, 4)
        ]

        self.button_widgets = []
        for text, row, col, rowspan, colspan in [(b[0], b[1], b[2], 1, 1) if len(b) == 3 else b for b in self.buttons]:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(self.on_click)
            self.grid.addWidget(button, row, col, rowspan, colspan)
            self.button_widgets.append(button)

        layout.addLayout(self.grid)

        # ComboBox para selecionar temas
        self.theme_selector = QComboBox()
        self.theme_selector.addItems(["Padrão", "Escuro", "Claro"])
        self.theme_selector.currentIndexChanged.connect(self.change_theme)
        layout.addWidget(self.theme_selector)

        # Aba para modo gráfico
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_graph_tab(), "Gráfico")
        layout.addWidget(self.tabs)

        self.setLayout(layout)

    def initMusic(self):
        # Inicializar o mixer do pygame
        pygame.mixer.init()
        # Carregar e tocar a música
        pygame.mixer.music.load("C:\\Users\\marmo\\Desktop\\imagens\\musica.mp3")
        pygame.mixer.music.play(-1)  # Tocar em loop
        self.music_playing = True

    def toggle_menu(self):
        menu = QMenu()
        
        # Adicionar ação para selecionar imagem
        select_image_action = QAction('Selecionar Imagem', self)
        select_image_action.triggered.connect(self.select_image)
        menu.addAction(select_image_action)

        # Adicionar ação para pausar/reproduzir música
        toggle_music_action = QAction('Pausar Música', self)
        toggle_music_action.triggered.connect(self.toggle_music)
        menu.addAction(toggle_music_action)

        # Adicionar ação para selecionar música
        select_music_action = QAction('Selecionar Música', self)
        select_music_action.triggered.connect(self.select_music)
        menu.addAction(select_music_action)

        # Adicionar ação para exportar histórico
        export_history_action = QAction('Exportar Histórico', self)
        export_history_action.triggered.connect(self.export_history)
        menu.addAction(export_history_action)

        menu.exec_(self.btn_menu.mapToGlobal(self.btn_menu.rect().bottomLeft()))

    def toggle_music(self):
        if self.music_playing:
            pygame.mixer.music.pause()
            self.music_playing = False
        else:
            pygame.mixer.music.unpause()
            self.music_playing = True

    def select_image(self):
        # Abrir diálogo para selecionar imagem
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg)", options=options)
        if fileName:
            self.set_background_image(fileName)

    def select_music(self):
        # Abrir diálogo para selecionar música
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecionar Música", "", "Músicas (*.mp3 *.wav)", options=options)
        if fileName:
            pygame.mixer.music.load(fileName)
            pygame.mixer.music.play(-1)  # Tocar em loop

    def set_background_image(self, image_path):
        # Definir a imagem de fundo
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def change_theme(self, index):
        if index == 0:  # Padrão
            self.setStyleSheet("")
        elif index == 1:  # Escuro
            self.setStyleSheet("background-color: #2E2E2E; color: white;")
        elif index == 2:  # Claro
            self.setStyleSheet("background-color: #FFFFFF; color: black;")

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                expression = self.display.text()
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('log', 'math.log10')
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('exp', 'math.exp')
                result = eval(expression)
                self.display.setText(str(result))
                self.history.append(f"{expression} = {result}")
            except Exception as e:
                self.display.setText('Erro')
        else:
            self.display.setText(self.display.text() + text)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_0:
            self.display.setText(self.display.text() + '0')
        elif key == Qt.Key_1:
            self.display.setText(self.display.text() + '1')
        elif key == Qt.Key_2:
            self.display.setText(self.display.text() + '2')
        elif key == Qt.Key_3:
            self.display.setText(self.display.text() + '3')
        elif key == Qt.Key_4:
            self.display.setText(self.display.text() + '4')
        elif key == Qt.Key_5:
            self.display.setText(self.display.text() + '5')
        elif key == Qt.Key_6:
            self.display.setText(self.display.text() + '6')
        elif key == Qt.Key_7:
            self.display.setText(self.display.text() + '7')
        elif key == Qt.Key_8:
            self.display.setText(self.display.text() + '8')
        elif key == Qt.Key_9:
            self.display.setText(self.display.text() + '9')
        elif key == Qt.Key_Plus:
            self.display.setText(self.display.text() + '+')
        elif key == Qt.Key_Minus:
            self.display.setText(self.display.text() + '-')
        elif key == Qt.Key_Asterisk:
            self.display.setText(self.display.text() + '*')
        elif key == Qt.Key_Slash:
            self.display.setText(self.display.text() + '/')
        elif key == Qt.Key_Equal or key == Qt.Key_Return or key == Qt.Key_Enter:
            self.on_click()
        elif key == Qt.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
        elif key == Qt.Key_Slash:
            self.display.setText(self.display.text() + '/')
        elif key == Qt.Key_Equal or key == Qt.Key_Return or key == Qt.Key_Enter:
            self.on_click()
        elif key == Qt.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
        elif key == Qt.Key_C:
            self.display.clear()

    def create_graph_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.graph_input = QLineEdit()
        self.graph_input.setPlaceholderText("Digite a função (ex: sin(x), cos(x), x**2)")
        layout.addWidget(self.graph_input)

        self.graph_button = QPushButton("Plotar Gráfico")
        self.graph_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.graph_button)

        tab.setLayout(layout)
        return tab

    def plot_graph(self):
        function = self.graph_input.text()
        x = np.linspace(-10, 10, 400)
        y = eval(function)
        plt.plot(x, y)
        plt.title(f"Gráfico de {function}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

    def export_history(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Exportar Histórico", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.history.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())
