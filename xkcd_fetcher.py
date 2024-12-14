import requests as req
import os, bs4, json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

url = 'https://xkcd.com/'

os.makedirs('xkcd',exist_ok=True)

res = req.get("https://xkcd.com/info.0.json")
comic_details = json.loads(res.text)

print(comic_details.get("img"))
res = req.get(comic_details.get("img"))

plt.xticks([])  
plt.yticks([])
plt.xlabel("\n" + comic_details.get("alt"), wrap=True)
img = mpimg.imread('xkcd/metar.png')
imgplot = plt.imshow(img)
plt.show()
