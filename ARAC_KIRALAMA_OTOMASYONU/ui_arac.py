# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arac_bilgi_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(622, 540)
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
        self.groupBox.setGeometry(QRect(30, 30, 231, 281))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 50, 198, 211))
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
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout.addWidget(self.comboBox_4, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 490, 121, 31))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(270, 30, 241, 411))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 50, 225, 354))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_2.addWidget(self.comboBox_8, 6, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 0, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 7, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 7, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 320, 221, 141))
        self.gridLayoutWidget_3 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 40, 191, 91))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_3.addWidget(self.comboBox_9, 0, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 1, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 490, 121, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Ara\u00e7 Kimlik \u0130\u015flemleri", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u00dcretim Y\u0131l\u0131:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Marka:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Motor No:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Model:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u015easi No:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Plaka:", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("Form", u"99999999999", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"45 ABC 123", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"TR12345678901234567", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0130PTAL", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Teknik ve Kiralama Detaylar\u0131", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"2", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"4", None))

        self.label_16.setText(QCoreApplication.translate("Form", u"\u00c7eki\u015f:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Manuel", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Otomatik", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Yar\u0131 Otomatik", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"Kasa Tipi:", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("Form", u"\u00d6nden \u00c7eki\u015f", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Form", u"Arkadan \u0130ti\u015f", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("Form", u" 4x4(D\u00f6rt \u00c7eker)", None))

        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"110 HP", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"Benzin", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Form", u"Dizel", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Form", u"Benzin & LPG", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("Form", u"Elektrik", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("Form", u"Hibrit", None))

        self.label_15.setText(QCoreApplication.translate("Form", u"Kap\u0131 Say\u0131s\u0131:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Renk:", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Form", u"1600 cc", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Motor G\u00fcc\u00fc:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Vites:", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Form", u"Sedan", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Form", u"Hatchback", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Form", u"Station Wagon", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("Form", u"SUV", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("Form", u"Cabrio", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("Form", u"Coupe", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("Form", u"Minivan", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("Form", u"Pick-up", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Yak\u0131t Tipi:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Motor Hacmi:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Fiyat ve Durum", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"G\u00fcnl\u00fck \u00dccret:", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("Form", u"Bo\u015fta", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("Form", u"Kirada", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("Form", u"Bak\u0131mda", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"Durumu:", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"TL", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"KAYDET", None))
    # retranslateUi

