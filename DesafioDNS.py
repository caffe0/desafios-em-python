n = int(input('quantos servidores voce vai entrar\n')) #quantidade de urls
k = int(input('qual o tempo de resposta do servidor?\n'))
m = int(input('qual o tempo de resposta da máquina?\n'))
cacheDns = int(input('qual a memória do servidor dns?\n'))
url = []
for i in range(n):
    urlNv = input()
    if len(url)<=cacheDns:
        if urlNv in url:
            indexNovo = url.index(urlNv)
            indexNovo = int(indexNovo)
            indexRem = url[0]
            url[0],url[indexNovo]=url[indexNovo], url[0]
        url.append(urlNv)
    if len(url)>cacheDns:
        url.pop(len(url)-1)
    print(url)
