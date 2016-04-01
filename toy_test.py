import requests

headers = {
    'Host': 'kat.cr',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0 Iceweasel/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://duckduckgo.com',
    'Cookie': 'lang_detected=en; lang_code=en; country_code=BR; state=1455499884092',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}

resp = requests.get('https://kat.cr/search/new girl/', headers=headers)

with open('python.html', 'w') as arq:
    print(resp.text, file=arq)
