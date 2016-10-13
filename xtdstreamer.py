import xmltodict
import re
from bfs import bfs
import os

def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    FILE_LIST = []
    for path, subdirs, files in os.walk(root):
        for file in files:
            if (file.endswith('.xml') and (file.startswith("enwiki"))):
                FILE_LIST.append(file)
    return FILE_LIST


def handle_page(_, page):
    global d
    global myre
    try:
        title = page[u'title'].lower()
    except KeyError:
        print "No title found"
        return True
    try:
        article = page[u'revision'][u'text']['#text']
        d[title] = [link.split('|')[0].lower() for link in myre.findall(article)]
    except KeyError:
        d[title] = []
    return True


files = filelist("/Users/vwrideout/Documents/MSAN692/wiki")
d = {}
myre = re.compile("\[\[(.*?)\]\]")
for myfile in files:
    print "reading:", myfile
    f = open(myfile, "r")
    xml = xmltodict.parse(f.read(), item_depth=2, item_callback=handle_page)
    f.close()


while(True):
    start = raw_input("Start:").lower().decode('utf-8')
    end = raw_input("End:").lower().decode('utf-8')
    print bfs(d, start, end)