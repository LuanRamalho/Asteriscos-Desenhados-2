import tkinter as tk
import random

def desenhar_asteriscos():
    # Limpa a tela antes de desenhar novos asteriscos
    canvas.delete("all")

    # Define o número de asteriscos a ser desenhado aleatoriamente (entre 10 e 100)
    quantidade = random.randint(10, 100)

    # Desenha os asteriscos
    for _ in range(quantidade):
        # Gera uma posição aleatória dentro da área do canvas
        x = random.randint(0, largura_canvas)
        y = random.randint(0, altura_canvas)

        # Escolhe uma cor aleatória
        cor = random.choice(["red", "green", "blue", "yellow", "purple", "orange", "cyan"])

        # Desenha o asterisco
        canvas.create_text(x, y, text="*", fill=cor, font=("Arial", 16))

# Configurações da janela principal
largura_canvas = 800
altura_canvas = 600

janela = tk.Tk()
janela.title("Desenho de Asteriscos Aleatórios")

# Cria um canvas para desenhar
canvas = tk.Canvas(janela, width=largura_canvas, height=altura_canvas, bg="white")
canvas.pack()

# Botão para gerar os asteriscos
botao = tk.Button(janela, text="Desenhar Asteriscos", command=desenhar_asteriscos)
botao.pack(pady=10)

# Inicia o loop principal do tkinter
janela.mainloop()
