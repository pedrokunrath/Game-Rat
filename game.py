import tkinter as tk
import random
from PIL import Image, ImageTk

def iniciar_jogo():
    botao_iniciar.pack_forget()
    atualizar_tempo()
    mover_botao()

def clique_botao():
    global score
    score += 1
    label_score.config(text=f"Pontos: {score}")
    mover_botao()

def mover_botao():
    if tempo_restante > 0:
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        botao.place(x=x, y=y)
        janela.after(3500, mover_botao)  

def atualizar_tempo():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        label_tempo.config(text=f"Tempo: {tempo_restante}s")
        janela.after(1000, atualizar_tempo)
    else:
        fim_do_jogo()

def fim_do_jogo():
    botao.config(state="disabled")
    botao.place_forget()
    
    if score > 10:
        mensagem_final = f"Fim de jogo\n Pontuação final: {score}\nParabéns voce ganhou"
    else:
        mensagem_final = f"Fim de jogo\n Você perdeu! Pontuação final: {score}"
    
    fim_label = tk.Label(janela, text=mensagem_final, font=("Arial", 30), fg="white", bg="black")
    fim_label.pack(pady=20)


janela = tk.Tk()
janela.title("Python Game")
janela.config(background="black")
janela.geometry("900x900")

score = 0
tempo_restante = 30

label_tempo = tk.Label(janela, text=f"Tempo: {tempo_restante}s", font=("Arial", 20), fg="white", bg="black")
label_tempo.pack(pady=20)

label_score = tk.Label(janela, text=f"Pontos: {score}", font=("Arial", 20), fg="white", bg="black")
label_score.pack(pady=20)

imagem = Image.open("./img/image-removebg-preview (4).png")
imagem = imagem.resize((100, 100))
imagem_tk = ImageTk.PhotoImage(imagem)

botao = tk.Button(janela, image=imagem_tk, borderwidth=0, command=clique_botao, background= "black")


botao_iniciar = tk.Button(janela, text="Iniciar", font=("Arial", 20), fg="white", bg="green", command=iniciar_jogo)
botao_iniciar.pack(pady=20)

janela.mainloop()
