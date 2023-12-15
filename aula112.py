import os

caminho_procura = 'C:\\Users\\NOTE\\Downloads\\ProjetoA3_Modelagem'
termo_procura = '1'

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
            except PermissionError as e:
                print('Sem permissão')
            except FileNotFoundError as e:
                print('não foi localizado nenhum arquivo')
            except Exception as e:
                print('Erro inesperado', e)
print()
print(f'{conta}arquivo(s) encontrado(s)')
