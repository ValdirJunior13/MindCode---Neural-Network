import re
import subprocess 

with open('README.md', 'r', enconding='utf-8') as file:
    content = file.read()
code_blocks = re.findall(r'```([\s\S]*?)', content)

for i, code_blocks in enumerate(code_blocks, start=1):
    if 'pip install' in code_blocks:
        print(f"Encontrado pip install no bloco de código {i}:\n{code_blocks.strip()}\n")

        code_lines = code_blocks.split("\n")

        for code_line in code_lines:
            with open('requirements.txt', 'a', enconding='utf-8') as output_file:
                output_file.write(code_line + '\n')

comando = ['python', "main.py"]
subprocess.run(comando, check=True)