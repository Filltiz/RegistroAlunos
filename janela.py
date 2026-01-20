import pandas as pd
import customtkinter as ctk
import tkinter as tk

pd.set_option('display.max_columns', None)

# Função para adicionar aluno e processar os dados
def adicionar_aluno():
    global dados, notaM, alunoMax, alunosAprovados, alunosReprovados, mediaClasse, cont

    nome = nome_entry.get()
    try:
        ra = int(ra_entry.get())
        nota1 = float(nota1_entry.get().replace(',', '.'))
        nota2 = float(nota2_entry.get().replace(',', '.'))
        nota3 = float(nota3_entry.get().replace(',', '.'))
    except ValueError:
        resultado_label.configure(text="Por favor, insira os dados válidas.")
        return

    # Verificar se as notas estão entre 0 e 10
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        resultado_label.configure(text="Notas devem estar entre 0 e 10.")
        return
    # Certificar se os RA não passa de 10 caracteres
    if not (len(str(ra)) <= 10):
        resultado_label.configure(text="O RA só pode ter até 10 caracteres.")
        return

    mediaAluno = (nota1 + nota2 + nota3) / 3
    aluno = {"Nome": nome, "RA": ra, "Média": mediaAluno}
    dados.append(aluno)
    mediaClasse += mediaAluno
    cont += 1

    if mediaAluno > notaM:
        notaM = mediaAluno
        alunoMax = aluno

    if mediaAluno < 6:
        alunosReprovados.append(aluno)
    else:
        alunosAprovados.append(aluno)

    atualizar_resultados()

    # Limpar os campos de entrada após adicionar o aluno
    nome_entry.delete(0, tk.END)
    ra_entry.delete(0, tk.END)
    nota1_entry.delete(0, tk.END)
    nota2_entry.delete(0, tk.END)
    nota3_entry.delete(0, tk.END)
    print(cont)


def atualizar_resultados():
    resultados_texto = ""
    aprovados_texto = ""
    reprovados_texto = ""

    for aluno in dados:
        resultados_texto += f"{aluno['Nome']} - RA: {alunoMax['RA']:010} - Média: {aluno['Média']:.1f}\n"

    if alunoMax:
        resultado_label.configure(text=f"A maior nota:\n{alunoMax['Nome'].title().strip()}"
                                       f" RA: {alunoMax['RA']:010}, Média: {alunoMax['Média']:.1f}")
    else:
        resultado_label.configure(text="Nenhum aluno registrado.")

    for aluno in alunosAprovados:
        aprovados_texto += f"{aluno['Nome'].title().strip()} - RA: {aluno['RA']:010} - Média: {aluno['Média']:.1f}\n"

    for aluno in alunosReprovados:
        reprovados_texto += f"{aluno['Nome'].title().strip()} - RA: {aluno['RA']:010} - Média: {aluno['Média']:.1f}\n"

    aprovados_label.configure(text=f"Aprovados(as): \n{aprovados_texto}")

    reprovados_label.configure(text=f"Reprovados(as): \n{reprovados_texto}")

    mediaClasse_label.configure(text=f"A média da classe: {mediaClasse/cont:.1f}")


# Inicialização da aplicação
#
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.title("Cadastro de Alunos")
app.geometry("1000x700")

# Criar campos de entrada
nome_label = ctk.CTkLabel(app, text="Nome:")
nome_label.pack(pady=10)
nome_entry = ctk.CTkEntry(app)
nome_entry.pack(pady=5)

ra_label = ctk.CTkLabel(app, text="RA:")
ra_label.pack(pady=5)
ra_entry = ctk.CTkEntry(app)
ra_entry.pack(pady=5)

nota1_label = ctk.CTkLabel(app, text="Nota da primeira prova:")
nota1_label.pack(pady=5)
nota1_entry = ctk.CTkEntry(app)
nota1_entry.pack(pady=5)

nota2_label = ctk.CTkLabel(app, text="Nota da segunda prova:")
nota2_label.pack(pady=5)
nota2_entry = ctk.CTkEntry(app)
nota2_entry.pack(pady=5)

nota3_label = ctk.CTkLabel(app, text="Nota de projeto:")
nota3_label.pack(pady=5)
nota3_entry = ctk.CTkEntry(app)
nota3_entry.pack(pady=5)

# Botão para adicionar aluno
adicionar_button = ctk.CTkButton(app, text="Adicionar Aluno", command=adicionar_aluno)
adicionar_button.pack(pady=20)

# Labels para resultados
resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=10)

aprovados_label = ctk.CTkLabel(app, text="Aprovados(as):")
aprovados_label.pack(pady=10)

reprovados_label = ctk.CTkLabel(app, text="Reprovados(as):")
reprovados_label.pack(pady=10)

mediaClasse_label = ctk.CTkLabel(app, text="Média da classe:")
mediaClasse_label.pack(pady=10)

# Variáveis para armazenar dados
dados = []
alunoMax = {}
alunosAprovados = []
alunosReprovados = []
notaM = 0
mediaClasse = 0
cont = 0
# Executar a aplicação
app.mainloop()
