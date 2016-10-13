import xmltodict
import re
from bfs import bfs

d = {}
myre = re.compile("\[\[(.*?)\]\]")
f = open("enwiki-20160920-pages-meta-current1.xml", "r")
xml = xmltodict.parse(f.read())
for page in xml[u'mediawiki'][u'page']:
    title = page[u'title'].lower()
    article = page[u'revision'][u'text']['#text']
    d[title] = [link.split('|')[0].lower() for link in myre.findall(article)]
f.close()


while(True):
    start = raw_input("Start:").lower().decode('utf-8')
    end = raw_input("End:").lower().decode('utf-8')
    print bfs(d, start, end)