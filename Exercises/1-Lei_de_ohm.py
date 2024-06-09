import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular():
    grandeza = grandeza_var.get()
    
    try:
        if grandeza == "V":
            i = float(entry_corrente.get())
            r = float(entry_resistencia.get())
            u = r * i
            resultado.set(f"O valor da tensão é: {u} V")
        elif grandeza == "I":
            u = float(entry_tensao.get())
            r = float(entry_resistencia.get())
            i = u / r
            resultado.set(f"O valor da corrente é: {i} A")
        elif grandeza == "R":
            u = float(entry_tensao.get())
            i = float(entry_corrente.get())
            r = u / i
            resultado.set(f"O valor da resistência é: {r} Ω")
        else:
            messagebox.showerror("Erro", "Escolha inválida. Por favor, escolha V, I ou R.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora da Lei de Ohm")

# Variável para armazenar a escolha da grandeza
grandeza_var = tk.StringVar(value="V")
resultado = tk.StringVar()

# Título
titulo = ttk.Label(root, text="Calculadora da Lei de Ohm", font=("Helvetica", 16))
titulo.pack(pady=10)

# Opções de grandeza
frame_opcoes = ttk.Frame(root)
frame_opcoes.pack(pady=10)

ttk.Label(frame_opcoes, text="Escolha a grandeza que você deseja calcular:").pack(anchor=tk.W)
ttk.Radiobutton(frame_opcoes, text="Tensão (V)", variable=grandeza_var, value="V").pack(anchor=tk.W)
ttk.Radiobutton(frame_opcoes, text="Corrente (I)", variable=grandeza_var, value="I").pack(anchor=tk.W)
ttk.Radiobutton(frame_opcoes, text="Resistência (R)", variable=grandeza_var, value="R").pack(anchor=tk.W)

# Entradas de dados
frame_entradas = ttk.Frame(root)
frame_entradas.pack(pady=10)

ttk.Label(frame_entradas, text="Tensão (V):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_tensao = ttk.Entry(frame_entradas)
entry_tensao.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entradas, text="Corrente (I):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_corrente = ttk.Entry(frame_entradas)
entry_corrente.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_entradas, text="Resistência (R):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_resistencia = ttk.Entry(frame_entradas)
entry_resistencia.grid(row=2, column=1, padx=5, pady=5)

# Botão de cálculo
btn_calcular = ttk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)

# Resultado
label_resultado = ttk.Label(root, textvariable=resultado, font=("Helvetica", 14))
label_resultado.pack(pady=10)

# Iniciar a aplicação
root.mainloop()
