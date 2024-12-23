# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

# Hesap bilgileri
hesap = {
    "ad": " ASLI",
    "hesapNo": "606060",
    "bakiye": 10000000,
    "ekHesap": 500000
}

# Menü-fonksiyonu
def menu():
    print("\n--- Bankamatik Uygulaması ---")
    print("1. Bakiye Sorgula")
    print("2. Para Çekme")
    print("3. Para Yatırma")
    print("4. Çıkış")
    return input("yapmak istediğiniz işlemi seçin: ")

# Bakiye sorgulama fonksiyonu
def bakiye_sorgula(hesap):
    print(f"\n{hesap['ad']} - Hesap No: {hesap['hesapNo']}")
    print(f"Bakiye: {hesap['bakiye']} TL")
    print(f"Ek Hesap Limiti: {hesap['ekHesap']} TL")

# Para çekme fonksiyonu
def para_cekme(hesap):
    miktar = float(input("Çekmek istediğiniz tutarı girin: "))
    
    if miktar <= hesap['bakiye']:
        hesap['bakiye'] -= miktar
        print(f"{miktar} TL başarıyla çekildi. Güncel bakiye: {hesap['bakiye']} TL")
    else:
        toplam_bakiye = hesap['bakiye'] + hesap['ekHesap']
        if miktar <= toplam_bakiye:
            kullan_ek_hesap = input("Hesap bakiyeniz yetersiz. Ek hesabı kullanmak ister misiniz? (E/H): ").lower()
            if kullan_ek_hesap == "e":
                ek_hesap_kullanilan = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ek_hesap_kullanilan
                print(f"{miktar} TL başarıyla çekildi. Güncel ek hesap limiti: {hesap['ekHesap']} TL")
            else:
                print("İşlem iptal edildi. Yetersiz bakiye.")
        else:
            print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")

# Para yatırma fonksiyonu
def para_yatirma(hesap):
    miktar = float(input("Yatırmak istediğiniz tutarı girin: "))
    hesap['bakiye'] += miktar
    print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {hesap['bakiye']} TL")

# Ana program
def main():
    print("Bankamatik Uygulamasına Hoşgeldiniz!")
    while True:
        secim = menu()
        
        if secim == "1":
            bakiye_sorgula(hesap)
        elif secim == "2":
            para_cekme(hesap)
        elif secim == "3":
            para_yatirma(hesap)
        elif secim == "4":
            print("Çıkış yapılıyor. İyi günler dileriz!")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

# Uygulamayı çalıştır
if __name__ == "__main__":
    main()