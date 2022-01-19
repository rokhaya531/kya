import numpy as np
import os

chemin="wireshark.txt"
try:
    #with open("evenementSAE_15.ics", encoding="utf8") as fh:
    with open(chemin, encoding="utf8") as fh:
        res=fh.read()
except:
    print("Le fichier n'existe pas %s", os.path.abspath(chemin))
ress=res.split('\n')
tableau_evenements=np.array([])


SYN ="[S],"
POUSSER = "[P.],"
RST = "[R],"



print(ress[5])
print("\n")
for event in ress:
    # Initialisation chaine de carcatere
    if event.startswith('11:42'):
        texte=event.split()
        if texte[5] == "Flags":
            evenement='temps : '+texte[0]+';'+' Adresse Ip source : '+texte[2]+';'+' Adresse IP destinataire : '+texte[4]+';'+' flag : '+texte[6]+';'
            if texte[6] == SYN:
                evenement_3 = 'Protocole :' +texte[len(texte)-1]+';'
                evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Taille de la fenêtre : '+texte[10]+';'+' Longueur du paquet : '+texte[len(texte)-2]+';'
            if texte[6] == POUSSER:
                evenement_3 = ' '
                evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Numéro accusé de réception : '+texte[10]+';'
            if texte[6] == "[.],":
                evenement_2 = 'Numéro accusé de réception : '+texte[8]+';'+' Taille de la fenêtre : '+texte[10]+';'
                evenement_3 = ' Longueur du paquet : '+texte[12]+';'
            if texte[6] == "[S.],":
                evenement_2 = 'Numéro de séquence : '+texte[8]+';'+' Numéro accusé de réception : '+texte[10]+';'+' Taille de la fenêtre : '+texte[12]+';'
                evenement_3 = ' Longueur du paquet : '+texte[len(texte)-1]+';'
            if texte[6] == RST:
                evenement_2 = ' '
                evenement_3 = 'RST'
            with open('fichier1.csv','a') as f:
                f.write(f"{evenement},{evenement_2},{evenement_3}\n")
f.close()
fh.close()
print('reussit')