# class Mekteb:

#     sinif = "Telebe"
#     sinif = "Mellim"

#     def __init__ (self, ad, soyad, ixtisas, yas):
#         self.ad = ad
#         self.soyad = soyad
#         self.ixtisas = ixtisas
#         self.yas = yas
#     def kurs(self, kurs=False):
#         if kurs==True:
#             kurs = "III-cu kurs"
#             return kurs
#         else:
#             return (f"")


# Telebe = Mekteb("Huseyn","Abbasov","Iqtisadiyyat", 24  )
# Telebe1 = Mekteb("Eli","Orucov","Maliyye", 18  )
# Telebe2 = Mekteb("Qalib","Memmedov","İnformasiya texnologiyalari", 19  )
# Telebe3 = Mekteb("Xelil","Xelilov","Biznesin idare edilmesi", 23  )
# Telebe4 = Mekteb("Behruz","Eliyev","Riyaziyyat", 22  )
# Telebe5 = Mekteb("Vurgun","Abbasov","Muhasibat ucotu", 20  )
# Telebe6 = Mekteb("Elnur","Cabbarov","Maliyye", 24  )
# Mellim = Mekteb("Hormet", "Hemidov", "Iqtisadiyyat", 23)
# Mellim1 = Mekteb("Salman", "Memmedli", "Maliyye", 30)
# Mellim2 = Mekteb("Vahide", "Aslanova", "İnformasiya texnologiyalari", 27)
# Mellim3 = Mekteb("Esger", "Abdullayev", "Maliyye", 41)
# print(f"\n{Telebe.ad} {Telebe.soyad} {Telebe.ixtisas} ixtisasının {Telebe.kurs(True)} tələbəsidir. {Mellim.ad} {Mellim.soyad}-un dərsindədir.\n")
# print(f"{Telebe1.ad} {Telebe1.soyad} {Telebe1.ixtisas} ixtisasının {Telebe1.kurs(False)} tələbəsidir. {Mellim1.ad} {Mellim1.soyad}-un dərsindədir.\n")
# print(f"{Telebe2.ad} {Telebe2.soyad} {Telebe2.ixtisas} ixtisasının {Telebe2.kurs(False)} tələbəsidir. {Mellim2.ad} {Mellim2.soyad}-un dərsindədir.\n")
# print(f"{Telebe3.ad} {Telebe3.soyad} {Telebe3.ixtisas} ixtisasının {Telebe3.kurs(True)} tələbəsidir. {Mellim3.ad} {Mellim3.soyad}-un dərsindədir.\n")
# print(f"{Telebe4.ad} {Telebe4.soyad} {Telebe4.ixtisas} ixtisasının {Telebe4.kurs(True)} tələbəsidir. {Mellim.ad} {Mellim.soyad}-un dərsindədir.\n")
# print(f"{Telebe5.ad} {Telebe5.soyad} {Telebe5.ixtisas} ixtisasının {Telebe5.kurs(False)} tələbəsidir. {Mellim1.ad} {Mellim1.soyad}-un dərsindədir.\n")
# print(f"{Telebe6.ad} {Telebe6.soyad} {Telebe6.ixtisas} ixtisasının {Telebe6.kurs(True)} tələbəsidir. {Mellim2.ad} {Mellim2.soyad}-un dərsindədir.")


# class Yirtici:

#     sinif = "Heyvan"

#     def __init__(self, ad, yas, novu):
#         self.ad = ad
#         self.yas = yas
#         self.novu = novu


# Heyvan = Yirtici("Aslan", 4, "vəhşi")


# class Memeliler:

#     sinif = "Qus"

#     def __init__(self, ad, yas, novu):
#         self.ad = ad
#         self.yas = yas
#         self.novu = novu


# Qus = Memeliler("Qartal", 5, "təhlükəli")

# print(f"\n{Qus.ad} cox {Qus.novu} qusdur, bala {Heyvan.ad}-ni bele caynaqlari arasina ala biler.\n")
# print(f"{Qus.yas} yasindaki {Qus.ad} {Heyvan.yas} yasindaki {Heyvan.novu} {Heyvan.ad}-ni qacirda bilmez...")


# class Mektebli:

#     sinif = "Sagird"
    
#     def __init__(self, ad, yas):
#         self.ad = ad
#         self.yas = yas 
    
#     def oxuma(self, oxuma_bilme = False):
#         if oxuma_bilme ==True:
#             return(f"bilir")
#         else:
#             return(f"bilmir")                
        
# Sagird = Mektebli("Hesen", 7)
# Sagird1 = Mektebli("Aydan", 3)

# print(f"{Sagird.ad}in {Sagird.yas} yasi var. O kitab oxuya {Sagird.oxuma(oxuma_bilme=True)}")
# print(f"{Sagird1.ad}in {Sagird1.yas} yasi var. O kitab oxuya {Sagird1.oxuma(oxuma_bilme=False)}")
    
