import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self,
                 host="localhost",
                 user="root",
                 port=3306):

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

        self._create_database()
        self._connect_database()
        self._create_tables()
        self._ornek_veri_ekle()

    def _create_database(self):
        try:
            conn = mysql.connector.connect(
                host=self.host, user=self.user, password=self.password, port=self.port
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{self.database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_turkish_ci")
            conn.close()
            print(f"[BILGI] Database kontrol edildi: {self.database}")
        except Error as e:
            print(f"Database hatasi: {e.msg}")

    def _connect_database(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host, user=self.user, password=self.password,
                database=self.database, port=self.port
            )
            self.cursor = self.connection.cursor(dictionary=True, buffered=True)
            print("[BILGI] Veritabanina baglanildi")
        except Error as e:
            print(f"Baglanti hatasi: {e.msg}")

    def _create_tables(self):
        try:

            #self.cursor.execute("DROP TABLE IF EXISTS kiralamalar")
            #self.cursor.execute("DROP TABLE IF EXISTS araclar")
            # ------------------------------

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS musteriler (
                    musteri_id INT AUTO_INCREMENT PRIMARY KEY,
                    ad VARCHAR(50), soyad VARCHAR(50), tc_kimlik VARCHAR(11) UNIQUE,
                    dogum_tarihi VARCHAR(20), adres TEXT, telefon VARCHAR(20),
                    meslek VARCHAR(50), ehliyet_sinifi VARCHAR(50),
                    medeni_durum VARCHAR(20), egitim_durumu VARCHAR(50)
                )
            """)


            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS araclar (
                    arac_id INT AUTO_INCREMENT PRIMARY KEY,
                    marka VARCHAR(50), model VARCHAR(50), uretim_yili VARCHAR(10),
                    yakit_turu VARCHAR(20), vites_tipi VARCHAR(20), motor_gucu VARCHAR(20),
                    kasa_tipi VARCHAR(20), motor_hacmi VARCHAR(20), cekis VARCHAR(20),
                    kapi_sayisi VARCHAR(10), renk VARCHAR(20), motor_no VARCHAR(50),
                    sasi_no VARCHAR(50), gunluk_ucret DECIMAL(10,2), durum VARCHAR(20),
                    plaka VARCHAR(20) UNIQUE,
                    menzil VARCHAR(20)
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS kiralamalar (
                    kira_id INT AUTO_INCREMENT PRIMARY KEY,
                    musteri_id INT, arac_id INT,
                    baslangic_tarihi VARCHAR(20), bitis_tarihi VARCHAR(20),
                    gun_sayisi INT, gidilecek_yer VARCHAR(100), toplam_ucret DECIMAL(10,2),
                    FOREIGN KEY (musteri_id) REFERENCES musteriler(musteri_id) ON DELETE CASCADE,
                    FOREIGN KEY (arac_id) REFERENCES araclar(arac_id) ON DELETE CASCADE
                )
            """)
            self.connection.commit()
            print("[BILGI] Tablolar hazir (Eski veriler temizlendi ve yeniden kuruldu)")
        except Error as e:
            print(f"Tablo hatasi: {e.msg}")

    def _ornek_veri_ekle(self):
        try:
            self.cursor.execute("SELECT COUNT(*) as sayi FROM musteriler")
            if self.cursor.fetchone()['sayi'] == 0:
                print("[BILGI] Ornek musteriler ekleniyor...")
                sql = "INSERT INTO musteriler (ad, soyad, tc_kimlik, telefon, ehliyet_sinifi) VALUES (%s, %s, %s, %s, %s)"
                veriler = [("Ahmet", "Yılmaz", "11111111111", "05551112233", "B"), ("Ayşe", "Demir", "22222222222", "05554445566", "B")]
                self.cursor.executemany(sql, veriler)
                self.connection.commit()

            self.cursor.execute("SELECT COUNT(*) as sayi FROM araclar")
            if self.cursor.fetchone()['sayi'] == 0:
                print("[BILGI] Ornek araclar ekleniyor...")
                sql = "INSERT INTO araclar (plaka, marka, model, uretim_yili, gunluk_ucret, durum, menzil) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                veriler = [("34 ABC 12", "Toyota", "Corolla", "2020", 1500, "Boşta", None), ("35 DEF 34", "Renault", "Clio", "2022", 1200, "Boşta", None)]
                self.cursor.executemany(sql, veriler)
                self.connection.commit()
        except Error as e:
            print(f"Ornek veri hatasi: {e}")

    def musteri_ekle(self, ad, soyad, tc_kimlik, dogum_tarihi=None, adres=None, telefon=None, meslek=None, ehliyet_sinifi=None, medeni_durum=None, egitim_durumu=None):
        query = "INSERT INTO musteriler (ad, soyad, tc_kimlik, dogum_tarihi, adres, telefon, meslek, ehliyet_sinifi, medeni_durum, egitim_durumu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (ad, soyad, tc_kimlik, dogum_tarihi, adres, telefon, meslek, ehliyet_sinifi, medeni_durum, egitim_durumu)
        self._execute(query, params)

    def musteri_listele(self):
        self.cursor.execute("SELECT * FROM musteriler ORDER BY musteri_id DESC")
        return self.cursor.fetchall()

    def arac_ekle(self, marka, model, uretim_yili, yakit_turu, vites_tipi, motor_gucu, kasa_tipi, motor_hacmi, cekis, kapi_sayisi, renk, motor_no, sasi_no, gunluk_ucret, durum, plaka, menzil=None):
        query = "INSERT INTO araclar (marka, model, uretim_yili, yakit_turu, vites_tipi, motor_gucu, kasa_tipi, motor_hacmi, cekis, kapi_sayisi, renk, motor_no, sasi_no, gunluk_ucret, durum, plaka, menzil) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (marka, model, uretim_yili, yakit_turu, vites_tipi, motor_gucu, kasa_tipi, motor_hacmi, cekis, kapi_sayisi, renk, motor_no, sasi_no, gunluk_ucret, durum, plaka, menzil)
        self._execute(query, params)

    def bosta_arac_listele(self):
        self.cursor.execute("SELECT * FROM araclar WHERE durum = 'Boşta' ORDER BY arac_id DESC")
        return self.cursor.fetchall()

    def kira_ekle(self, musteri_id, arac_id, baslangic_tarihi, bitis_tarihi, gun_sayisi, gidilecek_yer, toplam_ucret):
        try:
            self.cursor.execute("INSERT INTO kiralamalar (musteri_id, arac_id, baslangic_tarihi, bitis_tarihi, gun_sayisi, gidilecek_yer, toplam_ucret) VALUES (%s,%s,%s,%s,%s,%s,%s)", (musteri_id, arac_id, baslangic_tarihi, bitis_tarihi, gun_sayisi, gidilecek_yer, toplam_ucret))
            self.cursor.execute("UPDATE araclar SET durum='Kirada' WHERE arac_id=%s", (arac_id,))
            self.connection.commit()
        except Error as e:
            print(f"Kira hatasi: {e}")
            self.connection.rollback()
            raise e

    def kira_listele(self):
        query = """
        SELECT k.kira_id, m.ad, m.soyad, a.marka, a.model, a.plaka, k.baslangic_tarihi, k.bitis_tarihi, k.gun_sayisi, k.gidilecek_yer, k.toplam_ucret
        FROM kiralamalar k
        JOIN musteriler m ON k.musteri_id = m.musteri_id
        JOIN araclar a ON k.arac_id = a.arac_id
        WHERE a.durum = 'Kirada' ORDER BY k.kira_id DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_musteri_by_tc(self, tc):
        query = "SELECT * FROM musteriler WHERE tc_kimlik = %s"
        self.cursor.execute(query, (tc,))
        return self.cursor.fetchone()

    def get_arac_by_id(self, arac_id):
        query = "SELECT * FROM araclar WHERE arac_id = %s"
        self.cursor.execute(query, (arac_id,))
        return self.cursor.fetchone()

    def _execute(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"SQL Hata: {e}")
            raise e
