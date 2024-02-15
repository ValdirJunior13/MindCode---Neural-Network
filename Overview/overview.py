import os
import tkinter as tk
from tkinter import filedialog
from transformers import RobertaTokenizer, RobertaForCausalLM

root = tk.Tk()
root.withdraw()

# Abrir a caixa de diálogo de seleção de arquivos e obter o caminho do arquivo
filename = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])

print("Caminho do arquivo selecionado:", filename)

# Verificar se o usuário selecionou um arquivo
if filename:
    # Ler o conteúdo do arquivo
    with open(filename, 'r') as f:
        code = f.read()

    # Inicializa o tokenizador e o modelo
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = RobertaForCausalLM.from_pretrained('roberta-base')

    # Função para identificar erros no código Python
    def identify_errors(code):
        try:
            exec(code)
            return "Nenhum erro encontrado."
        except Exception as e:
            return str(e)

    # Função para gerar uma solução para os erros identificados
    def generate_solution(errors):
        # Tokeniza o prompt
        inputs = tokenizer.encode(
            "Erros identificados:\n\n" + errors + "\n\nSolução:\n\n", return_tensors="pt")

        # Gera o texto
        outputs = model.generate(inputs, max_length=300, do_sample=True)

        # Decodifica o texto gerado
        return tokenizer.decode(outputs[0])

    # Identificar os erros no código do arquivo
    errors = identify_errors(code)
    print("Erros identificados:", errors)

    # Se houver erros, gerar uma solução
    if errors != "Nenhum erro encontrado.":
        solution = generate_solution(errors)
        print("\nSolução proposta:\n", solution)

        # Escrever os erros e a solução em um arquivo .txt
        with open('errors_and_solution.txt', 'w') as f:
            f.write("Erros identificados:\n")
            f.write(errors)
            f.write("\n\nSolução proposta:\n")
            f.write(solution)
else:
    print("Nenhum arquivo selecionado.")
