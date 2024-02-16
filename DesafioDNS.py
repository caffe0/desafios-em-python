#ESTE CÓDIGO SERVE PARA SIMULAR UMA LIMPEZA DA MEMÓRIA MATRIZ DE UM SERVIDOR E DA MEMÓRIA CACHE DO HISÓRICO DE LINKS URLS UTILIZADAS PELO USUÁRIO#
n = int(input('quantos servidores voce vai entrar\n')) #quantidade de urls
k = int(input('qual o tempo de resposta do servidor?\n'))
m = int(input('qual o tempo de resposta da máquina?\n'))
cacheDns = int(input('qual a memória do servidor dns?\n'))
url = []
for i in range(n):
    urlNv = input('Digite a url que você deseja entrar: \n')
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
