klassen = ["Abdiwahid","Amanda","Andronikos","Atle","Burak","Buster","Christoffer","Daniel","Frederik","Sophia","Izzet","Jeppe","Johannes","Karl","Kasper","Kim","Kristine","Mads","Magnus","Malte","Marc","Mathias","Muhsin","Nikolaj","Phillip","Rune","Sebastian","Thorbjørn","Zakaria"]

sum_af_bogstaver = 0
for elev in klassen:
    sum_af_bogstaver+=len(elev)
    print(f"{elev} hedder {elev}, og har {len(elev)} bogstaver i sit navn")

print(f"\n\nDer er {sum_af_bogstaver} bogstaver i klassens fornavne\n\n")

gruppe0 = ["Abdiwahid", 'Izzet', 'Burak']
gruppe1 = ["Kristine", 'Magnus', 'Amanda']
gruppe2 = ["Andronikos", 'Nikolaj', 'Johannes']
gruppe3 = ['Atle', 'Christoffer', 'Thorbjørn']
gruppe4 = ['Buster', 'Rune', 'Daniel']
gruppe5 = ['Frederik', 'Sebastian', 'Muhsin', 'Zakaria']
gruppe6 = ['Marc', 'Kasper', 'Mads']
gruppe7 = ['Mathias', 'Kim', 'Malte']
gruppe8 = ['Jeppe', 'Phillip', 'Karl']



grupper = [ gruppe0,gruppe1,gruppe2,gruppe3,gruppe4,gruppe5,gruppe6,gruppe7,gruppe8]

summe=0
for gruppe in grupper:
    count=0
    for medlem in gruppe:
        count+=1
    summe+=count
    print(gruppe,':',count)

delta = len(klassen)-summe

#TODO: Does not handle Overbooked classmates (if someone is in more than one group)
#TODO: FØLG DIT EGET FLOWCHART NÅR DU SKRIVER KODE!
#TODO: Genau!

#TODO: This is of course implemented neatly in python already: https://www.geeksforgeeks.org/python-check-if-element-exists-in-list-of-lists/
if delta != 0:
    print(f"Error: Mismatch between counted group members and class members! Members in groups: {summe}, Classmates: {len(klassen)}, Delta: {delta}")
    for elev in klassen:
        er_i_en_gruppe = False
        for gruppe in grupper:
            if elev in gruppe:
                er_i_en_gruppe=True
        if not er_i_en_gruppe:
            print(f"{elev} is not in any group!")


import random
randomGruppe = random.choice(grupper)
while(len(randomGruppe)>3):
    randomGruppe = random.choice(grupper)