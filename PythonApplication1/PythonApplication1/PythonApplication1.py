
hesap=0
birinciDeger=int(input("Retorant�m�za Ho�geld�n\n1-Men�\n2-��k��\nL�tfen Se�imini Yap\n"))

while True:
    if birinciDeger == 1:
        menu = ["1-Yemekler", "2-Corbalar", "3-Tatl�lar", "4-Salatlar"]
        for m in menu:
            print(m)
        ikinciDeger = int(input("L�tfen Se�imini Yap\n"))
        if ikinciDeger == 1:
            yemekler = ["1-Pide: 30tl", "2-Mant�: 40tl", "3-Sarma: 60tl", "4-�i�er: 50tl", "5-K�fte: 60tl"]
            for y in yemekler:
                print(y)
            ucuncuDeger = int(input("L�tfen Seciminizi Yapin:\n"))
            if ucuncuDeger == 1:
                print("Seciminiz:", yemekler[0])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 2:
                print("Seciminiz:", yemekler[1])
                hesap = hesap + 40
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 3:
                print("Seciminiz:", yemekler[2])
                hesap = hesap + 60
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 4:
                print("Seciminiz:", yemekler[3])
                hesap = hesap + 50
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 5:
                print("Seciminiz:", yemekler[4])
                hesap = hesap + 60
                print("toplam hesabiniz:", hesap)
            else:
                print("Hatal� giri�")
        elif ikinciDeger == 2:
            corbalar = ["1-Merco: 30tl", "2-Kello: 30tl", "3-Yaylo: 30tl", "4-Manto: 30tl", "5-Tavo: 30tl"]
            for c in corbalar:
                print(c)
            ucuncuDeger = int(input("L�tfen Seciminizi Yapin:\n"))
            if ucuncuDeger == 1:
                print("Seciminiz:", corbalar[0])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 2:
                print("Seciminiz:", corbalar[1])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 3:
                print("Seciminiz:", corbalar[2])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 4:
                print("Seciminiz:", corbalar[3])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 5:
                print("Seciminiz:", corbalar[4])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            else:
                print("Hatal� giri�")
        elif ikinciDeger == 3:
            tatlilar = ["1-baklava: 30tl", "2-kazandibi: 40tl", "3-sutlac: 50tl", "4-kabak: 40tl", "5-kunefe: 50tl"]
            for t in tatlilar:
                print(t)
            ucuncuDeger = int(input("L�tfen Seciminizi Yapin:\n"))
            if ucuncuDeger == 1:
                print("Seciminiz:", tatlilar[0])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 2:
                print("Seciminiz:", tatlilar[1])
                hesap = hesap + 40
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 3:
                print("Seciminiz:", tatlilar[2])
                hesap = hesap + 50
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 4:
                print("Seciminiz:", tatlilar[3])
                hesap = hesap + 40
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 5:
                print("Seciminiz:", tatlilar[4])
                hesap = hesap + 50
                print("toplam hesabiniz:", hesap)
            else:
                print("Hatal� giri�")
        elif ikinciDeger == 4:
            salata = ["1-coban: 30tl", "2-mevs�m: 30tl", "3-rus: 30tl", "4-sezar: 30tl", "5-gavurda�i: 30tl"]
            for s in salata:
                print(s)
            ucuncuDeger = int(input("L�tfen Seciminizi Yapin:\n"))
            if ucuncuDeger == 1:
                print("Seciminiz:", salata[0])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 2:
                print("Seciminiz:", salata[1])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 3:
                print("Seciminiz:", salata[2])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            elif ucuncuDeger == 4:
                print("Seciminiz:", salata[3])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)

            elif ucuncuDeger == 5:
                print("Seciminiz:", salata[4])
                hesap = hesap + 30
                print("toplam hesabiniz:", hesap)
            else:
                print("Hatal� giri�")
        else:
            print("Hatal� g�r�s")
    elif birinciDeger == 0:
        print("��k��l Yapt�n�z Gene Bekler�z")
    else:
        print("HATALI�G�R���")



       
