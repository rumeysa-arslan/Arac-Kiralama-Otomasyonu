# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arac_kiralama_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(666, 625)
        Form.setStyleSheet(u"/* --- GENEL ARKA PLAN --- */\n"
"QWidget {\n"
"    background-color: #E3F2FD; /* Ana ekranla ayn\u0131 a\u00e7\u0131k mavi ton */\n"
"    font-family: \"Segoe UI\";   /* Okunakl\u0131 modern yaz\u0131 tipi */\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* --- GRUP KUTULARI (Ki\u015fisel Bilgiler vb.) --- */\n"
"QGroupBox {\n"
"    border: 2px solid #2196F3; /* Mavi \u00c7er\u00e7eve */\n"
"    border-radius: 10px;       /* K\u00f6\u015feleri Yuvarlat */\n"
"    margin-top: 25px;          /* Ba\u015fl\u0131k i\u00e7in pay */\n"
"    font-weight: bold;\n"
"    color: #0D47A1;            /* Ba\u015fl\u0131k Rengi: Koyu Lacivert */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortala */\n"
"    padding: 0 10px;\n"
"    background-color: #E3F2FD; /* \u00c7izgi yaz\u0131n\u0131n alt\u0131ndan ge\u00e7mesin */\n"
"}\n"
"\n"
"/* --- YAZI ET\u0130KETLER\u0130 (Ad, Soyad vb.) --- */\n"
"QLabel {\n"
"    color: #1565C0; /* Orta ko"
                        "yulukta mavi */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* --- G\u0130R\u0130\u015e KUTULARI (Text, Combo, Date) --- */\n"
"QLineEdit, QComboBox, QDateEdit, QPlainTextEdit {\n"
"    background-color: white;   /* \u0130\u00e7i bembeyaz olsun */\n"
"    border: 1px solid #90CAF9; /* \u0130nce mavi \u00e7er\u00e7eve */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #333333;            /* Yaz\u0131lan yaz\u0131 koyu gri */\n"
"}\n"
"\n"
"/* Kutulara t\u0131klay\u0131nca (Odaklan\u0131nca) */\n"
"QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QPlainTextEdit:focus {\n"
"    border: 2px solid #2196F3; /* Se\u00e7ili kutunun \u00e7er\u00e7evesi kal\u0131nla\u015fs\u0131n */\n"
"}\n"
"\n"
"/* --- BUTONLAR (Genel) --- */\n"
"QPushButton {\n"
"    background-color: #1976D2; /* Ana men\u00fcdeki mavi buton */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
""
                        "\n"
"QPushButton:hover {\n"
"    background-color: #1565C0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0D47A1; /* T\u0131klay\u0131nca daha da koyu */\n"
"}")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(280, 20, 241, 211))
        self.groupBox_2.setStyleSheet(u"/* --- GENEL ARKA PLAN --- */\n"
"QWidget {\n"
"    background-color: #E3F2FD; /* Ana ekranla ayn\u0131 a\u00e7\u0131k mavi ton */\n"
"    font-family: \"Segoe UI\";   /* Okunakl\u0131 modern yaz\u0131 tipi */\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* --- GRUP KUTULARI (Ki\u015fisel Bilgiler vb.) --- */\n"
"QGroupBox {\n"
"    border: 2px solid #2196F3; /* Mavi \u00c7er\u00e7eve */\n"
"    border-radius: 10px;       /* K\u00f6\u015feleri Yuvarlat */\n"
"    margin-top: 25px;          /* Ba\u015fl\u0131k i\u00e7in pay */\n"
"    font-weight: bold;\n"
"    color: #0D47A1;            /* Ba\u015fl\u0131k Rengi: Koyu Lacivert */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortala */\n"
"    padding: 0 10px;\n"
"    background-color: #E3F2FD; /* \u00c7izgi yaz\u0131n\u0131n alt\u0131ndan ge\u00e7mesin */\n"
"}\n"
"\n"
"/* --- YAZI ET\u0130KETLER\u0130 (Ad, Soyad vb.) --- */\n"
"QLabel {\n"
"    color: #1565C0; /* Orta ko"
                        "yulukta mavi */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* --- G\u0130R\u0130\u015e KUTULARI (Text, Combo, Date) --- */\n"
"QLineEdit, QComboBox, QDateEdit, QPlainTextEdit {\n"
"    background-color: white;   /* \u0130\u00e7i bembeyaz olsun */\n"
"    border: 1px solid #90CAF9; /* \u0130nce mavi \u00e7er\u00e7eve */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #333333;            /* Yaz\u0131lan yaz\u0131 koyu gri */\n"
"}\n"
"\n"
"/* Kutulara t\u0131klay\u0131nca (Odaklan\u0131nca) */\n"
"QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QPlainTextEdit:focus {\n"
"    border: 2px solid #2196F3; /* Se\u00e7ili kutunun \u00e7er\u00e7evesi kal\u0131nla\u015fs\u0131n */\n"
"}\n"
"\n"
"/* --- BUTONLAR (Genel) --- */\n"
"QPushButton {\n"
"    background-color: #1976D2; /* Ana men\u00fcdeki mavi buton */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
""
                        "\n"
"QPushButton:hover {\n"
"    background-color: #1565C0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0D47A1; /* T\u0131klay\u0131nca daha da koyu */\n"
"}")
        self.gridLayoutWidget_2 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 50, 225, 141))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 0, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(40, 240, 481, 251))
        self.groupBox_3.setStyleSheet(u"/* --- GENEL ARKA PLAN --- */\n"
"QWidget {\n"
"    background-color: #E3F2FD; /* Ana ekranla ayn\u0131 a\u00e7\u0131k mavi ton */\n"
"    font-family: \"Segoe UI\";   /* Okunakl\u0131 modern yaz\u0131 tipi */\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* --- GRUP KUTULARI (Ki\u015fisel Bilgiler vb.) --- */\n"
"QGroupBox {\n"
"    border: 2px solid #2196F3; /* Mavi \u00c7er\u00e7eve */\n"
"    border-radius: 10px;       /* K\u00f6\u015feleri Yuvarlat */\n"
"    margin-top: 25px;          /* Ba\u015fl\u0131k i\u00e7in pay */\n"
"    font-weight: bold;\n"
"    color: #0D47A1;            /* Ba\u015fl\u0131k Rengi: Koyu Lacivert */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortala */\n"
"    padding: 0 10px;\n"
"    background-color: #E3F2FD; /* \u00c7izgi yaz\u0131n\u0131n alt\u0131ndan ge\u00e7mesin */\n"
"}\n"
"\n"
"/* --- YAZI ET\u0130KETLER\u0130 (Ad, Soyad vb.) --- */\n"
"QLabel {\n"
"    color: #1565C0; /* Orta ko"
                        "yulukta mavi */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* --- G\u0130R\u0130\u015e KUTULARI (Text, Combo, Date) --- */\n"
"QLineEdit, QComboBox, QDateEdit, QPlainTextEdit {\n"
"    background-color: white;   /* \u0130\u00e7i bembeyaz olsun */\n"
"    border: 1px solid #90CAF9; /* \u0130nce mavi \u00e7er\u00e7eve */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #333333;            /* Yaz\u0131lan yaz\u0131 koyu gri */\n"
"}\n"
"\n"
"/* Kutulara t\u0131klay\u0131nca (Odaklan\u0131nca) */\n"
"QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QPlainTextEdit:focus {\n"
"    border: 2px solid #2196F3; /* Se\u00e7ili kutunun \u00e7er\u00e7evesi kal\u0131nla\u015fs\u0131n */\n"
"}\n"
"\n"
"/* --- BUTONLAR (Genel) --- */\n"
"QPushButton {\n"
"    background-color: #1976D2; /* Ana men\u00fcdeki mavi buton */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
""
                        "\n"
"QPushButton:hover {\n"
"    background-color: #1565C0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0D47A1; /* T\u0131klay\u0131nca daha da koyu */\n"
"}")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 110, 201, 31))
        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 421, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.horizontalLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout.addWidget(self.label_18)

        self.dateEdit = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)

        self.label_19 = QLabel(self.horizontalLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout.addWidget(self.label_19)

        self.dateEdit_2 = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout.addWidget(self.dateEdit_2)

        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(40, 160, 381, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.label_5 = QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_5)

        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(16, 110, 91, 20))
        self.lineEdit_gidilecek = QLineEdit(self.groupBox_3)
        self.lineEdit_gidilecek.setObjectName(u"lineEdit_gidilecek")
        self.lineEdit_gidilecek.setGeometry(QRect(110, 110, 113, 31))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 20, 231, 211))
        self.groupBox.setStyleSheet(u"/* --- GENEL ARKA PLAN --- */\n"
"QWidget {\n"
"    background-color: #E3F2FD; /* Ana ekranla ayn\u0131 a\u00e7\u0131k mavi ton */\n"
"    font-family: \"Segoe UI\";   /* Okunakl\u0131 modern yaz\u0131 tipi */\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* --- GRUP KUTULARI (Ki\u015fisel Bilgiler vb.) --- */\n"
"QGroupBox {\n"
"    border: 2px solid #2196F3; /* Mavi \u00c7er\u00e7eve */\n"
"    border-radius: 10px;       /* K\u00f6\u015feleri Yuvarlat */\n"
"    margin-top: 25px;          /* Ba\u015fl\u0131k i\u00e7in pay */\n"
"    font-weight: bold;\n"
"    color: #0D47A1;            /* Ba\u015fl\u0131k Rengi: Koyu Lacivert */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Ba\u015fl\u0131\u011f\u0131 ortala */\n"
"    padding: 0 10px;\n"
"    background-color: #E3F2FD; /* \u00c7izgi yaz\u0131n\u0131n alt\u0131ndan ge\u00e7mesin */\n"
"}\n"
"\n"
"/* --- YAZI ET\u0130KETLER\u0130 (Ad, Soyad vb.) --- */\n"
"QLabel {\n"
"    color: #1565C0; /* Orta ko"
                        "yulukta mavi */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* --- G\u0130R\u0130\u015e KUTULARI (Text, Combo, Date) --- */\n"
"QLineEdit, QComboBox, QDateEdit, QPlainTextEdit {\n"
"    background-color: white;   /* \u0130\u00e7i bembeyaz olsun */\n"
"    border: 1px solid #90CAF9; /* \u0130nce mavi \u00e7er\u00e7eve */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: #333333;            /* Yaz\u0131lan yaz\u0131 koyu gri */\n"
"}\n"
"\n"
"/* Kutulara t\u0131klay\u0131nca (Odaklan\u0131nca) */\n"
"QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QPlainTextEdit:focus {\n"
"    border: 2px solid #2196F3; /* Se\u00e7ili kutunun \u00e7er\u00e7evesi kal\u0131nla\u015fs\u0131n */\n"
"}\n"
"\n"
"/* --- BUTONLAR (Genel) --- */\n"
"QPushButton {\n"
"    background-color: #1976D2; /* Ana men\u00fcdeki mavi buton */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
""
                        "\n"
"QPushButton:hover {\n"
"    background-color: #1565C0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0D47A1; /* T\u0131klay\u0131nca daha da koyu */\n"
"}")
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 50, 198, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.leTelefon = QLineEdit(self.gridLayoutWidget)
        self.leTelefon.setObjectName(u"leTelefon")
        self.leTelefon.setReadOnly(True)

        self.gridLayout.addWidget(self.leTelefon, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.leAdSoyad = QLineEdit(self.gridLayoutWidget)
        self.leAdSoyad.setObjectName(u"leAdSoyad")
        self.leAdSoyad.setReadOnly(True)

        self.gridLayout.addWidget(self.leAdSoyad, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Ara\u00e7 Se\u00e7imi", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Ara\u00e7 Plakas\u0131:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Marka/Model:", None))
        self.lineEdit_8.setPlaceholderText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"G\u00fcnl\u00fck \u00dccret:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Tarih ve Hesaplama", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"HESAPLA", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Al\u0131\u015f Tarihi:", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u0130ade Tarihi:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Toplam G\u00fcn:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TOPLAM TUTAR:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TL", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Gidilecek Yer:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"M\u00fc\u015fteri Se\u00e7imi", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ad Soyad:", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("Form", u"99999999999", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"99999999999", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Telefon No:", None))
        self.label.setText(QCoreApplication.translate("Form", u"T.C:", None))
    # retranslateUi

