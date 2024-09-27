telefonkatalog = [] 
fil = "telefondata.txt" #Filen hvor den settes inn og hentes fra data

def hent_personer_fra_fil(filnavn): #Henter ut personer fra filen
    with open(filnavn, 'r') as fil:
        for linje in  fil:
            person = []
            for ord in linje.split():
                person.append(ord)
            telefonkatalog.append(person)

hent_personer_fra_fil(fil)

def skriv_til_fil(filnavn): #Setter inn data
    with open (filnavn, "w") as txt_file:
        for line in telefonkatalog:
            txt_file.write(" ".join(line) + "\n")

def printMeny(): #Printer menyen
    print("------------------Telefonkatalog------------------")
    print("| 1. Legg til ny person                          |")
    print("| 2. Søk opp person, telefonnummer eller e-post  |")
    print("| 3. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge menyen: ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall): #Alternativer fra menyen
    if valgtTall == "1": #For eksempel, hvis valgt tall var 1 så skal den registrere en ny person, altså sette inn data
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            skriv_til_fil(fil)
            exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-4: ")
        utfoerMenyvalg(nyttForsoek)

def registrerPerson(): #Den registrerer en ny person
    fornavn = input("Skriv inn fornavn: ") #For eksempel her så spør den brukeren å skrive inn navn
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")
    ePost = input("Skriv inn e-post: ")

    nyRegistrering = [fornavn, etternavn, telefonnummer, ePost] #Utfører registreringen
    telefonkatalog.append(nyRegistrering)

    print("{0} {1} er registrert med telefonnummer {2} og e-post {3}" #Printer at registreringen er utført
          .format(fornavn, etternavn, telefonnummer, ePost))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

def sokPerson(): #Søker etter personen
    if not telefonkatalog: #Hvis det er ingen 
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else:
        print("1. Søk på fornavn") 
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Søk på e-post")
        print("5. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-4, eller 5 for å gå tilbake: ") #Ber brukeren om å velge hvordan de skal søke på personen
        if sokefelt == "1": #For eksempel, hvis ønsket søk er 1 så skal brukeren sette in fornavnet 
            navn = input ("Fornavn: ")
            finnPerson("fornavn", navn) #Finner fram person med det fornavnet
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3":
            tlfnummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", tlfnummer)
        elif sokefelt == "4":
            ePost = input("E-post: ")
            finnPerson("ePost", ePost)
        elif sokefelt == "5":
            printMeny()
        else:
            print("Ugyldig valg. Velg et tall mellom 1-5")
            sokPerson()

def finnPerson(typeSok, sokeTekst): #Funksjonen for å finne personen 
    har_funnet = False
    for personer in range(len(telefonkatalog)):
        fornavn = telefonkatalog[personer][0]
        etternavn = telefonkatalog[personer][1]
        telefonnummer = telefonkatalog[personer][2]
        ePost = telefonkatalog[personer][3]
        
        if typeSok == "fornavn" and har_funnet == False: #Hvis brukeren vil finne fram personen med fornavn alternativet
            if fornavn == sokeTekst: #Hvis fornavnet er registrert
                funnet=telefonkatalog[personer] 
                print("{0} {1} har telefonnummer {2} og e-post {3}" #Printer ut at angitt fornavn har etternavn ___ osv.
                    .format(funnet[0], funnet[1], funnet[2], funnet[3]))
                har_funnet = True
            elif personer >= (len(telefonkatalog)-1) :
                print("Finner ingen personer med fornavn " + sokeTekst) #Hvis fornavnet er ikke registrert

        elif typeSok == "etternavn" and har_funnet == False:
            if etternavn == sokeTekst:
                funnet=telefonkatalog[personer]
                print("{0} {1} har telefonnummer {2}, e-post: {3}"
                    .format(funnet[0], funnet[1], funnet[2], funnet[3]))
                har_funnet = True
            elif personer >= (len(telefonkatalog)-1):
                print("Finner ingen personer med etternavn " + sokeTekst)

        elif typeSok == "telefonnummer" and har_funnet == False:
            if telefonnummer == sokeTekst:
                funnet=telefonkatalog[personer]
                print("Telefonnummer {0} tilhører {1} {2}, e-post: {3}"
                    .format(funnet[2], funnet[0], funnet[1], funnet[3]))
                har_funnet = True
            elif personer >= (len(telefonkatalog)-1):
                print("Telefonnummer " + sokeTekst + " er ikke registrert. \n")

        elif typeSok == "ePost" and har_funnet == False:
            if ePost == sokeTekst:
                funnet=telefonkatalog[personer]
                print("E-post {0} tilhører {1} {2}, tlfnr: {3}"
                    .format(funnet[3], funnet[0], funnet[1], funnet[2]))
                har_funnet = True
            elif personer >= (len(telefonkatalog)-1):
                print("E-post " + sokeTekst + " er ikke registrert. /n")

printMeny()