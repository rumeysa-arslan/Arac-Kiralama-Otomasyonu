import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, QDate

from veritabani import Database

from ui_form import Ui_Widget
from ui_musteri_form import Ui_Form as Ui_Musteri
from ui_arac_bilgi_form import Ui_Form as Ui_Arac
from ui_arac_kiralama_form import Ui_Form as Ui_Kiralama
from ui_kirada_form import Ui_Form as Ui_Kirada

# ---------------------------------------------------------
# 1. MÜŞTERİ PENCERESİ
# ---------------------------------------------------------
class MusteriPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Musteri()
        self.ui.setupUi(self)
        self.db = Database()

        self.ui.pushButton.clicked.connect(self.kaydet)
        self.ui.pushButton_2.clicked.connect(self.close)

    def kaydet(self):
        try:
            tc = self.ui.lineEdit.text()
            ad_soyad = self.ui.lineEdit_2.text()

            parts = ad_soyad.strip().split(' ', 1)
            ad = parts[0]
            soyad = parts[1] if len(parts) > 1 else ""

            if not tc or not ad:
                QMessageBox.warning(self, "Uyarı", "TC ve Ad Soyad zorunludur!")
                return

            self.db.musteri_ekle(ad=ad, soyad=soyad, tc_kimlik=tc, dogum_tarihi=self.ui.dateEdit.date().toString("dd.MM.yyyy"),
                                 adres=self.ui.plainTextEdit.toPlainText(), telefon=self.ui.lineEdit_3.text(),
                                 meslek=self.ui.lineEdit_4.text(), ehliyet_sinifi=self.ui.comboBox.currentText(),
                                 medeni_durum=self.ui.comboBox_2.currentText(), egitim_durumu=self.ui.comboBox_3.currentText())
            QMessageBox.information(self, "Başarılı", "Müşteri Kaydedildi")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))

# ---------------------------------------------------------
# 2. ARAÇ PENCERESİ
# ---------------------------------------------------------
# widget.py dosyasında AracPenceresi sınıfını şu şekilde güncelleyin:

from PySide6.QtWidgets import QLabel, QLineEdit # En üste ekleyin

class AracPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Arac()
        self.ui.setupUi(self)
        self.db = Database()

        self.ui.lineEdit.setInputMask("")
        self.kutulari_doldur()

        # --- YENİ EKLENEN KISIM: MENZİL ALANLARI ---
        # Tasarım dosyasına dokunmadan kod ile arayüze ekliyoruz
        self.label_menzil = QLabel("Menzil (km):")
        self.lineEdit_menzil = QLineEdit()
        self.lineEdit_menzil.setPlaceholderText("Örn: 450 km")

        # Teknik detaylar grubuna (gridLayout_2) ekleyelim (En alt satıra)
        # Mevcut satır sayısı 8 olduğu için 8. satıra ekliyoruz
        self.ui.gridLayout_2.addWidget(self.label_menzil, 8, 0)
        self.ui.gridLayout_2.addWidget(self.lineEdit_menzil, 8, 1)

        # Başlangıçta gizleyelim
        self.label_menzil.setVisible(False)
        self.lineEdit_menzil.setVisible(False)

        # Yakıt türü değişince çalışacak fonksiyonu bağla
        self.ui.comboBox_5.currentTextChanged.connect(self.yakit_turu_kontrol)
        # -------------------------------------------

        self.ui.pushButton.clicked.connect(self.kaydet)
        self.ui.pushButton_2.clicked.connect(self.close)

    def yakit_turu_kontrol(self, text):
        """Yakıt türü Elektrik ise menzil alanını gösterir."""
        if text == "Elektrik":
            self.label_menzil.setVisible(True)
            self.lineEdit_menzil.setVisible(True)
        else:
            self.label_menzil.setVisible(False)
            self.lineEdit_menzil.setVisible(False)
            self.lineEdit_menzil.clear()

    def kutulari_doldur(self):
        # ... (Mevcut kodlarınız aynı kalsın) ...
        # Sadece comboBox_5 kontrolü yapın, "Elektrik" zaten listede var mı diye.
        markalar = ["Toyota", "Renault", "Fiat", "Ford", "BMW", "Mercedes", "Volkswagen", "Honda", "Hyundai", "Peugeot", "Togg"] # Togg ekledim :)
        self.ui.comboBox_4.clear()
        self.ui.comboBox_4.addItems(markalar)

        yillar = [str(yil) for yil in range(2026, 2000, -1)]
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(yillar)

        # Eğer tasarım dosyasında Elektrik yoksa buraya ekler, varsa pas geçer
        if self.ui.comboBox_5.findText("Elektrik") == -1:
             self.ui.comboBox_5.addItem("Elektrik")

    def kaydet(self):
        try:
            plaka = self.ui.lineEdit.text().upper()
            ucret_text = self.ui.lineEdit_9.text().replace(",", ".")
            ucret = float(ucret_text) if ucret_text else 0.0

            # Menzil bilgisini al
            menzil_bilgisi = self.lineEdit_menzil.text() if self.lineEdit_menzil.isVisible() else None

            # Veritabanına menzil parametresini de gönderiyoruz
            self.db.arac_ekle(self.ui.comboBox_4.currentText(), self.ui.lineEdit_2.text(), self.ui.comboBox_3.currentText(),
                              self.ui.comboBox_5.currentText(), self.ui.comboBox.currentText(), self.ui.lineEdit_6.text(),
                              self.ui.comboBox_6.currentText(), self.ui.lineEdit_8.text(), self.ui.comboBox_8.currentText(),
                              self.ui.comboBox_2.currentText(), self.ui.lineEdit_7.text(), self.ui.lineEdit_5.text(),
                              self.ui.lineEdit_4.text(), ucret, self.ui.comboBox_9.currentText(), plaka,
                              menzil=menzil_bilgisi) # <--- YENİ PARAMETRE

            QMessageBox.information(self, "Başarılı", f"Araç Kaydedildi!\nFiyat: {ucret} TL")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Araç kaydedilemedi: {str(e)}")

# ---------------------------------------------------------
# 3. KİRALAMA PENCERESİ (GÜNCELLENDİ: leAdSoyad ve leTelefon)
# ---------------------------------------------------------
class KiralamaPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Kiralama()
        self.ui.setupUi(self)
        self.db = Database()

        self.verileri_yukle()

        self.ui.lineEdit.textChanged.connect(self.tc_kontrol)

        self.ui.comboBox_6.currentIndexChanged.connect(self.arac_detay_getir)

        self.ui.pushButton.clicked.connect(self.hesapla_ve_kirala)

        self.gunluk_ucret = 0.0

    def verileri_yukle(self):
        self.ui.comboBox_6.clear()
        araclar = self.db.bosta_arac_listele()
        for a in araclar:
            self.ui.comboBox_6.addItem(a['plaka'], a['arac_id'])

        self.arac_detay_getir()

    def tc_kontrol(self):
        if len(self.ui.lineEdit.text()) == 11:
            self.tc_ile_musteri_getir()

    def tc_ile_musteri_getir(self):
        tc = self.ui.lineEdit.text()
        musteri = self.db.get_musteri_by_tc(tc)

        if musteri:
            self.ui.leAdSoyad.setText(f"{musteri['ad']} {musteri['soyad']}")
            self.ui.leTelefon.setText(musteri['telefon'])
        else:
            self.ui.leAdSoyad.clear()
            self.ui.leTelefon.clear()

    def arac_detay_getir(self):
        arac_id = self.ui.comboBox_6.currentData()

        if arac_id is None:
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_8.clear()
            self.gunluk_ucret = 0.0
            return

        arac = self.db.get_arac_by_id(arac_id)
        if arac:
            self.gunluk_ucret = float(arac['gunluk_ucret'])

            try:
                self.ui.lineEdit_7.setText(f"{arac['marka']} {arac['model']}")
                self.ui.lineEdit_8.setText(f"{self.gunluk_ucret:.2f}")
            except:
                pass

            # widget.py dosyasında KiralamaPenceresi sınıfının hesapla_ve_kirala metodunu güncelleyin:

    def hesapla_ve_kirala(self):
            try:
                tc = self.ui.lineEdit.text()
                musteri = self.db.get_musteri_by_tc(tc)
                arac_id = self.ui.comboBox_6.currentData()

                gidilecek = ""
                if hasattr(self.ui, 'lineEdit_gidilecek'):
                    gidilecek = self.ui.lineEdit_gidilecek.text()
                elif hasattr(self.ui, 'lineEdit_6'):
                    gidilecek = self.ui.lineEdit_6.text() # ui dosyasındaki isimlendirmeye göre

                arac = self.db.get_arac_by_id(arac_id) # Aracı veritabanından çek
                guncel_fiyat = float(arac['gunluk_ucret']) if arac else 0.0

                        # ... (Validasyon kontrolleri aynı kalsın: if not musteri, if not arac_id vb.) ...
                if not musteri:
                    return QMessageBox.warning(self, "Hata", "Müşteri bulunamadı! Lütfen TC'yi kontrol edin.")
                if not arac_id:
                    return QMessageBox.warning(self, "Hata", "Araç seçilmedi!")

                alis = self.ui.dateEdit.date()
                iade = self.ui.dateEdit_2.date()
                gun = alis.daysTo(iade)

                if gun <= 0:
                    return QMessageBox.warning(self, "Hata", "İade tarihi, alış tarihinden en az 1 gün sonra olmalı!")

                toplam = gun * guncel_fiyat


                ozel_mesaj = ""
                if arac['yakit_turu'] == "Elektrik":
                    toplam = toplam * 0.5  # %50 İndirim
                    ozel_mesaj = "\n(Elektrikli araç indirimi uygulandı: %50)"
                        # -------------------------------------------

                self.ui.lineEdit_4.setText(str(gun))
                self.ui.lineEdit_5.setText(f"{toplam:.2f}")

                mesaj = (f"Müşteri: {musteri['ad']} {musteri['soyad']}\n"
                         f"Araç: {self.ui.lineEdit_7.text()}\n"
                         f"-----------------------------\n"
                         f"Süre: {gun} Gün\n"
                         f"Günlük: {guncel_fiyat} TL\n"
                         f"TOPLAM: {toplam} TL{ozel_mesaj}\n\n" # Mesaja indirim notunu ekledik
                         f"Onaylıyor musunuz?")

                onay = QMessageBox.question(self, "Kiralama Onayı", mesaj, QMessageBox.Yes | QMessageBox.No)

                if onay == QMessageBox.Yes:
                    self.db.kira_ekle(
                        musteri['musteri_id'],
                        arac_id,
                        alis.toString("dd.MM.yyyy"),
                        iade.toString("dd.MM.yyyy"),
                        gun,
                        gidilecek,
                        toplam
                    )
                    QMessageBox.information(self, "Başarılı", "Kiralama işlemi tamamlandı!")
                    self.close()

            except Exception as e:
                QMessageBox.critical(self, "Hata", str(e))

# ---------------------------------------------------------
# 4. KİRADA OLANLAR PENCERESİ
# ---------------------------------------------------------
class KiradaPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Kirada()
        self.ui.setupUi(self)
        self.db = Database()

        self.listele()
        self.ui.pushButton.clicked.connect(self.listele)
        self.ui.pushButton_2.clicked.connect(self.close)

    def listele(self):
        try:
            veriler = self.db.kira_listele()
            self.ui.tblKiradaAraclar.setRowCount(0)
            for row, veri in enumerate(veriler):
                self.ui.tblKiradaAraclar.insertRow(row)
                self.ui.tblKiradaAraclar.setItem(row, 0, QTableWidgetItem(f"{veri['marka']} {veri['model']}"))
                self.ui.tblKiradaAraclar.setItem(row, 1, QTableWidgetItem(veri['plaka']))
                self.ui.tblKiradaAraclar.setItem(row, 2, QTableWidgetItem(f"{veri['ad']} {veri['soyad']}"))
                self.ui.tblKiradaAraclar.setItem(row, 3, QTableWidgetItem(str(veri['bitis_tarihi'])))
        except Exception as e:
            print(f"Liste Hatası: {e}")

# ---------------------------------------------------------
# ANA PENCERE
# ---------------------------------------------------------
class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.btnMusteri.clicked.connect(lambda: self.ac(MusteriPenceresi))
        self.ui.btnArac.clicked.connect(lambda: self.ac(AracPenceresi))
        self.ui.btnKiralama.clicked.connect(lambda: self.ac(KiralamaPenceresi))
        self.ui.btnKirada.clicked.connect(lambda: self.ac(KiradaPenceresi))

    def ac(self, pencere_sinifi):
        self.pencere = pencere_sinifi()
        self.pencere.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnaPencere()
    window.show()
    sys.exit(app.exec())
