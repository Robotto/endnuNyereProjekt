#Tager imod et spørgsmål som parameter, som er dét den spørger brugeren om.
#Kalder sig selv rekursivt indtil brugeren har indtastet en gyldig værdi som kan parses til en float.
def giverAltidEnFloat(askThisQuestion):
    tastet = input(askThisQuestion)
    try:
        return float(tastet)
    except ValueError:
        print(f"Du tastede {tastet}... Det lykkedes ikke at tolke som et tal. Prøv igen...")
        return giverAltidEnFloat(askThisQuestion) #https://media.tenor.com/C_typNW6OgEAAAAC/recursion-winnie.gif

alder = giverAltidEnFloat("Hvad er din alder?")

tallene = []
antalTal = 5
print(f"Jeg skal bruge {antalTal} tal.")
for i in range( antalTal ):
    tallene.append( giverAltidEnFloat("Stik mig et tal, bro! ") )

#de skal lægges sammen og printes
print(f"fedt. Tak for fem tal, bro.. Summen er: {sum(tallene)}")