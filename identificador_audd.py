import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import json

API_KEY = "sua_chave_de_api"  # Substitua pela sua chave de API

def identificar_musica(caminho_arquivo):
    url = "https://api.audd.io/"
    data = {
        'api_token': API_KEY,
        'return': 'timecode,apple_music,spotify',
    }
    files = {
        'file': open(caminho_arquivo, 'rb'),
    }
    print("Enviando solicitação para a API...")  # Debug
    response = requests.post(url, data=data, files=files)
    print(f"Código de status da resposta: {response.status_code}")  # Debug
    print(f"Resposta da API: {response.text}")  # Debug
    resultado = response.json()
    return resultado

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivo MP3", "*.mp3")])
    if caminho_arquivo:
        resultado = identificar_musica(caminho_arquivo)
        exibir_resultado(resultado)

def exibir_resultado(resultado):
    if 'result' in resultado:
        info = resultado['result']
        mensagem = f"Artista: {info['artist']}\nMúsica: {info['title']}\nÁlbum: {info.get('album', 'Desconhecido')}"
        messagebox.showinfo("Resultado", mensagem)
    else:
        mensagem = f"Erro: {resultado.get('status', 'Desconhecido')}"
        messagebox.showerror("Erro", mensagem)

# Criação da janela principal
janela = tk.Tk()
janela.title("Identificador de Música")
janela.geometry("300x150")

# Botão para selecionar arquivo
btn_selecionar = tk.Button(janela, text="Selecionar Arquivo MP3", command=selecionar_arquivo)
btn_selecionar.pack(pady=20)

# Executa a aplicação
janela.mainloop()
