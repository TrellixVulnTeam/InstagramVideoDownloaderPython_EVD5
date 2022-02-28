import re
import requests
from bs4 import BeautifulSoup
import urllib.request as DFU
import os
from termcolor import colored

url = input("Enter URL: ")

data = requests.get(url)
# print(data)

str = data.text
# print(str)

match = re.findall(r'video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count', str)
# match = re.findall(r’video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count’, str)

extraction = '.mp4'

page = BeautifulSoup(str, "html.parser")
title = page.find("title")
title = title.get_text()

title = re.sub(r"\W+", "_", title)
title = "download/sarjsk991"+title+"Sarjsk991"
print("\n"+title)



if res != "" :
    print('found \n \n'+'\033[1m'+colored(res, 'green')+'\033[0m'+'\n') #'found word:cat'
    download = input("Do you want to download(y/N) : ")
if (download == "y" or download == "Y"):
  try:
      fileName = title
      print("Downloading.....")
      DFU.urlretrieve(res, fileName+extraction)
      print("Download Successfully!")
      os.system("tree download")
    except:
       print("Sorry! Download Unsuccessful")

    else:
       print('did not find or post is from private account')
       exit()