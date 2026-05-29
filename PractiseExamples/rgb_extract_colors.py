import colorgram
colors = colorgram.extract("godi.jpg",10)

for color in colors:
    rgb = color.rgb
    print(rgb.r, rgb.g, rgb.b)