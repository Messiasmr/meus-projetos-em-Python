import os

caminho_imagem = "C:\\Users\\marmo\\Desktop\\licao\\patoshino.jpg"
if os.path.exists(caminho_imagem):
    print("Arquivo encontrado:", caminho_imagem)
    image = Image.open(caminho_imagem)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
else:
    print("Arquivo não encontrado:", caminho_imagem)
