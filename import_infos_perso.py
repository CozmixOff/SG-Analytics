
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

typevalue_vagues = []
for i in range(len(vagues)):
    if vagues[i] not in typevalue_vagues:
        typevalue_vagues.append(vagues[i])

typevalue_genres = []
for i in range(len(genres)):
    if (genres[i]) not in typevalue_genres:
        typevalue_genres.append(genres[i])

typevalue_ages = []
for i in range(len(ages)):
    if (ages[i]) not in typevalue_ages:
        typevalue_ages.append(ages[i])

typevalue_zone_geos = []
for i in range(len(zone_geos)):
    if (zone_geos[i]) not in typevalue_zone_geos:
        typevalue_zone_geos.append(zone_geos[i])

typevalue_regions = []
for i in range(len(regions)):
    if (regions[i]) not in typevalue_regions:
        typevalue_regions.append(regions[i])

typevalue_departements = []
for i in range(len(departements)):
    if (departements[i]) not in typevalue_departements:
        typevalue_departements.append(departements[i])

typevalue_taille_commune1s = []
for i in range(len(taille_commune1s)):
    if (taille_commune1s[i]) not in typevalue_taille_commune1s:
        typevalue_taille_commune1s.append(taille_commune1s[i])

typevalue_taille_commune2s = []
for i in range(len(taille_commune2s)):
    if (taille_commune2s[i]) not in typevalue_taille_commune2s:
        typevalue_taille_commune2s.append(taille_commune2s[i])

typevalue_situ_pros = []
for i in range(len(situ_pros)):
    if (situ_pros[i]) not in typevalue_situ_pros:
        typevalue_situ_pros.append(situ_pros[i])

typevalue_CSPs = []
for i in range(len(CSPs)):
    if (CSPs[i]) not in typevalue_CSPs:
        typevalue_CSPs.append(CSPs[i])

def transformateur (L):
    code = []
        

