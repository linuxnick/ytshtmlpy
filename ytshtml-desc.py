# import module
import webbrowser
from rss_parser import Parser
from requests import get
rss_url = "https://yts.mx/rss"
xml = get(rss_url)
parser = Parser(xml=xml.content, limit=None)
feed = parser.parse()
#print(feed.language)
#print(feed.version)
ita = 1
Func = open("ytstitle.html","w")
out = "<html>\n<head>\n<title> \nOutput Data in an HTML file\n </title></head><body>"
feed2 = " "
for item in feed.feed:
    feed2 = feed2 + "<br>" + item.title + "<br>" + item.description
out = out + feed2
Func.write(out)
Func.close()
webbrowser.open('ytstitle.html')

