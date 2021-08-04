# Crie um codigo em python que teste se o site pudim esta acessivel pelo computador usado

import urllib
import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('Deu ruim')
else:
    print('Tudo Ok')
    print(site.read())

