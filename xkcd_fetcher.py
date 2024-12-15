import requests as req
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os, json, sys

url = 'https://xkcd.com/'

os.makedirs('xkcd',exist_ok=True)

def get_comic_details():
    res = req.get("https://xkcd.com/info.0.json")
    return json.loads(res.text)

def get_comic(url, title):
    res = req.get(url).content

    with open(title + ".png", 'wb') as handler:
        handler.write(res)

class MainWindow(QMainWindow):
    def __init__(self, x, y, alt, title):
        super().__init__()
        layout = QVBoxLayout()

        self.x = x
        self.y = y
        self.alt = alt
        self.title = title

        comic = QLabel(self)
        pixmap = QPixmap(self.title + ".png")
        comic.setPixmap(pixmap)
        comic.setAlignment(Qt.AlignmentFlag.AlignTop)

        alt_label = QLabel(alt,self)
        font = alt_label.font()
        font.setPointSize(12)
        alt_label.setFont(font)
        alt_label.setWordWrap(True)
        alt_label.setContentsMargins(10,15,10,10)
        alt_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        
        comic.adjustSize()
        alt_label.adjustSize()
        comic.setFixedSize(comic.size())
        
        layout.addWidget(comic)
        layout.addWidget(alt_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.resize(self.minimumSizeHint())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnBottomHint | Qt.WindowType.Tool)
        self.setGeometry(self.x - (pixmap.width() + 50), self.y, pixmap.width() + 20, pixmap.height())

if __name__ == "__main__":
    comic_details = get_comic_details()
    alt = comic_details.get("alt")
    title = comic_details.get("safe_title")
    url = comic_details.get("img")
    get_comic(url, title)

    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    x = screen.size().width()
    y = 30
    window = MainWindow(x,y,alt,title)
    window.show()

    sys.exit(app.exec())
