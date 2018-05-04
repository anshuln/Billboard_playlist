#script creates the link of a youtube playlist of the top 50 songs of billboard top 100
from bs4 import BeautifulSoup as BS
import urllib.request
def convert_spaces(s):
    x=0
    
    while(x<len(s)):
        if(s[x]==' '):
            s=s[:x]+'+'+s[x+1:]
        x+=1
    return str(s)


buff_link=""
playlist_container="http://www.youtube.com/watch_videos?video_ids="
source="http://www.billboard.com/charts/youtube"
source = "https://www.billboard.com/charts/hot-100"
page = urllib.request.urlopen(source)
body = page.read()
soup = BS(body, 'html.parser')
page.close()
pl=soup.find_all("div",class_="chart-row__title")
x=1
for it in pl:
    
    title=str(it.h2)
    title=(title[28:len(title)-5])
    artist=str(it.span)
    
    if(len(artist)>4):
        artist=artist[33:len(artist)-7]
    else:
        buff=it.find("a",class_="chart-row__artist")
        artist=str(buff["href"])
        artist=artist[7:len(artist)]
        
    final=title+" by "+artist
    buff=convert_spaces(final)
    if(x<=50):
        print(x)
        print(final)
        source = "https://www.youtube.com/results?search_query="+buff
        page = urllib.request.urlopen(source)
        body = page.read()
        soup = BS(body, 'html.parser')
        page.close()
        yt=soup.find_all("a")
        for it in yt:
            s=str(it["href"])
            if '/watch?' in s:
                break
        buff_link+=s[9:len(s)]+","
    if(x>50):
        break
    x+=1
    playlist_link=playlist_container+buff_link[:len(buff_link)-1]
    print(playlist_link)
playlist_link=playlist_container+buff_link[:len(buff_link)-1]
print(playlist_link)
