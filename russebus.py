'''

Den universelle opskrift som altid gælder 60% af tiden:

1: Hvad skal tingen kunne?
    Krav / user stories / use cases / etc
2: Flowcharts
3: Kodeskelet
    Pseudokode

'''
muligeValg = {'1': 'Indbetal', '2': 'Status', '3': 'Gem og Luk'}

def menu():
    #vis menuen -> print()?

    #vent på input
    #returner GYLDIGT valg
    print("Gyldige valg:")
    for valgNummer, valg in muligeValg.items():
        print(f"{valgNummer}: {valg}")
    valg = input("Tast et af ovenstående tal for at vælge en funktion: ")
    return valg

def valgetErGyldigt(valget):
    #match brugervalg med mulige valg
    if valget in muligeValg.keys():
        return True
    else:
        False

def indbetal():
    #spørg om navn
    #spørg om beløb - Validér INPUT!!!
    #gem
    pass

if __name__ == "__main__":
    print("Velkommen til russebusseprogrammet.me")
    valg = menu()
    print(f"du har valgt {valg}")
    if valgetErGyldigt(valg):
        switch()
        if muligeValg[valg] == 'Indbetal':
            indbetal()
        elif

    else:
        pass
