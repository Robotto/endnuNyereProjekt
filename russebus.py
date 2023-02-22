'''

Den universelle opskrift som altid gælder 60% af tiden:

1: Hvad skal tingen kunne?
    Krav / user stories / use cases / etc
2: Flowcharts
3: Kodeskelet
    Pseudokode

'''

def menu():
    #vis menuen -> print()?

    #vent på input
    #returner GYLDIGT valg
    valg = input("Vælg en funktion")
    return valg

def tjekOmMenuValgetErGyldigt(valget):
    # definér mulige valg
    muligeValg = {'1':'Indbetal','2':'Status','3':'Gem og Luk'}

    #match brugervalg med mulige valg
    if valget not in muligeValg.keys():
        print("ugyldigt valg... prøv igen")
        menu()
        du har valgt muligeValg[valget]
    return valget
    #ingen match? -> spørg igen , vær god ved brugeren
    #returnér valget
    pass

def indbetal():
    #spørg om navn
    #spørg om beløb - Validér INPUT!!!
    #gem
    pass

print("Velkommen til russebusseprogrammet.me")
valg = menu()
print(f"du har valgt {valg}")