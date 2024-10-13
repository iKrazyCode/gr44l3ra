import requests

url = "https://era.graalonline.com/cdn-cgi/apps/head/j-Kn1ppMo0qxwSerh20p5M66z4g.js"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "game=era; /idbfs/33b28fcee7db5511f69dba35d2c3830a/files/creationtime.dat=1716061201.0ssss0999999;",
    "Pragma": "no-cache",
    "Priority": "u=1, i",
    "Referer": "https://era.graalonline.com/",
    "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Ts-Request-Embed-Key": "9e1fb267-22ec-4e7d-a551-b8484d38197b:bf7a8f6f8efbe8442dc821b114fc255e354f5651c9e8bce66ecd99178a8ec56f",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.headers)
print(response.text)

        








