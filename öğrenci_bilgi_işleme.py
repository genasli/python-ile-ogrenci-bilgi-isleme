class Ogrenci: 

    def __init__(self, ad, soyad, ogrenci_no): 

        self.ad = ad 
        self.soyad = soyad 
        self.ogrenci_no = ogrenci_no 
        self.dersler = {} 

    def ders_kaydet(self, ders_adı, vize_notu, final_notu): 

        self.dersler[ders_adı] = {"Vize": vize_notu, "Final": final_notu} 

    def en_yuksek_notu_alan_dersler(self): 

        en_yuksek_notlar = {} 
        for ders, notlar_dict in self.dersler.items(): 

            vize_notu = notlar_dict["Vize"] 
            final_notu = notlar_dict["Final"] 
            en_yuksek_not = max(vize_notu, final_notu) 
            if en_yuksek_not not in en_yuksek_notlar: 

                en_yuksek_notlar[en_yuksek_not] = [ders] 

            else: 

                en_yuksek_notlar[en_yuksek_not].append(ders) 

        return en_yuksek_notlar 

def ogrenci_kaydet(ogrenci): 

    with open("ogrenci.txt", "a") as dosya: 

        dosya.write(f"Ad: {ogrenci.ad}\n") 
        dosya.write(f"Soyad: {ogrenci.soyad}\n") 
        dosya.write(f"Öğrenci No: {ogrenci.ogrenci_no}\n") 
        dosya.write("Ders Notları:\n") 

        for ders, notlar in ogrenci.dersler.items(): 

            dosya.write(f"{ders}: Vize - {notlar['Vize']}, Final - {notlar['Final']}\n") 

        dosya.write("\n") 

def en_yuksek_notu_alan_ogrenciler(ogrenciler): 

    en_yuksek_notlar = {} 
    for ogrenci in ogrenciler: 

        notlar = ogrenci.en_yuksek_notu_alan_dersler() 
        for notu, dersler in notlar.items(): 

            if notu not in en_yuksek_notlar: 

                en_yuksek_notlar[notu] = [(ogrenci.ad, ogrenci.soyad, dersler)] 

            else: 

                en_yuksek_notlar[notu].append((ogrenci.ad, ogrenci.soyad, dersler)) 

    return en_yuksek_notlar 

dersler = ["Matematik", "Fizik", "Kimya", "Türkçe", "İngilizce"] 
ogrenci_sayisi = int(input("Kaç öğrenci kaydı yapmak istiyorsunuz? ")) 
ogrenciler = [] 

for i in range(ogrenci_sayisi): 

    ad = input(f"{i+1}. öğrencinin adını girin: ") 
    soyad = input(f"{i+1}. öğrencinin soyadını girin: ") 
    ogrenci_no = input(f"{i+1}. öğrencinin öğrenci numarasını girin: ") 
    ogrenci = Ogrenci(ad, soyad, ogrenci_no) 

    for ders in dersler: 

        vize = float(input(f"{i+1}. öğrencinin {ders} dersi vize notunu girin: ")) 
        final = float(input(f"{i+1}. öğrencinin {ders} dersi final notunu girin: ")) 
        ogrenci.ders_kaydet(ders, vize, final) 

    ogrenciler.append(ogrenci) 

kontrol_sonuclari = en_yuksek_notu_alan_ogrenciler(ogrenciler) 
with open("kontrol.txt", "w") as dosya: 

    for notu, ogrenciler in kontrol_sonuclari.items():
        
        dosya.write(f"En Yüksek Not: {notu}\n") 
        for ogrenci in ogrenciler: 

            ad, soyad, dersler = ogrenci 
            dosya.write(f"Öğrenci: {ad} {soyad}\n") 
            dosya.write(f"Aldığı Dersler: {', '.join(dersler)}\n") 

        dosya.write("\n")
        
print("Kontrol sonuçları 'kontrol.txt' dosyasına yazıldı.") 
