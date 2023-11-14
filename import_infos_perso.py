import csv
import time
import random

start_time = time.time()

print("[1/4] - "+str(round(int(time.time()-start_time),3))+" | Importing the file")

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
print(info_perso)
    