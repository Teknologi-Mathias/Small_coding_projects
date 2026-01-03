def hemmelige_tal():
    import random
    return random.randint(1, 100)
# Funktion der genererer et tilfældigt tal mellem 1 og 100

def end():
    exit()
# Funk jeg bruger i opstart_navn og gentag spil

def opstart_navn():
    name = str(input("Indtast dit navn: "))
    if name == "":
        print("Du skal indtaste et navn for at fortsætte.")
        return opstart_navn()
    elif name.lower() == "stop":
        print("Spillet er afsluttet.")
        end()
    else:
        print(f"Hej, {name}!")
        gæt_tal()


def gæt_tal():
    global Gæt_tæller  # Tilføj global erklæring ellers snakker funk ikke sammen med variablen udenfor funktionen.
    tal = valgte_tal
    try:
        gæt = int(input("Gæt et tal mellem 1 og 100: ")) 
    except ValueError:          # Brugte førhen ingen fejlhåndtering, programmet vil gå i stå med tekst (string) input.
        print("Du skal taste tal")
        return gæt_tal()
    if gæt <= 100 and gæt >= 1:
        if gæt == tal:
            print("Tillykke! Du gættede det rigtige tal: ", tal)
            gentag_spil()
        elif gæt < tal:
            print(f"Dit gæt er for lavt.: Antal gæt {Gæt_tæller}")
            Gæt_tæller += 1  
            return gæt_tal()
        elif gæt > tal:
            print(f"Dit gæt er for højt.: Antal gæt {Gæt_tæller}")
            Gæt_tæller += 1  
            return gæt_tal()
    if not gæt <= 100 and gæt >=1: # elif med et tal der der var udover 100 og 1 satte else i gang i stedet, derfor dobbelt logik. 
        if gæt == 123:
            print("Hemmelige afslutning")
            gentag_spil()
        else:
            print("Dit gæt skal være mellem 1 og 100.")
            return gæt_tal()
# Hovedprogrammet

def gentag_spil():
    global valgte_tal  # Gør valgte_tal til en global variabel så vi kan opdatere den igennem funktionen 
    valg = str(input("Vil du spille igen? (ja/nej): "))
    if valg == "Ja" or valg == "ja":
        valgte_tal = hemmelige_tal()  # Opdaterer valgte_tal med et nyt hemmeligt tal
        gæt_tal()
    else:
        print("Tak for spillet! Farvel.")
        end()


valgte_tal = hemmelige_tal() # Gemmer det hemmelige tal i en variabel, så return i def gæt_tal ikke vælger et nyt tal hver gang man gætter forkert
Gæt_tæller = 1

#Koden starter her 
print("Velkommen til gæt et tal spillet!")
opstart_navn() 
