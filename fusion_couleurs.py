import matplotlib.pyplot as plt

def hex_to_rgb(hex):
    return [int(hex[i:i+2], 16) for i in (0, 2, 4)]

r = 'ff0000'
o = 'ff7f00'
y = 'ffff00'
g = '00ff00'
b = '00ffff'

n = int(input('Combien de couleurs ? '))

print('Couleurs :\nRouge : r\nOrange : o\nJaune : y\nVert : g\nBleu : b\n')

translate = {"r":r,
             "o":o,
             "y":y,
             "g":g,
             "b":b}

colors = []
for i in range(n):
    colors.append(hex_to_rgb(translate[input()]))

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

fig,ax = plt.subplots()
ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=[x / 255 for x in average_color]))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.show()