import customtkinter as ctk
import random
from PIL import Image, ImageTk

def iniciar_jogo():
    global nome_jogador
    nome_jogador = entrada_nome.get().strip().upper()
    if nome_jogador:
        label_nome.pack_forget()
        entrada_nome.pack_forget()
        botao_iniciar.pack_forget()
        label_tempo.pack(pady=10)
        label_score.pack(pady=10)
        botao.place(x=400, y=300)
        janela.attributes('-fullscreen', True)
        atualizar_tempo()
        mover_botao()
    else:
        label_nome.configure(text="Digite seu nome antes de iniciar", text_color="red")

def clique_botao():
    global score
    score += 1
    label_score.configure(text=f"Pontos: {score}")
    mover_botao()

def mover_botao():
    if tempo_restante > 0:
        x = random.randint(50, janela.winfo_width() - 150)
        y = random.randint(50, janela.winfo_height() - 150)
        botao.place(x=x, y=y)
        janela.after(800, mover_botao)

def atualizar_tempo():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        label_tempo.configure(text=f"Tempo: {tempo_restante}s")
        janela.after(1000, atualizar_tempo)
    else:
        fim_do_jogo()

def fim_do_jogo():
    botao.place_forget()
    mensagem_final = f"Fim de jogo\n Pontuação final: {score}\nParabéns, {nome_jogador}, você ganhou!" if score > 10 else f"Fim de jogo\n {nome_jogador}, você perdeu! Pontuação final: {score}"
    fim_label = ctk.CTkLabel(janela, text=mensagem_final, font=("Arial", 30), text_color="white")
    fim_label.pack(pady=20)
    botao_reiniciar = ctk.CTkButton(janela, text="Reiniciar", font=("Arial", 20), text_color="white", fg_color="red", hover_color="#e57373", command=reiniciar_jogo)
    botao_reiniciar.pack(pady=20)

def reiniciar_jogo():
    global score, tempo_restante
    score = 0
    tempo_restante = 30
    label_tempo.configure(text=f"Tempo: {tempo_restante}s")
    label_score.configure(text=f"Pontos: {score}")
    for widget in janela.winfo_children():
        widget.pack_forget()
    tela_inicial()

def tela_inicial():
    label_nome.pack(pady=20)
    entrada_nome.pack(pady=10)
    botao_iniciar.pack(pady=20)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Python Game")
janela.geometry("900x900")

score = 0
tempo_restante = 30
nome_jogador = ""

label_nome = ctk.CTkLabel(janela, text="Digite seu nome para começar:", font=("Arial", 20), text_color="white")
entrada_nome = ctk.CTkEntry(janela, width=200, font=("Arial", 20))

label_tempo = ctk.CTkLabel(janela, text=f"Tempo: {tempo_restante}s", font=("Arial", 20), text_color="white")
label_score = ctk.CTkLabel(janela, text=f"Pontos: {score}", font=("Arial", 20), text_color="white")

imagem = Image.open("./img/image-removebg-preview (4).png")
imagem = imagem.resize((100, 100))
imagem_tk = ImageTk.PhotoImage(imagem)

botao = ctk.CTkButton(janela, image=imagem_tk, text="", fg_color="grey", hover_color="#333333", command=clique_botao)
botao_iniciar = ctk.CTkButton(janela, text="Iniciar", font=("Arial", 20), text_color="white", fg_color="green", hover_color="#3a9f5d", command=iniciar_jogo)

tela_inicial()

janela.mainloop()
