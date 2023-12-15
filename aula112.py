import os

caminho_procura = input('Digite um Caminho: ')
termo_procura = input('Digite um Termo: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        tamanho = tamanho
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'Kb'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'Mb'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'Gb'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'Tb'
    else:
        tamanho /= peta
        texto = 'Pb'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('I found the archive:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensao:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho Formatado: ', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissão')
            except FileNotFoundError as e:
                print('não foi localizado nenhum arquivo')
            except Exception as e:
                print('Erro inesperado', e)
print()
print(f'{conta} arquivo(s) encontrado(s)')
