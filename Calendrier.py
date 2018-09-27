from MoisConversionString import *  # Import de toutes les fonctions
date = input("Entrez une date valide : JJ/MM/AAAA : ")  # Saisie d'une Date

if "/" in date :    # Verification Validité Format
    Jour,Mois,Année = date.split("/")
else:   # Réécriture Date
    date = input("Entrez une date valide : JJ/MM/AAAA")
    if "/" in date:  # Verification Validité Format
        Jour, Mois, Année = date.split("/")
    else:  # Réécriture Date
        date = input("Entrez une date valide : JJ/MM/AAAA")

Jour = int(Jour)  # Conversion Int
Mois = int(Mois)
Année = int(Année)

if Année < 1582:  # Verification Validité Calcul
    if Mois < 10:
        MoisLettre = ConvertitMoisIntEnString(Mois)
        print("La date que vous avez entrer correspond au ", Jour, "", MoisLettre, "", Année, " car ces méthodes de calcul ne permettent pas de calculer pour des dates inférieures au 1 er Novembre 1582")

else:   # Si Methode Valide alors
    AnnéeDeuxChiffres = dernierschiffres(Année)  # Récupération des deux derniers chiffres
    UnQuartAnnée = AnnéeDeuxChiffres // 4  # Division du quart de l'année
    AnnéeDeuxChiffres += UnQuartAnnée   # Ajout du Quart de l'année
    AnnéeDeuxChiffres += Jour      # Ajout du Jour à l'Année
    AjoutMois = MoisAjout(Mois)    # Utilisation de la fonction MoisAjout pour récupérer la valeur correspondante au mois
    AnnéeDeuxChiffres += AjoutMois  # Ajout de la valeure correspondante au mois

    if Bissextile(Année) == True and Mois <= 2:  # Vérification Année Bissextile
        AnnéeDeuxChiffres -= 1  # Si l'Année est Bissextile on enlève 1
    Siecle = SiecleAjout(Année)    # Utilisation de la fonction SiecleAjout
    AnnéeDeuxChiffres += Siecle     # Ajout de la valeure correspondante au siècle
    AnnéeReste = AnnéeDeuxChiffres % 7    # Modulo de l'année finale poure récup le reste

    JourSemaine = JourSemaine(AnnéeReste)   # Utilisation Fonction JourSemaine
    print("Le jour de la semaine correspondant à une date donnée est : ", JourSemaine)
