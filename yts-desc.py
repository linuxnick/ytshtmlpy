from rss_parser import Parser
from requests import get

rss_url = "https://yts.mx/rss"
xml = get(rss_url)

# Limit feed output to 5 items
# To disable limit simply do not provide the argument or use None
parser = Parser(xml=xml.content, limit=None)
feed = parser.parse()

# Print out feed meta data
#print(feed.language)
#print(feed.version)

# Iteratively print feed items
ita = 1
for item in feed.feed:
    print(ita ," ",item.title)
    ita = ita + 1
    print(item.description)
