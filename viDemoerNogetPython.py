from enAndenFil import *

enVariabelMedEtRelevantNavn = 6 #her er en kommentar

enFunktionFraEtAndetSted()
''' 
Her er en kommentar der fylder lidt flere linier
altså.. nu gør den.
'''
nogetTekst = 'heyyyy'
kortTekst = 'ooo'

print(nogetTekst+kortTekst)



#nu lægger vi tal sammen, med en funktion som er defineret i en anden fil:
resultatet = summa(7,35)
print(f"omgwtfbbq: {resultatet}")

etTal = 5
etAndetTal = 7
print(f"omgwtfbbq: {summa(etTal,etAndetTal)}")

nuGårDetGalt(1000)
import sys
print('Current recursion limit:',sys.getrecursionlimit())

#sys.setrecursionlimit(100000000)
#print('Current recursion limit:',sys.getrecursionlimit())
#nu dræber vi computeren:
#nuGårDetGalt(1000000000000)
print('done')