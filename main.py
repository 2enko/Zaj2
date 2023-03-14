# Zad1

a = "Python 2023"
b = "Python 2023"
c = "Java 11"

print(a == b)
print(b == c)
print(type(a), type(b), type(c))
print(hex(id(a)), hex(id(b)), hex(id(c)))

# Zad2

a = input("Podaj pierwszą liczbę:\n")
b = input("Podaj drguą liczbę:\n")
c = input("Podaj operator:\n")

if c == "/":
    print(int(a) / int(b))
elif c == "*":
    print((int(a) * int(b)))
elif c == "+":
    print((int(a) + int(b)))
elif c == "-":
    print((int(a) - int(b)))

# Zad3

pytania = "0.Podaj swoje imię oraz nazwisko:\n;" \
          "1.Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n;2.W jakich okolicznościach czytasz " \
          "książki najczęsciej?\n;3.Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego " \
          "wyboru?\n;4.Po książki w jakiej formie sięgasz najczęściej?\n;5.Ile książek czytasz średnio w ciągu " \
          "roku?\n;6.Jak często średnio czytasz książki?\n;7.Po jakie gatunki książek sięgasz najczęściej?\n"

odp = ";" \
      "\na)oglądanie telewizji/filmów/seriali\nb)czytanie książek/czasopism\nc)słuchanie muzyki\n;" \
      "\na)podczas podróży\nb)w czasie wolnym (po pracy, na urlopie) \nc)podczas pracy/nauki (to ich element)\n;" \
      "\na)chęć poszerzenia wiedzy\nb)czytanie mnie relaksuje/odpręża\nc)fakt, że czytanie jest modne\n;" \
      "\na)papierowej (tradycyjnej)\nb)e-booki (książki elektroniczne) na komputerze\nc)e-booki na " \
      "tablecie/telefonie\n;" \
      "\na)0\nb)żadnej w całości - jedynie fragmenty\nc)1\n;" \
      "\na)codziennie\nb)raz w tygodniu\nc)raz w miesiącu\n;" \
      "\na)kryminały/thrillery\nb)romanse\nc)psychologiczne\n;"

a = pytania.split(";")
b = odp.split(";")
listaOdp = []

print("Wybierz swoją odpowiedź poprzez wpisanie jej\n")

for x in range(len(a)):
    print(a[x], b[x])
    odp = input()
    listaOdp.append(odp)

print("\nTwoje odpowiedźi na pytania:\n")

for x in range(len(a)):
    print(a[x], listaOdp[x])
