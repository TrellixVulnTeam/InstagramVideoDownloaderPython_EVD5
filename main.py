import requests
import re
import urllib.request

def getResponse(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})

#Enter url and call getResponse function
url = input('Enter Instagram URL: ')
response = getResponse(url)

#match link provided
videoUlrMatches = re.findall('"video_url":"([^"]+)"', response)
picUrlMatches = re.findall('"display_url":"([^"]+)"', response)

vidUrls = prepare_urls(videoUlrMatches)
picUrls = prepare_urls(picUrlMatches)

if vidUrls:
    vidLink = (vidUrls[0])
    r = requests.get(vidLink, allow_redirects=True)
    open('newvideo.mp4', 'wb').write(r.content)
# if picUrls:
#     picLink = (picUrls[0])
#     r = requests.get(picLink, allow_redirects= True)
#     open('ig.png', 'wb').write(r.content)

if not (vidUrls or picUrls):
    print('Could not find media in the provided url. Please Provide another link')



# video_file_name = "downloadedvideo.mp4"
# piture_file_name = "downloadedimage.jpg"

# req = urllib.request.build_opener()
# req.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')]
# urllib.request.install_opener(req)

# urllib.request.urlretrieve(imageUrl, piture_file_name)

