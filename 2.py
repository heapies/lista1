print("ZADANIE NR 2")
while True:
    print(u"Wpisz literę odpowiadającą działaniu które chcesz wykonać")
    print("a - dodawanie")
    print("b - odejmowanie")
    print(u"c - mnożenie")
    print("d - dzielenie")
    wprowadzona_litera = input(": ")
    if wprowadzona_litera == "a":
        liczba1 = float(input("Podaj 1 liczbe "))
        liczba2 = float(input("Podaj 2 liczbe "))
        wynik = str(liczba1 + liczba2)
        print("Wynik dodawania to " + wynik)
    elif wprowadzona_litera == "b":
        liczba1 = float(input("Podaj 1 liczbe "))
        liczba2 = float(input("Podaj 2 liczbe "))
        wynik = str(liczba1-liczba2)
        print("Wynik odejmowania to " + wynik)
    elif wprowadzona_litera == "c":
        liczba1 = float(input("Podaj 1 liczbe "))
        liczba2 = float(input("Podaj 2 liczbe "))
        wynik = str(liczba1*liczba2)
        print("Wynik mnożenia to " + wynik)
    elif wprowadzona_litera == "d":
        liczba1 = float(input("Podaj 1 liczbe "))
        liczba2 = float(input("Podaj 2 liczbe "))
        wynik = str(liczba1/liczba2)
        print("Wynik dzielenia to " + wynik)
    else:
        print(u"wprowadziłeś znak(i) nieodpowiadające żadnemu z działań")