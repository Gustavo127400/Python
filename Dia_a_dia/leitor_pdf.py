import PyPDF2
import pandas as pd


# Passo 1: Definir o caminho do arquivo
c_arquivo = r"C:\Users\gusta\Downloads\extraindo_arquivos-pdf\conta_vivo.pdf"

# Passo 2: Fazer uma função que leia e extraia os arquivos
with open(c_arquivo, "rb") as arquivo:
    leitor_pdf = PyPDF2.PdfReader(arquivo)
    info = ''
    
    # Iterar sobre cada página e extrair o texto
    for pagina in range(len(leitor_pdf.pages)):
        info += leitor_pdf.pages[pagina].extract_text()

# Passo 3: Organizar os dados
linhas = info.split('\n')  # Separar por linhas
dados = [linha.split() for linha in linhas if linha.strip()]  # Separar por espaço ou outro delimitador

# Passo 4: Criar o DataFrame
df = pd.DataFrame(dados)

# Exibir o DataFrame
print(df)

# Exportar para CSV
df.to_csv('dados_organizados.csv', index=False)