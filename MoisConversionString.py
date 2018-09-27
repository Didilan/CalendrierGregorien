def ConvertitMoisIntEnString(Mois):  # Fonction qui convertit le mois chiffre en mois écrit
    if Mois == 1:
        MoisLettre = "Janvier"
        return MoisLettre
    elif Mois == 2:
        MoisLettre = "Février"
        return MoisLettre
    elif Mois == 3:
        MoisLettre = "Mars"
        return MoisLettre
    elif Mois == 4:
        MoisLettre = "Avril"
        return MoisLettre
    elif Mois == 5:
        MoisLettre = "Mai"
        return MoisLettre
    elif Mois == 6:
        MoisLettre = "Juin"
        return MoisLettre
    elif Mois == 7:
        MoisLettre = "Juillet"
        return MoisLettre
    elif Mois == 8:
        MoisLettre = "Août"
        return MoisLettre
    elif Mois == 9:
        MoisLettre = "Septembre"
        return MoisLettre
    elif Mois == 10:
        MoisLettre = "Octobre"
        return MoisLettre
    elif Mois == 11:
        MoisLettre = "Novembre"
        return MoisLettre
    else:
        MoisLettre = "Décembre"
        return MoisLettre

def MoisAjout(Mois):  # Fonction qui trouve la valeure à ajouter lié au mois
    if Mois == 1:
        return 0
    elif Mois == 2:
        return 3
    elif Mois == 3:
        return 3
    elif Mois == 4:
        return  6
    elif Mois == 5:
        return  1
    elif Mois == 6:
        return 4
    elif Mois == 7:
        return 6
    elif Mois == 8:
        return 2
    elif Mois == 9:
        return 5
    elif Mois == 10:
        return 0
    elif Mois == 11:
        return 3
    elif Mois == 12:
        return 5

def SiecleAjout(Année):  # Fonction qui récupère les deux premiers chiffres d'un siècle pour trouver la valeure à ajouter
    if float(str(Année)[:2]) == 16:
        return 6
    elif float(str(Année)[:2]) == 17:
        return 4
    elif float(str(Année)[:2]) == 18:
        return 2
    elif float(str(Année)[:2]) == 19:
        return 0
    elif float(str(Année)[:2]) == 20:
        return 6
    elif float(str(Année)[:2]) == 21:
        return 4

def dernierschiffres(Année):  # Fonction qui récupère les deux derniers chiffres de l'année
    return float(str(Année)[-3:]) if '.' in str(Année)[-2] else int(str(Année)[-2:])

def Bissextile(Année):  # Fonction qui vérifie si l'année est Bissextile
    bissextile = False
    if Année % 400 == 0:    # Si l'année est divisible par 400
        bissextile = True
    elif Année % 100 == 0:  # Si l'année est divisible par 100
        bissextile = False
    elif Année %4 == 0:    # Si l'année est divisible par 4
        bissextile = True
    return bissextile

def JourSemaine(AnnéeReste):  # Fonction qui convertit le reste de l'année en jour
    if AnnéeReste == 0:
        return "Dimanche"
    elif AnnéeReste == 1:
        return "Lundi"
    elif AnnéeReste == 2:
        return "Mardi"
    elif AnnéeReste == 3:
        return "Mercredi"
    elif AnnéeReste == 4:
        return "Jeudi"
    elif AnnéeReste == 5:
        return "Vendredi"
    elif AnnéeReste == 6:
        return "Samedi"