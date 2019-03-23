tekst = "Anna, paweł, TomEK"

tab = tekst.split(",")
print(tekst)
print(tab)
imie = tab[0]
print(imie)
print(type(tab))

imieDuze = imie.upper()
print(imieDuze)

imieMale = imie.lower()
print(imieMale)

zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie =""
zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = "Julia"
print("\nDane użytkownika:\nMasz na imie: "+imie)

text1 = "Jana\n"
text2 = "Nowak"
print(text1 + text2)
text1 = text1.rstrip()
print(text1 + text2)

#wyswietlanie lancuchow znakow
#wszystkie wersje Pythona
text ="%s, JAVA i %s"%("PHP", "Python")
print(text)

#nowsze wersje pythona
text = "{0}, Java i {1}".format("PHP", "Python")
print(text)
new = text.replace("PHP", "C#")
print(new)

rok = "2019"
miesiac = "marca"
dzien = "23"

# end="" nie bierze przejscia do nowej linii
print("data : ", end="")
print(dzien, miesiac, rok)