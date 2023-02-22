def giverAltidEnFloat():
    tastet = input("giv mig et tal")
    try:
        return float(tastet)
    except ValueError:
        print("det virkede ikke.. prøv igen...")
        return giverAltidEnFloat()


tallene = []
antalTal = 5
for i in range( antalTal ):
    tallene.append( giverAltidEnFloat() )

#de skal lægges sammen og printes
print(f"fedt. Tak for fem tal.. Summen er: {sum(tallene)}")