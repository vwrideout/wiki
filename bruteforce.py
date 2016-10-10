import sys
import re
import pickle

d = {}

buffer = ""

pagere = re.compile("<page>(.*?)<\/page>", re.DOTALL)
titlere = re.compile("<title>(.*?)<\/title>", re.DOTALL)
textre = re.compile("<text xml:space=\"preserve\">(.*?)<\/text>", re.DOTALL)
linkre = re.compile("\[\[(.*?)\]\]", re.DOTALL)

for line in sys.stdin:
    buffer = buffer + line
    if "</page>" in line:
        pages = pagere.findall(buffer)
        if len(pages) > 0:
            if len(pages) > 1:
                print "uhhh more than one page"
            else:
                page = pages[0]
                title = titlere.findall(page)[0].lower()
                texts = textre.findall(page)
                if len(texts) > 0:
                    d[title] = [link.split('|')[0].lower() for link in linkre.findall(texts[0])]
                else:
                    d[title] = []
            buffer = ""


with open("wikidict.pkl", "wb") as f:
    pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)

