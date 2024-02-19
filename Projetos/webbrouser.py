import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainStream(QMainWindow):
    def __init__(self):
        super(MainStream, self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl("http://www.google.com"))  # Corrigido para adicionar 'http://'
        self.setCentralWidget(self.Browser)  # Corrigido 'self.centralWidget' para 'self.setCentralWidget'
        self.showMaximized()
        navBar = QToolBar()
        self.addToolBar(navBar)

        BackButton = QAction('Voltar', self)
        BackButton.triggered.connect(self.Browser.back)
        navBar.addAction(BackButton)

        FowardButton = QAction('Avançar', self)
        FowardButton.triggered.connect(self.Browser.forward)
        navBar.addAction(FowardButton)

        ReloadButton = QAction('Recarregar', self)
        ReloadButton.triggered.connect(self.Browser.reload)
        navBar.addAction(ReloadButton)

        HomeButton = QAction('Menu', self)
        HomeButton.triggered.connect(self.NavigateHome)
        navBar.addAction(HomeButton)

        self.UrlBar = QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavigateToUrl)

        navBar.addWidget(self.UrlBar)
        self.Browser.urlChanged.connect(self.UpdateUrl)

    def NavigateHome(self):
        self.Browser.setUrl(QUrl("http://www.google.com"))  # Corrigido para adicionar 'http://'

    def NavigateToUrl(self):
        Url = self.UrlBar.text()
        self.Browser.setUrl(QUrl(Url))  # Corrigido para usar a URL digitada

    def UpdateUrl(self, p):
        self.UrlBar.setText(p.toString())  # Corrigido para usar toString() em vez de str()

Application = QApplication(sys.argv)
QApplication.setApplicationName('web browser by- valkenrox')
Window = MainStream()
Application.exec_()