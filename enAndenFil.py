print("nu har vi importeret en anden fil") #dårlig stil at køre kode uden at blive spurgt

def enFunktionFraEtAndetSted():
    print('det virker')

def summa(alpha, Δ):
    return alpha+Δ


def nuGårDetGalt(recursionCount):
    #print(recursionCount)
    if recursionCount==0:
        return 0
    else:
        return nuGårDetGalt(recursionCount-1)
