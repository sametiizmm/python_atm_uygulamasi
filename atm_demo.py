SametHesap={
    "ad": "Samet Çakmak",
    "hesapNo": "14531453",
    "bakiye": 5000,
    "Avans": 2500
}
SemihHesap={
    "ad": "Semih Çakmak",
    "hesapNo": "58452558",
    "bakiye": 7000,
    "Avans": 3600
}
AhmetHesap={
    "ad": "Ahmet Çakmak",
    "hesapNo": "34585834",
    "bakiye": 9000,
    "Avans": 4500
}


def ParaÇek(hesap,miktar):
    print(f"Merhaba {hesap['ad'] }")

    if (hesap['bakiye']>= miktar):
        kalan=hesap['bakiye']-miktar
        print(f"Paranızı Alabilirsiniz. Güncel bakiyeniz {kalan}, Ek hesap bakiyeniz: {hesap['Avans']}")
    else:
        toplam= (hesap['Avans'] + hesap['bakiye'])
        if toplam >= miktar :
            Avanskullanımı= input("Avans kullanmak istermisiniz (Y/N): ")
            if Avanskullanımı == "Y"  :
                ekHesaptankullanılacakmiktar= miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['Avans']-=ekHesaptankullanılacakmiktar
                print(f"Paranızı Alabilirsiniz. Güncel bakiyeniz: {hesap['bakiye']}, Ek hesap bakiyeniz: {hesap['Avans']}")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda, {hesap['bakiye']} TL bakiye bulunmaktadır.")
        else:
            print("Üzgünüz..! Bakiye yetersiz.")


ParaÇek(SametHesap,int(input("Çekmek istediğiniz tutar: ")))

