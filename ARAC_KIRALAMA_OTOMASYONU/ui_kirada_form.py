# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kirada_form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(544, 382)
        Form.setStyleSheet(u"/* --- GENEL ARKA PLAN --- */\n"
"QWidget {\n"
"    background-color: #E3F2FD; /* Ana ekranla ayn\u0131 a\u00e7\u0131k mavi ton */\n"
"    font-family: \"Segoe UI\";   /* Okunakl\u0131 modern yaz\u0131 tipi */\n"
"    font-size: 13px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* --- TABLO TASARIMI (En \u00d6nemli K\u0131s\u0131m) --- */\n"
"QTableWidget {\n"
"    background-color: white;       /* Tablo i\u00e7i bembeyaz */\n"
"    border: 2px solid #2196F3;     /* Mavi \u00c7er\u00e7eve (Di\u011fer kutularla uyumlu) */\n"
"    border-radius: 10px;           /* K\u00f6\u015feleri yuvarlat */\n"
"    gridline-color: #E0E0E0;       /* Sat\u0131r \u00e7izgileri \u00e7ok silik gri */\n"
"    selection-background-color: #BBDEFB; /* Se\u00e7ili sat\u0131r a\u00e7\u0131k mavi olsun */\n"
"    selection-color: #000000;      /* Se\u00e7ili yaz\u0131 siyah kals\u0131n */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* --- TABLO BA\u015eLIKLARI (\u00dcst K\u0131s\u0131m) --- */\n"
"QHeaderView::section {\n"
"    background-color: #1"
                        "976D2;     /* Ba\u015fl\u0131klar koyu mavi olsun */\n"
"    color: white;                  /* Ba\u015fl\u0131k yaz\u0131lar\u0131 beyaz */\n"
"    padding: 6px;\n"
"    border: 1px solid #1565C0;     /* Aralarda ince \u00e7izgiler */\n"
"    font-weight: bold;             /* Kal\u0131n yaz\u0131 */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Sol \u00fcst k\u00f6\u015fedeki bo\u015f kutucuk (Tablo kesi\u015fimi) */\n"
"QTableCornerButton::section {\n"
"    background-color: #1976D2;\n"
"    border: 1px solid #1565C0;\n"
"}\n"
"\n"
"/* --- BUTONLAR (Senin Kodunla Ayn\u0131) --- */\n"
"QPushButton {\n"
"    background-color: #1976D2; \n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    min-width: 100px; /* Butonlar \u00e7ok dar olmas\u0131n */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1565C0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0D47A1; /* T\u0131"
                        "klay\u0131nca daha da koyu */\n"
"}\n"
"\n"
"/* --- ET\u0130KETLER (Ba\u015fl\u0131klar vb.) --- */\n"
"QLabel {\n"
"    color: #0D47A1; /* Koyu Lacivert (Di\u011fer sayfadaki ba\u015fl\u0131k rengi) */\n"
"    font-weight: bold;\n"
"    font-size: 15px; /* Ba\u015fl\u0131klar biraz daha b\u00fcy\u00fck dursun */\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tblKiradaAraclar = QTableWidget(Form)
        if (self.tblKiradaAraclar.columnCount() < 4):
            self.tblKiradaAraclar.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblKiradaAraclar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblKiradaAraclar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblKiradaAraclar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblKiradaAraclar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblKiradaAraclar.setObjectName(u"tblKiradaAraclar")
        self.tblKiradaAraclar.setStyleSheet(u"/* --- GENEL SAYFA YAPISI --- */\n"
"QWidget {\n"
"    background-color: #E3F2FD; /* Ana arka plan a\u00e7\u0131k mavi */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Modern yaz\u0131 tipi */\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* --- ANA BA\u015eLIK (Label) --- */\n"
"QLabel {\n"
"    color: #1565C0; /* Koyu mavi ba\u015fl\u0131k rengi */\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"/* --- TABLO TASARIMI (QTableWidget) --- */\n"
"QTableWidget {\n"
"    background-color: #FFFFFF; /* Tablo i\u00e7i beyaz */\n"
"    border: 2px solid #2196F3; /* Kenarl\u0131k mavi */\n"
"    border-radius: 8px; /* K\u00f6\u015feler yuvarlak */\n"
"    gridline-color: #BBDEFB; /* Sat\u0131r \u00e7izgileri a\u00e7\u0131k mavi */\n"
"    selection-background-color: #64B5F6; /* Se\u00e7ili sat\u0131r rengi */\n"
"    selection-color: #FFFFFF; /* Se\u00e7ili yaz\u0131 rengi */\n"
"}\n"
"\n"
"/* --- TABLO BA\u015eLIKLARI (Header) --- */\n"
"QHeaderView::section {\n"
"    backg"
                        "round-color: #1976D2; /* Ba\u015fl\u0131k arka plan\u0131 koyu mavi */\n"
"    color: #FFFFFF; /* Ba\u015fl\u0131k yaz\u0131s\u0131 beyaz */\n"
"    padding: 6px 4px; /* \u0130\u00e7 bo\u015fluk */\n"
"    border: none; /* Ba\u015fl\u0131klar aras\u0131 \u00e7izgi olmas\u0131n */\n"
"    border-right: 1px solid #1565C0; /* Sadece sa\u011fda ince \u00e7izgi */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Tablonun sol \u00fcst k\u00f6\u015fesindeki bo\u015f kutu */\n"
"QTableCornerButton::section {\n"
"    background-color: #1976D2;\n"
"    border: none;\n"
"}\n"
"\n"
"/* --- BUTONLAR (QPushButton) --- */\n"
"QPushButton {\n"
"    background-color: #1976D2; /* Buton rengi mavi */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px; /* Butonlar\u0131 biraz geni\u015flet */\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1565C0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}\n"
"\n"
"QPushButton:"
                        "pressed {\n"
"    background-color: #0D47A1; /* T\u0131klay\u0131nca daha koyu */\n"
"}")
        self.tblKiradaAraclar.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblKiradaAraclar.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblKiradaAraclar.horizontalHeader().setDefaultSectionSize(150)
        self.tblKiradaAraclar.horizontalHeader().setStretchLastSection(True)
        self.tblKiradaAraclar.verticalHeader().setDefaultSectionSize(23)

        self.verticalLayout.addWidget(self.tblKiradaAraclar)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"K\u0130RADA OLAN ARA\u00c7LAR", None))
        ___qtablewidgetitem = self.tblKiradaAraclar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Ara\u00e7 Bilgisi", None));
        ___qtablewidgetitem1 = self.tblKiradaAraclar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Plaka", None));
        ___qtablewidgetitem2 = self.tblKiradaAraclar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"M\u00fc\u015fteri Ad Soyad", None));
        ___qtablewidgetitem3 = self.tblKiradaAraclar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"D\u00f6n\u00fc\u015f Tarihi", None));
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"KAPAT", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"L\u0130STEY\u0130 YEN\u0130LE", None))
    # retranslateUi

