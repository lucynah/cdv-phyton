#pierwszy plik
print("podaj swoje imie: ")
imie = input()
print("Twoje imie : "+ imie)
print("podaj wiek")
wiek = input()
print('twoj wiek: '+ wiek)

nazwisko = "kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)
ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))
x = float(x)
print(type(x))

y = 5
print(type(y))
y = y/2
print(type(y))

print(nazwisko[0:3])
print(nazwisko[-2])
print(nazwisko[-2:])