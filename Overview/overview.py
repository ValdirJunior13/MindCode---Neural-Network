import openai
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Abre a caixa de diálogo de seleção de arquivos e obtém o caminho do arquivo
filename = filedialog.askopenfilename()

print("Caminho do arquivo selecionado:", filename)

openai.api_key = "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"

# Escolha um modelo da open ai (por exemplo, davinci)
model = "gpt-3.5-turbo-0125"

# Função para ler um arquivo Python e identificar erros


def identify_errors(filename):
    with open(filename, 'r') as f:
        code = f.read()

    # Verifica os erros no código usando exec
    try:
        exec(code)
        return "Nenhum erro encontrado."
    except Exception as e:
        return str(e)

# Função para gerar uma solução para os erros identificados


def generate_solution(errors):
    prompt = "Erros identificados:\n\n" + errors + "\n\nSolução:\n\n"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.9,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"])
    return response["choices"][0]["text"]


# Verifica se o arquivo inserido pelo usuário é válido
if not os.path.isfile(filename):
    print("O arquivo especificado não é válido.")
    exit()

# Identifica os erros no código
errors = identify_errors(filename)
print("Erros identificados:", errors)

# Se houver erros, gera uma solução
if errors != "Nenhum erro encontrado.":
    solution = generate_solution(errors)
    print("\nSolução proposta:\n", solution)

    # Escreve os erros e a solução em um arquivo .txt
    with open('errors_and_solution.txt', 'w') as f:
        f.write("Erros identificados:\n")
        f.write(errors)
        f.write("\n\nSolução proposta:\n")
        f.write(solution)
