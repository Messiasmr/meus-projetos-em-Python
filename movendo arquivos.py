import os
import shutil

def organizar_por_extensao(diretorio):
    extensoes = {
        'txt': 'Arquivo TXT',
        'png': 'Arquivo PNG',
        'docx': 'Arquivo DOCX',
        'pdf': 'Arquivo PDF',
        'jpg': 'Arquivo JPG'
    }

    for destino in extensoes.values():
        caminho_destino = os.path.join(diretorio, destino)
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao[1:].lower()
            if extensao in extensoes:
                caminho_destino = os.path.join(diretorio, extensoes[extensao], arquivo)
                shutil.move(caminho_arquivo, caminho_destino)
                print(f'movido: {arquivo} para {destino}')
dir_destino = "C:\organizado"
organizar_por_extensao(dir_destino)
