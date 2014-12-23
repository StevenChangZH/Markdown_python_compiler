# ------------------------------------------------------------
# plyScripts_2_7.py
#
# Some scripts to provide better codes integration
# version 6.0 for Markdown_python_compiler
# NOTICE: this script only used for python version under 3.3
# ------------------------------------------------------------
#-*-coding:utf-8-*- 
import re
import base64
import urllib2

# DO NOT call those methods directly
def getImageType(path):
    if path[-4:] in [".jpg", ".png", ".gif"]:return path[-3:]
    elif path[-4:] in [".jpeg"]: return path[-4:]
    else: return None

def getUrlImageData(url):
    imagetype = getImageType(url)
    if imagetype==None:return url
    if imagetype=="jpg":return url
    rawdata = urllib2.urlopen(url).read()
    out=open("/users/steven/desktop/t."+imagetype,'w')
    try: out.write(rawdata)
    finally: out.close()
    input=open("/users/steven/desktop/t."+imagetype,"rb")
    try: rawdata = input.read()
    finally: input.close()
    if rawdata==None: return url
    data = base64.encodestring(rawdata)
    resultdata = ""
    for char in data:
        if char!="\n" and char!="\r": resultdata+=char
    resultdata = "data:image/" + imagetype + ";base64," + resultdata
    return resultdata

def getLocalImage(path):
    imagetype = getImageType(path)
    if imagetype==None:return path
    fin = open(path, "rb")
    try: rawdata = fin.read()
    finally: fin.close()
    data = rawdata.encode('base64')
    resultdata = ""
    for char in data:
        if char!="\n" and char!="\r": resultdata+=char
    resultdata = "data:image/" + imagetype + ";base64," + resultdata
    return resultdata

# Call methods below if you need
# Parse url or local image path and get data
def getImageContents(path):
    if re.match(r"[a-zA-z]+://([a-zA-Z0-9.]+[/]{0,})+",path):contents = getUrlImageData(path)
    else:contents = getLocalImage(path)
    return contents


# Parse youtube url and construct iframe for youtube
# format:https://www.youtube.com/watch?v=XXXXXXXXX...
# or http://youtu.be/XXXXXXXXX
# XXXXXXXXX should be videoid
def getYoutubeVideoContents(url):
    prefix = "http://www.youtube.com/embed/"
    suffix = "?enablejsapi=1&origin=http://www.youtube.com"
    if url[:32]=="https://www.youtube.com/watch?v=":return prefix+url[32:43]+suffix
    elif url[:16]=="http://youtu.be/":return prefix+url[16:27]+suffix
    else: return url






