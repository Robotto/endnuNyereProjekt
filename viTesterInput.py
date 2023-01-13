navnet = input('skriv dit navn: ')
print('hej', navnet)

try:
    etTal = int(input('Giv mig et tal: '))
except:
    print("det virkede ikke")
    exit('ID10T')

etAndetTal = int(input('Giv mig et andet tal: '))

summen = etTal+etAndetTal
print('Summen af de to tal er: ', summen, ',', navnet, '.. Vidste du ikke det?')

print()11