def hex_to_rgb(hex):
    return [int(hex[i:i+2], 16) for i in (0, 2, 4)]
r = 'ff0000'
o = 'ff7f00'
y = 'ffff00'
g = '00ff00'
b = '00ffff'
reponse = {"question 1" : ["reponse 1", "reponse 2", "reponse 3", "reponse 4", "reponse 5"], "question 2" : ["reponse 6", "reponse 7", "reponse 8", "reponse 9", "reponse 10"], "question 3" : ["reponse 11", "reponse 12", "reponse 13", "reponse 14", "reponse 15"]}
reponse_coloree = {"question 1" : [r, o, y, g, b], "question 2" : [r, o, y, g, b], "question 3" : [r, o, y, g, b]}

exemple_personnage = {"question 1" : "reponse 1", "question 2" : "reponse 6" , "question 3" : "reponse 11"}
exemple_personnage2 = {"question 1" : "reponse 2", "question 2" : "reponse 7", "question 3" : "reponse 12"}
exemple_personnage3 = {"question 1" : "reponse 3", "question 2" : "reponse 8", "question 3" : "reponse 13"}

def couleur_personnage(personnage):
    couleur_perso = []
    for i in personnage:
        couleur_perso.append(reponse_coloree[i][reponse[i].index(personnage[i])])
    return couleur_perso

def couleur_moyenne(exemple):
    colors = []
    couleur_perso = couleur_personnage(exemple)
    n = len(couleur_perso)
    for i in range(n):
        colors.append(hex_to_rgb(couleur_perso[i]))
    average_red = 0
    average_green = 0
    average_blue = 0

    for i in range(n):
        average_red += colors[i][0]
    average_red /= n

    for i in range(n):
        average_green += colors[i][1]
    average_green /= n

    for i in range(n):
        average_blue += colors[i][2]
    average_blue /= n

    average_color = [round(average_red),round(average_green),round(average_blue)]
    return average_color