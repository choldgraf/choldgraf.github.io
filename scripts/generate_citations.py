import requests
from bs4 import BeautifulSoup as bs
from IPython.display import HTML
import numpy as np
import os

names = ['CR Holdgraf', 'C Holdgraf']
base_url = 'http://scholar.google.com'

url = base_url + '/citations?hl=en&user=fJmcIEIAAAAJ&view_op=list_works&sortby=pubdate'
resp = requests.post(url)
html = bs(resp.text, 'html5lib')

articles = html.find_all('tr', attrs={'class': 'gsc_a_tr'})
citations = ''
for article in articles:
    link = article.find_all('a', attrs={'class': 'gsc_a_at'})[0]
    title = link.text
    authors, journal = article.find_all('div', attrs={'class':"gs_gray"})
    authors, journal = [ii.text for ii in [authors, journal]]

    ixs = np.array([authors.find(nm) for nm in names])
    ix_match = np.argwhere(ixs != -1)
    if len(ix_match) > 0:
        string_match = names[ix_match[0, 0]]
        left, right = authors.split(string_match)
        authors = '{}**{}**{}'.format(left, string_match, right)
    url_paper = link.attrs['href']
    citations += '\n* [{}]({}). {}. *{}*'.format(
        title, base_url + url_paper, authors, journal)

with open(os.path.expanduser('~/Dropbox/github/publicRepos/choldgraf.github.io/content/pages/projects.md_raw'), 'r') as ff:
    lines = ff.readlines()

ix_papers = np.where([line.startswith('## Papers') for line in lines])[0][0]
lines.insert(ix_papers + 2, citations)
with open(os.path.expanduser('~/Dropbox/github/publicRepos/choldgraf.github.io/content/pages/projects.md'), 'w') as ff2:
    ff2.writelines(lines)
print('Done generating citations...')
