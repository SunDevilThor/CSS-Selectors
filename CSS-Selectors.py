# CSS Selectors - Books to Scrape
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTMLSession

s = HTMLSession()
r = s.get('https://books.toscrape.com/')

#sel = 'title'
#sel = 'div'
#sel = '#default'
#sel = '.default'
#sel = 'body.default'
#sel = '.header.container-fluid'
#sel = '.col-xs-6.col-sm-4.col-md-3.col-lg-3'
#sel = 'ol li'
#sel = 'ol.row li'
#sel = 'ol.row + div'
#sel = 'body > div > div > div > div > section > div:nth-child(2) > ol'
#sel = 'div[role=alert]'
#sel = '[type=submit]'
#sel = 'button[type=submit]'
#sel = 'a[href]'
#sel = 'img.thumbnail'
#sel = 'img[src]'
sel = 'a img[src]'

print(r.html.find(sel))