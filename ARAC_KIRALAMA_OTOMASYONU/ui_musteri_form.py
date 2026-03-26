# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musteri_form.ui'
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
    QGroupBox, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(504, 375)
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
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 231, 281))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 50, 198, 210))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.dateEdit = QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 320, 111, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 320, 121, 31))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 10, 241, 281))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 50, 223, 201))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 2, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Ki\u015fisel Bilgiler", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"E\u011fitim Durumu:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ad Soyad:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Medeni Durum:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Do\u011fumTarihi:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Mesle\u011fi:", None))
        self.label.setText(QCoreApplication.translate("Form", u"T.C:", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("Form", u"99999999999", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Evli", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Bekar", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Lise", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u00dcniversite", None))

        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0130PTAL", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"KAYDET", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0130leti\u015fim ve Ehliyet", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Adres:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ehliyet S\u0131n\u0131f\u0131:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Telefon No:", None))
        self.lineEdit_3.setInputMask(QCoreApplication.translate("Form", u"(999) 999 99 99", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"M(Motorlu Bisiklet)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"A1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"A2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"A(Motosiklet)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"B1", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"B(Otomobil)", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"BE", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"C1", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"C1E", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"C(Kamyon)", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"CE", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Form", u"D1", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Form", u"D1E", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Form", u"D(Otob\u00fcs)", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Form", u"DE", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("Form", u"F(Trakt\u00f6r)", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("Form", u"G(\u0130\u015f Makines\u0131)", None))

    # retranslateUi

