from turtle import *
def bruņurupuča_vadība(dar, vērt):
    dar = dar.upper()
    if dar == "P":
        forward(vērt)
    elif dar == "A":
        backward(vērt)
    elif dar == "L":
        right(vērt)
    elif dar == "K":
        left(vērt)
    elif dar == "N":
        penup()
    elif dar == "I":
        pendown()
    elif dar == "J":
        reset()
    else:
        print("Nezināma komanda")


def virknes_tulkotājs(programma):
    kmd_saraksts = programma.split('-')
    for komanda in kmd_saraksts:
        kmd_garums = len(komanda)
        if kmd_garums == 0:
            continue
        kmd_tips = komanda[0]
        sk = 0
        if kmd_garums > 1:
            sk_virkne = komanda[1:]
            sk = int(sk_virkne)
        print(komanda, ":", kmd_tips, sk)
        bruņurupuča_vadība(kmd_tips, sk)

#virknes_tulkotājs('J-K90-P100-L45-P70-L90-P70-L45-P100-L90-P100')

instrukcijas = """"Ievadi programmu bruņurupucim!
Piemēram, P100-L45-N-P100-K45-I-P100-L90-A50.
J = Jauns zīmējums
N/I = Nolikt/Ieslēgt zīmuli
P100 = Uz priekšu 100 soļus
A50 = Atpakaļ 50 soļus
L90 = Pagriezties par 90 grādiem pa labi
K45 = Pagriezties par 45 grādiem pa kreisi"""
ekrāns = getscreen()
while True:
    t_programma = ekrāns.textinput('Zīmēšanas rīks', instrukcijas)
    print(t_programma)
    if t_programma == None or t_programma.upper() == "BEIGT":
        break
    virknes_tulkotājs(t_programma)

#Examples
# Māja
# J-K90-P100-L45-P70-L90-P70-L45-P100-L90-P100
# Māja ar logu
# J-K90-P100-L45-P70-L90-P70-L45-P100-L90-P100-A10-N-L90-P10-I-P30-L90-P30-L90-P30
# Nezināma eksistence
# J-P10-K90-P200-K90-P50-L60-P30-K120-P30-L60-P40-L60-P30-K120-P30-L60-P50-K90-P200-K90-P100-K90-N-P150-K90-P20-I-P30-K90-P30-K90-P30-K90-P30-L90-N-P40-I-P30-L90-P30-L90-P30-L90-P30-K180-N-P60-L90-I-P40-K120-P40-K120-P40