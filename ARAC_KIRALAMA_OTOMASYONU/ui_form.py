# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 40, 321, 281))
        self.groupBox.setStyleSheet(u"/* --- Ana Kutu (GroupBox) Ayarlar\u0131 --- */\n"
"QGroupBox {\n"
"    /* Arka Plan: \u00c7ok a\u00e7\u0131k, ferah bir mavi tonu */\n"
"    background-color: #FFFFFF; \n"
"    \n"
"    /* \u00c7er\u00e7eve: Belirgin bir mavi */\n"
"    border: 3px solid #2196F3; \n"
"    \n"
"    /* K\u00f6\u015feleri yumu\u015fat */\n"
"    border-radius: 12px;        \n"
"    \n"
"    /* Ba\u015fl\u0131k yaz\u0131s\u0131n\u0131n \u00e7izginin \u00fcst\u00fcne gelmemesi i\u00e7in yukar\u0131dan bo\u015fluk */\n"
"    margin-top: 25px;           \n"
"    \n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* --- Kutunun Ba\u015fl\u0131\u011f\u0131 (\u00d6rn: Men\u00fc) --- */\n"
"QGroupBox::title {\n"
"    /* Ba\u015fl\u0131\u011f\u0131 kutunun \u00e7er\u00e7evesinin ortas\u0131na yerle\u015ftir */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; \n"
"    \n"
"    /* Ba\u015fl\u0131\u011f\u0131n etraf\u0131na biraz bo\u015fluk b\u0131rak */\n"
"    padding: 5px 15px;\n"
"    \n"
"    /* Ba\u015fl\u0131k Yaz"
                        "\u0131 Rengi: Koyu, okunakl\u0131 mavi */\n"
"    color: #0D47A1; \n"
"    \n"
"    /* Ba\u015fl\u0131\u011f\u0131n kendi arka plan\u0131 (\u015feffaf olsun) */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* --- Butonlar\u0131n Normal Hali --- */\n"
"QPushButton {\n"
"    /* Buton Rengi: Canl\u0131, modern bir mavi */\n"
"    background-color: #1976D2; \n"
"    \n"
"    /* Yaz\u0131 Rengi: Beyaz */\n"
"    color: white;              \n"
"    \n"
"    /* Kenarl\u0131k olmas\u0131n, sadece renk olsun */\n"
"    border: none;\n"
"    \n"
"    /* Buton k\u00f6\u015felerini hafif yuvarlat */\n"
"    border-radius: 6px;\n"
"    \n"
"    /* Butonun i\u00e7i biraz geni\u015f ve ferah olsun */\n"
"    padding: 12px;             \n"
"    \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* --- Butonun \u00dczerine Gelince (Hover) --- */\n"
"QPushButton:hover {\n"
"    /* Rengi biraz daha koyula\u015ft\u0131r */\n"
"    background-color: #1565C0; \n"
"}\n"
"\n"
"/* --- Butona T\u0131klan\u0131"
                        "nca (Pressed) --- */\n"
"QPushButton:pressed {\n"
"    /* T\u0131klama hissi i\u00e7in en koyu mavi tonu */\n"
"    background-color: #0D47A1; \n"
"}")
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 60, 181, 186))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnMusteri = QPushButton(self.verticalLayoutWidget)
        self.btnMusteri.setObjectName(u"btnMusteri")
        font = QFont()
        font.setBold(True)
        self.btnMusteri.setFont(font)

        self.verticalLayout.addWidget(self.btnMusteri)

        self.btnArac = QPushButton(self.verticalLayoutWidget)
        self.btnArac.setObjectName(u"btnArac")
        self.btnArac.setFont(font)

        self.verticalLayout.addWidget(self.btnArac)

        self.btnKiralama = QPushButton(self.verticalLayoutWidget)
        self.btnKiralama.setObjectName(u"btnKiralama")
        self.btnKiralama.setFont(font)

        self.verticalLayout.addWidget(self.btnKiralama)

        self.btnKirada = QPushButton(self.verticalLayoutWidget)
        self.btnKirada.setObjectName(u"btnKirada")
        self.btnKirada.setFont(font)
        self.btnKirada.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.btnKirada)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 100, 81, 101))
        self.label.setPixmap(QPixmap(u"../../Desktop/araba.jpg"))
        self.label.setScaledContents(True)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Y\u00f6netim Paneli", None))
        self.btnMusteri.setText(QCoreApplication.translate("Widget", u"M\u00fc\u015fteri Giri\u015f", None))
        self.btnArac.setText(QCoreApplication.translate("Widget", u"Ara\u00e7 Bilgileri", None))
        self.btnKiralama.setText(QCoreApplication.translate("Widget", u"Ara\u00e7 Kiralama Bilgileri ", None))
        self.btnKirada.setText(QCoreApplication.translate("Widget", u"Kirada Olan Ara\u00e7lar", None))
        self.label.setText("")
    # retranslateUi

