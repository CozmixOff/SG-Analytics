
import csv
vagues = []
genres = []
ages = []
zone_geos = []
regions = []
departements = []
taille_commune1s = []
taille_commune2s = []
situ_pros = []
CSPs = []

with open('donnees_completes.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")
    next(csvreader)
    for row in csvreader:
        vague, genre, age, zone_geo, region, departement, none1, taille_commune1, taille_commune2, situ_pro, CSP = row[:11]
        vagues.append(vague)
        genres.append(genre)
        ages.append(age)
        zone_geos.append(zone_geo)
        regions.append(region)
        departements.append(departement)
        taille_commune1s.append(taille_commune1)
        taille_commune2s.append(taille_commune2)
        situ_pros.append(situ_pro)
        CSPs.append(CSP)
listekey = ["vagues", "genres", "ages", "zone geos", "regions", "departements", "taille_commune1", "taille commune2", "situ_pro", "CSP"]
listevalue = [vagues, genres, ages, zone_geos, regions, departements, taille_commune1s, taille_commune2s, situ_pros, CSPs]
info_perso = {listekey[i]: listevalue[i] for i in range(len(listekey))}

def info_personne(n):
    pers = {}
    for i in info_perso:
        pers[i] = info_perso[i][n]
    return pers

def personne(n):
    personne = reponse_personne(n)
    personne['personnel'] = info_personne(n)
    personne['couleur_moyenne'] = couleur_moyenne(personne)
    return personne

def typeur (L):
    typevalue_L = []
    for i in range(len(L)):
        if L[i] not in typevalue_L:
            typevalue_L.append(L[i])
    return typevalue_L

def transformateur (L):
    typevalue_L = typeur(L)
    transfo_L = []
    for i in L: 
        x = typevalue_L.index(i)
        transfo_L.append(x)
    return transfo_L


typevalue_vagues = typeur(vagues)
typevalue_genres = typeur(genres)
typevalue_ages = typeur(ages)
typevalue_zone_geos = typeur(zone_geos)
typevalue_regions = typeur(regions)
typevalue_departements = typeur(departements)
typevalue_taille_commune1s = typeur(taille_commune1s)
typevalue_taille_commune2s = typeur(taille_commune2s)
typevalue_situ_pros = typeur(situ_pros)
typevalue_CSPs = typeur(CSPs)
"""


transfo_vagues = transformateur(vagues)
transfo_genres = transformateur(genres)
transfo_ages = transformateur(ages)
transfo_zone_geos = transformateur(zone_geos)
transfo_regions = transformateur(regions)
transfo_departements = transformateur(departements)
transfo_taille_commune1s = transformateur(taille_commune1s)
transfo_taille_commune2s = transformateur(taille_commune2s)
transfo_situ_pros = transformateur(situ_pros)
transfo_CSPs = transformateur(CSPs)

"""
def reponse_personne(n):
    dictio = {}
    return dictio
def couleur_moyenne(reponse_personne):
    dico = {}
    return dico

print (typevalue_vagues)
print (transformateur(typevalue_vagues))