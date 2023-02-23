"""

Den universelle opskrift som altid gælder 60% af tiden:

1: Hvad skal tingen kunne?
    Krav / user stories / use cases / etc
2: Flowcharts
3: Kodeskelet
    Pseudokode

"""
import pickle #Bruges til at gemme og indlæse data til/fra disk.

muligeValg = {'1': 'Indbetal', '2': 'Status', '3': 'Gem og Luk'}

def printMenu():
    #vis menuen -> print()?
    #vent på input
    #returner valg

    print("\tGyldige valg:")
    for valgNummer, valg in muligeValg.items():
        print(f"\t\t{valgNummer}: {valg}")
    valg = input("\tTast et af ovenstående tal for at vælge en funktion: ")
    return valg

def valgetErGyldigt(valget):
    #match brugervalg med mulige valg
    if valget in muligeValg.keys():
        return True
    else:
        return False

def loadSavedDataFromFile(filename):
    indbetalinger = {}

    #load pickled dict from disc to memory:
    try:
        with open(filename, 'rb') as infile:
            indbetalinger = pickle.load(infile)
    except FileNotFoundError:
        print(f"\t\tADVARSEL: KUNNE IKKE FINDE FILEN: \"{filename}\"!")

    #Tjek om der kom data ind fra filen:
    if(len(indbetalinger)<1):
        print(f"\t\tADVARSEL: KUNNE IKKE FINDE DATA I FILEN: \"{filename}\"!")

    return indbetalinger
def indbetal():
    #spørg om navn
    #spørg om beløb - Validér INPUT!!!
    #gem
    print("\t\tRan: Indbetal")
    return 0
def status():
    #vis indbetalinger indtil nu.
    print("\t\tRan: status")
    print()
    return 0

def saveToFile(data,filename):
    print("\t\tSaving and Quitting...")
    #save data by pickling the dict:
    try:
        with open(filename, 'wb') as outfile:
            pickle.dump(data,outfile)
        return True
    except FileNotFoundError:
        print(f"\t\tADVARSEL: KUNNE IKKE GEMME TIL FILEN: \"{filename}\"!")
        return False


if __name__ == "__main__":
    print("Velkommen til russebusseprogrammet")

    ##Call load to get data from disc:
    indbetalinger = loadSavedDataFromFile("2p.pickle")

    while True:
        valg = printMenu()
        print(f"\n\nDu har valgt {valg}")
        if valgetErGyldigt(valg):
            match muligeValg[valg]:
                case 'Indbetal':
                    indbetal()
                case 'Status':
                    status()
                case 'Gem og Luk':
                    saveToFile("2p.pickle")
                    exit("Bye!")

        else:
            print("Det kan man ikke vælge. Prøv igen. :)")
