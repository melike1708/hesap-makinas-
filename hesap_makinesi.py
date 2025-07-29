ilkSayi = int(input("İlk sayıyı giriniz: "))
ikinciSayi = int(input("İkinci sayıyı giriniz: "))
islem = input("""Yapmak istediğiniz işlemi giriniz.
(Toplama: +, Çıkarma: -, Çarpma: x, Bölme: /): """)

if islem == "+":
    print("Sonuç: " + str(ilkSayi + ikinciSayi))

elif islem == "-":
    print("Sonuç: " + str(ilkSayi - ikinciSayi))

elif islem == "x":
    print("Sonuç: " + str(ilkSayi * ikinciSayi))

elif islem == "/":
    if ikinciSayi != 0:
        print("Sonuç: " + str(ilkSayi / ikinciSayi))
    else:
        print("Hata! Sıfıra bölme hatası.")
else:
    print("Geçersiz işlem.")