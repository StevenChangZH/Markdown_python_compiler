# ------------------------------------------------------------
# plyScripts_3_3.py
#
# Some scripts to provide better codes integration
# version 6.0 for Markdown_python_compiler
# NOTICE: this script only used for python version above 3.3
# ------------------------------------------------------------
import re
import base64
import urllib.request


# DO NOT call those methods directly
def getImageType(path):
    if path[-4:] in [".jpg", ".png", ".gif"]:return path[-3:]
    elif path[-4:] in [".jpeg"]: return path[-4:]
    else: return None

def getUrlImageData(url):
    imagetype = getImageType(url)
    if imagetype==None:return url
    if imagetype=="jpg":return url
    rawdata = urllib.request.urlopen(line).read()
    if rawdata==None: return url
    data = rawdata.encode('base64')
    resultdata = None
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

